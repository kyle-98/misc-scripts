from pytube import YouTube as YT
import re
import os
import ffmpeg

def download_vid_720(save_dir, link):
    video = YT(link)
    file = video.streams.get_highest_resolution()
    print(f'>>> Downloading {file.title}')
    file_name = re.sub(r'[\"\\/\?;*<>|]', '', file.title)
    file.download(output_path=save_dir, filename=rf"{file_name}.mp4")
    print(f'done downloading {file.title}')

def download_vid_HD(save_dir, link):
    try:
        video = YT(link)
        file = video.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()
        print(f'>>> Downloading {file.title}')
        audio = video.streams.filter(only_audio=True).first()
        file_name = re.sub(r'[\"\\/\?;*<>|]', '', file.title)
        file.download(output_path=save_dir, filename=rf"{file_name}.mp4")
        audio.download(output_path=save_dir, filename=rf'{file_name}_audio.mp4')
        print(f'done downloading {file.title}')
        video_feed = ffmpeg.input(f'{save_dir}\\{file_name}.mp4')
        audio_feed = ffmpeg.input(f'{save_dir}\\{file_name}_audio.mp4')

        ffmpeg.concat(video_feed, audio_feed, v=1, a=1).output(f'{save_dir}\\{file_name}_completed.mp4').run()
        os.remove(f'{save_dir}\\{file_name}.mp4')
        os.remove(f'{save_dir}\\{file_name}_audio.mp4')
    except:
        print(f'>>> Failed to download {file.title}')

if __name__ == '__main__':
    path = input('Enter save path: ')
    print('ctrl + c to exit')
    while(True):
        quality = input('HD or 720: ')
        link = input('Enter link: ')
        if quality == "HD":
            download_vid_HD(path, link)
        else:
            download_vid_720(path, link)
