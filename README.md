# ADAM
Automated Data Acquisition and Management


## Introduction

ADAM is my take on process control software using off-the-shelf components. 
It is currently centered around a Raspberry Pi Zero W with some additional components, connected to a hacked SilverCrest jam preserver using a GX16-8 8-Pin connector to interface the I2C-bus of the RasPi, which in turn is used to interface an ADS1115 as well as a ZS-042 RTC. It turns out that GX16-8 connectors are pretty nice to use in "rough" environments.


__I DO NOT RECOMMEND DOING THE MODIFICATIONS TO SAID JAM PRESERVER IF YOU ARE A NOVICE AS YOU HAVE TO WORK WITH HIGH VOLTAGE AND THUS MUST KNOW WHAT YOU ARE DOING__

On the software side, it is currently Raspbian Strech (Lite) in a headless configuration. Note that in order to acquire wireless connectivity, it seems best to install Raspbian onto the SD card, insert it into another Raspberry Pi with wireless chipset, run raspi-config and set the wireless country. While it is possible to set country in wpa_supplicant, it seems that this isn't always working as rfkill won't always accept it.

## Goal

The idea of ADAM was concieved while working at a SME brewery. The Goal is to develop a software suite for small or medium enterprises which allows for redundant, stable and precise control of brewery systems - while collecting meticously all necessary data. Furthermore it should make it possible for SMEs to cheaply upgrade their brewery systems so they can brew in a semi-automatic manner (in effect, by using an array of cheaply available sensors and for example Raspberry Pi compute modules or similar). 

## Notes

Original code for ADAM is years old and unfinished, which is why I will rewrite it to be more modern. Also I am considering a new design to the whole system. Original ADAM used a main server which would control a group of Raspberry Pi's connected to it using asyncio. That setup had similarities to a botnet (C&C infrastructure), but it worked surprisingly well.
Since ADAM is supposed to be redundant I want to figure out a way to:
- Connect to the control board of it via USB in case of network outage
- Be able to complete a task profile even if the network is disconnected
- Send all available data back to main server once network is restored

Original code will be uploaded to ADAM-Legacy branch once I have the time to review it.

## ToDo

- Figure out which software to use (Probably a stack of Python, vue.js, plot.ly and asyncio as the original iteration used)
- Figure out a software design that adheres to the principles of reliablility, usability and modifability
- Make a usable, intuitive UI
- Automatic registration of Raspberry Pi to main server when added to network and subsequent assortment of UUID (original used Unix Timestamp, but technically there might be issue if two raspberry pis were to try and acquire UUID at exactly the same time. Unlikely unless somebody tried to do such on purpose)
- Main server infrastructure
- Figure out how to do self-tuning PID using artificial intelligence in a way that allows for pre-emptive warning of possible equipment failure
- semi-automatic inventory system
- Encrypted customer database and invoicing system
- Granular Access control system (i.e. User 1 may be able to control brewing process but not see customer databse, while User 2 can see the customer database but not access the brewery system)

## Considerations

The first ADAM iteration ran in a client/server manner, with the server computing all necessary steps for the PID while the raspberry pi simply interfaced the jam preserver using GPIO. While this worked quite well, it is not reliable in case of a network outage.
Instead the new iteration should compile the information needed for the brewing process and send it to the client. This will allow the client to continue the process without issue even if there is unstable network connection. In order to be able to supervise the process in such a case, it is necessary for the client to be accessible by USB.

## Roadmap

1. Basic logic of Client-Server infrastructure
2. First UI iterations
3. Implementation and testing of features
4. Second UI iteration
5. ???

## Licensing

I have not yet decided on a license for this project as I am not certain how I can exclude certain companies from using my software in a legal manner (i.e. they might use it since it's open source, but I really really don't want them using it).

## Other notes

Why not use CraftBeerPi or similar? 
These software suites are great software for sure, but during initial development of ADAM i realized it could be used for so much more than brewing beer. ADAM in itself would be a process control suite that can be hacked to your process needs. Also, you don't learn new stuff as deeply by using pre-existing software as you do when writing your own.
