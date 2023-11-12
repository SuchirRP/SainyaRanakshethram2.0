# import required module
import speech_recognition as sr
import sys
import os
from pydub import AudioSegment
import tempfile
import subprocess
import shutil



# explicit function to take input commands
# and recognize them
def DecodeAudio(filename):

    r = sr.Recognizer()
    filesplit = os.path.splitext(filename)
    #print(filesplit[1])
    if filesplit[1].lower() == ".mp3":
        sound = AudioSegment.from_mp3(filename)
        output = tempfile.NamedTemporaryFile()
        sound.export(output, format="wav")
    elif filesplit[1].lower() == ".flac":
        sound = AudioSegment.from_file(filename)
        output = tempfile.NamedTemporaryFile()
        sound.export(output, format="wav")
    elif filesplit[1].lower() == ".wav":
        sound = AudioSegment.from_wav(filename)
        output = tempfile.NamedTemporaryFile()
        sound.export(output, format="wav")
    else :
        print ("Sorry file format not supported")
        return
    dirpath = tempfile.mkdtemp()
    shutil.copyfile(output.name, dirpath+"/raw.wav")
    outpath = tempfile.mkdtemp()

    os.system("/usr/bin/python3 -m denoiser.enhance --dns48   --noisy_dir="+dirpath+" "+"--out_dir="+outpath)
    cleanaudio = outpath+"/raw_enhanced.wav"
    sound.export(cleanaudio, format="wav")
    print("clean audio path is : ---")
    print(cleanaudio)

    #output_enhanced.wav
    with sr.AudioFile(cleanaudio) as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        print('Listening to raw audio file')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing Audio")
            Query = r.recognize_google(audio, language='en-IN')

            # for listening the command in indian english
            print("Audio trascript is :--  ' ", Query, "'")
            #Query = r.recognize_google(audio, language='hi-In')
            #print("the Hindi printed='", Query, "'")
            #ipd.Audio(output)

        # handling the exception, so that assistant can
        # ask for telling again the command
        except Exception as e:
            print(e)
            print("Sorry could not decode")
            return "None"
        return Query



# Driver Code

# call the function
filename = sys.argv[1]
DecodeAudio(filename)
