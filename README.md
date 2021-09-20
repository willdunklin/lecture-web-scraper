# lecture-web-scraper

Recently one of my favorite online classes of the pandemic period ended and I wanted to save the lecture videos for posterity. 
Unluckily for me, the video host Echo360 made it remarkably difficult to download any content on their site. 
So I set out to make this project, a webscraper/ffmpeg app in Python that will download Echo360 lectures to your heart's content.

## How it works

The project uses Selenium, more specifically selenium-wire, to open content on Echo360 and track the network traffic.
I investigated the source of the media and found it to be two tailored URLs, one for audio and ther other for video (even though both were in the same .m4s file format). 
After downloading the files, all that is left to do is to combine them using ffmpeg to output a shiny, brand new mp4.

### Dependencies
- ffmpeg
- ffmpeg-python
- selenium-wire
- re
- requests
