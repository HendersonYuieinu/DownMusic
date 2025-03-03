from yt_dlp import YoutubeDL
import os

class download_API():
    def __init__(self):
        self.aviso = ''
        
    def get_downloads_folder(self):
        '''if os.name == 'nt':
            return os.path.join(os.environ['USERPROFILE'], 'Downloads')
        else:
            return os.path.join(os.environ['HOME'], 'Downloads')'''
        return 'musicas'

    def audio(self, video_url):
        self.Download_folder = self.get_downloads_folder()
        
        try:    

            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(self.Download_folder, '%(title)s.%(ext)s'),
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                
            return "COMPLETE"
        except Exception as e:
            return e
