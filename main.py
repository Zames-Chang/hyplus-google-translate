# -*- coding: utf-8 -*-

import io
import os
from pydub import AudioSegment
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from pydub.utils import mediainfo
import math
import sys
def transcribe_file(speech_file,timer,language,mp3):
    if(language == "tw"):
        trans_lan = "cmn-Hant-TW"
    if(language == "cn"):
        trans_lan = "cmn-Hans-CN"
    """Transcribe the given audio file."""
    ratio = 60/timer
    client = speech.SpeechClient()
    my_path = os.path.abspath(os.path.dirname(__file__))
    sound = AudioSegment.from_file(my_path+"/"+speech_file,format = "flac")
    minute = int(math.floor(sound.duration_seconds/60))*ratio
    print("sound len:",len(sound))
    sound_list = []
    for i in range(minute):
        temp = sound[i*60*1000/ratio:(i+1)*60*1000/ratio]
        sound_list.append(temp)
    sound_list.append(sound[minute*60*1000/ratio:])
    second = 0
    counter = 0
    os.remove("output.txt")
    for sou in sound_list:
        sou = sou.set_frame_rate(48000).set_channels(1)
        sou.export("./456.flac", format="flac")
        with io.open("456.flac", 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)
            config = types.RecognitionConfig(
                encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
                sample_rate_hertz=48000,
                language_code=trans_lan)
            with open("output.txt","a") as text:
                if(second == 0 and counter < 10):
                    text.write("\n"+"[{}{}:{}]".format("0",counter,"00").encode('utf8'))
                elif(second == 0 and counter >= 10):
                    text.write("\n"+"[{}:{}]".format(counter,"00").encode('utf8'))
                elif(second != 0 and counter < 10):
                    text.write("\n"+"[{}{}:{}]".format("0",counter,second).encode('utf8'))
                else:
                    text.write("\n"+"[{}:{}]".format(counter,second).encode('utf8'))
                text.close()
            second += timer
            if(second == 60):
                counter += 1
                second = 0
            response = client.recognize(config, audio)
            # Each result is for a consecutive portion of the audio. Iterate through
            # them to get the transcripts for the entire audio file.
            for result in response.results:
                # The first alternative is the most likely one for this portion.
                print(u'Transcript: {}'.format(result.alternatives[0].transcript))
                with open("output.txt","a") as text:
                    text.write(result.alternatives[0].transcript.encode('utf8')+"\n")
                    text.close()
print("拜託你先去https://online-audio-converter.com/ 把該死的mp3 阿之類的格式轉乘flac格式再用")
#transcribe_file(sys.argv[1])
