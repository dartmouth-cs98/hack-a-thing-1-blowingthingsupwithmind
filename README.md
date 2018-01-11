# hack-a-thing-1-blowingthingsupwithmind
##### Brophy Tyree & Josh Kerber
## To run:
1. Open Emotiv CortexUI locally
2. Login using EmotivID
3. Connect headset
4. Run main script: "python main.py"
5. Blow things up with mind



For our Hack-a-thing, we played around with the Emotiv Insight headset - a 5-channel, wireless EEG headset that records your brainwaves and translates them into meaningful data. We begun by using the CortexUI to test out the capabilities of the headset. Using the Cortex UI, we were able to "control" an object floating in space. By training the headset to associate certain brain waves with certain desired effects, we were able to push the floating object backwards in space with our mind. After, we attempted to reproduce the application by building it from scratch. Working our way through the API, we tried to build a terminal interface that allowed us to train the headset to detect different commands and produce a GUI that displayed the movements of the object floating in space.

Unfortunately, we did not get the application up and running. While the API seemed nice and easy (it always does), it ended up producing a program that was very finicky. We were able to train the headset sometimes, but the Server would crash when we tried to train a second command. Sometimes, the first training session would crash the program. When we looked online at reviews of the headset, we found many people with similar concerns. The general consensus on the product was that it functions poorly and is quite difficult to use. We built the GUI, but were unable to integrate it with the headset. We tested it by having the 'd' key stand in for the signal returned by the headset. It would be very simple to integrate the GUI once the Emotiv API is functioning properly. 

Despite the fact that this product did not work well, the technology is fascinating and quite promising. When using the Cortex UI, we were able to get the "push" command working shockingly well. By thinking about the ball moving backwards in space, we were able to make it move backwards in space. This is an incredible experience. When we tried to train multiple commands (Up, Down, Right, Left), the program stopped working as well. I think that, with the relatively small amount of training we did to the system, the headset couldn't differentiate between the "push" brain waves and the brainwaves associated with the other desired commands. With many more hours of training and the premium headset (Emotive Epoc+), we could build an incredible application (assuming the API is improved for the premium headset). 

We would not recommend the Emotiv Insight after our experiences with it. The technology is not advanced enough in its current state and the API does not function correctly. It will be very frustrating, require many many hours of training (which is boring and cumbersome) and likely will not produce the desired effect. But I think that later (more expensive) iterations of this technology will build some awesome things

