import speech_recognition as sr
from moviepy. editor import VideoFileClip,AudioFileClip,compositeAudioClip 
class MovieManager:

    def get_war_audio(self,mp4_file,war_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.Write_audifile(war_file,code='pcm_s16le',)
        ac.close()
        vc.close()
    
    def audio_to_text(self,audio_file):
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return 'unknow'
        




