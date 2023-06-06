from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
GIRL: What's going on? [gasps] Are you going to invent AI and destroy humanity? [gasps] Oh no. We're so screwed."
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("out.wav", SAMPLE_RATE, audio_array)
  
# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)