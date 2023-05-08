# I2 Meta

### *Group members*

- Guchea Augusto
- Orellano Joaquin
- Peralta Lucio

### *Description of I2 Meta*

>I2 meta is a program that allows you to download videos in .mp3 or .mp4 format and play these files locally.

### *Functions:*

>1. Download youtube videos for free
>2. Download youtube audios for free

### *Interaction with the user:*

>Enter the url of the video and choose the file format to download.

### *Libraries*

>Our main library is [pytube](https://pytube.io/en/latest/)
>And our secondary library is [tkinter](https://docs.python.org/3/library/tkinter.html)

### *Instalation*

>To install [pytube](https://pytube.io/en/latest/)
paste the following line on bash:  

```bash
pip install git+https://github.com/pytube/pytube
```  

>And to install [Tkinter](https://docs.python.org/3/library/tkinter.html) paste the folowing line:

```bash
sudo apt-get install python3-tk
```

### *Possible problems:*

- If when downloading you get the "KeyGen" error, do the following: 

```bash
cd /home/USER/.local/lib/python3.10/site-packages/pytube
```   

>then put:  

```bash
open innertube.py
```   

>and look for the following line:  

```bash
class InnerTube:
    """Object for interacting with the innertube API."""
    def _init_(self, client='ANDROID', use_oauth=False, allow_cache=True):
```   

>and modify where it says "ANDROID" and replace it with "WEB"  

>It would look like this: 

```bash
class InnerTube:
    """Object for interacting with the innertube API."""
    def _init_(self, client='WEB', use_oauth=False, allow_cache=True):
```   

>And voila, the program should already work.