import ffmpeg

for i in range(28):
    video_stream = ffmpeg.input(f'videos/video{i}.m4s')
    audio_stream = ffmpeg.input(f'videos/audio{i}.m4s')
    stream = ffmpeg.concat(video_stream, audio_stream, v=1, a=1).output(video_stream, f'output/output{i}.mp4')

    ffmpeg.run(stream)