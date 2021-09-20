import ffmpeg

# this is hacked together
# this would otherwise be integrated into scrape.py

# iterate through the list of files (shouldn't be hardcoded to 28 for anyone with more/less than 28 lectures to download) 
for i in range(28):
    # get each media stream from respective files
    video_stream = ffmpeg.input(f'videos/video{i}.m4s')
    audio_stream = ffmpeg.input(f'videos/audio{i}.m4s')

    # concatenate them
    stream = ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output(video_stream, f'output/output{i}.mp4')

    # execute the ffmpeg instruction
    ffmpeg.run(stream)