"""
Emotiv object

Author:         Josh Kerber & Brophy Tyree
Date:           01/10/2018
Project:        CS98 Hack-a-thing 1
"""

from Util import *
import websocket
import socket
import ssl
import _thread
import json
import time
import os

class Emotiv:
    """Operations for communication with Emotiv Cortex"""
    def __init__(self):
        self.trained = False

        # for training session
        self.webSocket = None
        self.authToken = None
        self.sessionId = None

        # for authorization
        self.clientSecret = 's7DZupwKBGDUy8bgZUb8INqq265yRFSkFqAT1uDuQL6dMwSrmZTZtWMkzDw3MSiJikrZGIbtr3b89vx0wwWVO0N83D4SrkJ0mPQ1yhISxlwFZsikwFZ2cT6IRSmCJ5gB'
        self.clientId = 'afGFgm19lkKsJhIYzFSE7UZ8TIjhTk3s9Ktf7zS7'

    def test(self):
        """test mental commands"""
        for _ in range(60):
            res = self.webSocket.recv()
            if 'com' in res:
                com = json.loads(res)['com']
                method, score = com[0], com[1]

                # display active score
                print(method, score)
                time.sleep(0.25)
        inform('testing complete')

    def train(self, action):
        """train Emotiv mental command"""
        res = self.makeRequest('training', {
            "_auth":self.authToken,
            "detection":"mentalCommand",
            "session":self.sessionId,
            "action":"neutral",
            "status":"start"
        })
        if 'error' in res:
            print('training failed')
            return False

        # begin neutral training
        inform('starting up {} training'.format(action), clear=True, end='')
        inform('please wait')
        complete = False
        while not complete:
            time.sleep(3)
            res = self.webSocket.recv()

            # poll for training status
            if 'MC_Started' in res:
                inform('training {}...'.format(action.upper()))
            elif 'MC_Succeeded' in res:

                # accept successful training
                self.makeRequest('training', {
                    "_auth":self.authToken,
                    "detection":"mentalCommand",
                    "session":self.sessionId,
                    "action":action,
                    "status":"accept"
                })
                inform('training succeeded!', clear=True)
                return True
            elif 'MC_Failed' in res:
                inform('training failed', end='')
                inform('please try again')
                complete = True
            elif 'error' in res:
                inform('startup failed', end='')
                complete = True
        return False

    def subscribe(self):
        """subscribe to Emotiv stream"""
        res = self.makeRequest('subscribe', {
            "_auth": self.authToken,
            "streams": [
                "com",
                "sys" ]
        })
        if 'error' in res:
            return False
        return True

    def createSession(self):
        """establish Emotiv training session"""
        res = self.makeRequest('createSession', {
            "_auth": self.authToken,
            "status": "open"
        })
        if 'error' in res:
            return False

        # store session id
        resJson = json.loads(res)
        self.sessionId = resJson['result']['id']
        return True

    def authorize(self):
        """authenticate Emotiv user"""
        res = self.makeRequest('authorize')
        if 'error' in res:
            return False

        # store auth token
        resJson = json.loads(res)
        self.authToken = resJson['result']['_auth']
        return True

    def initialize(self):
        """initialize Emotiv session"""
        if self.authorize() and self.createSession() and self.subscribe():
            return True
        return False

    def makeRequest(self, method, params={}):
        """make request to Emotiv web socket"""
        self.webSocket.send(json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": 1
        }))
        return self.webSocket.recv()

    def connect(self, callback):
        """connect to Emotiv Cortex web socket"""
        websocket.enableTrace(True)
        self.webSocket = websocket.create_connection(
            'wss://emotivcortex.com:54321',
            sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),),
            sslopt={'cert_reqs': ssl.CERT_NONE},
            class_=CustomWebSocket)

        # run callback passed as param
        callback()

    def disconnect(self):
        """disconnect from Emotiv Cortex web socket"""
        self.webSocket.close()
