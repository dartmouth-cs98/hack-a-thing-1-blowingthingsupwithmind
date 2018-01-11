"""
Utility functions

Author:         Josh Kerber & Brophy Tyree
Date:           01/10/2018
Project:        CS98 Hack-a-thing 1
"""

import websocket
import json
import os

# verbose data reception
DEBUG = True

def inform(msg, clear=False, end='\n'):
    """display message to console"""
    if clear:
        os.system('clear')
    print('\n{}{}'.format(msg.upper(), end))

class CustomWebSocket(websocket.WebSocket):
    """Web socket with custom data reception"""
    def recv_frame(self):
        frame = super().recv_frame()
        data = frame.data.decode('utf-8')

        # parse error message
        if 'error' in data:
            err = json.loads(data)['error']['message']
            inform('ERROR: {}'.format(err), end='')
        elif DEBUG:
            print('RECV:', data)
        return frame
