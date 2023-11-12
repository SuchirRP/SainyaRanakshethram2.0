#Submission for ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING

#Features:
    1. Transcribes audio files to text after removing any noise present in the recording.
    2. Supported formats .wav, .mp3, .flak.
    3. Uses the facebook research denoiser to clean the audio file. [https://github.com/facebookresearch/denoiser]
    4. Uses the "pydub" python library to transcribe the cleaned audio to text. [https://github.com/jiaaro/pydub]

#Dependencies:
    1. Linux debian based environoment preferably Ubuntu with Python version 3.10 minimum
    2. speech recognition library: [https://pypi.org/project/SpeechRecognition/]
        $pip install SpeechRecognition
    3. pydub library: [https://pypi.org/project/pydub/]
        $pip install pydub
    4. facebook denoiser: [https://github.com/facebookresearch/denoiser]
        $pip install denoiser
    5. ffmpeg and ffplay or libav and avplay
        $sudo apt-get install ffmpeg libavcodec-extra

#Running the Program:
The path+name of the audio file to be transcibed must be given as an argument while running the program,
Format: $python SuchirPunuru_SainyaRanakshetram2_AI.py path/filename.wav
Example: $python SuchirPunuru_SainyaRanakshetram2_AI.py data/221001_2111.mp3
