from seleniumwire import webdriver
import requests
import ffmpeg
import re

# function to download media
def download(url, path):
    print('downloading:', url)
    # stream download the file from the location
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    f.close()
    return path

# read the list of lecture links from file
urls = open('links', 'r').readlines()

# create selenium-wire page
driver = webdriver.Firefox()

# regex pattern for the media links for echo360
media_pattern = re.compile(r'(https:\/\/content\.echo360\..+\/)s0q0\.m4s(\?.+)')

requests_total = 0

for i, url in enumerate(urls):
    print(f'url[{i}]')
    
    # open the current url
    driver.get(url)

    found_media = False
    # the browser takes a while to capture the request, so spin until it is found
    while not found_media:
        # only iterate over the traffic from this page, (not previous) 
        for request in driver.requests[requests_total:]:

            # find the specific media links we're after
            result = media_pattern.match(request.url)
            if result != None:
                groups = result.groups()
                print(groups[0])
            
                # download the separate audio/video files
                download(f'{groups[0]}s0q0.m4s{groups[1]}', f'videos/audio{i}.m4s')
                download(f'{groups[0]}s1q1.m4s{groups[1]}', f'videos/video{i}.m4s')
                print('downloaded!')
            
                # break the while loop
                found_media = True
                # reset for the next page
                result = None
                # update where the end of the previous page traffic is now
                requests_total = len(driver.requests)

                # ffmpeg
                # get each media stream from respective files
                video_stream = ffmpeg.input(f'videos/video{i}.m4s')
                audio_stream = ffmpeg.input(f'videos/audio{i}.m4s')

                # concatenate them
                stream = ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output(video_stream, f'output/output{i}.mp4')

                # execute the ffmpeg instruction
                ffmpeg.run(stream)

                break