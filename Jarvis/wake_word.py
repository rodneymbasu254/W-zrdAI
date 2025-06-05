import pvporcupine
import pyaudio
import os

key = os.getenv("ACCESS_KEY")
def wait_for_wake_word():
    porcupine = pvporcupine.create(key, keywords=["jarvis"])
    pa = pyaudio.PyAudio()
    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )
    print("🔴 Listening for wake word...")

    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = list(porcupine._unpack_pcm(pcm))
        if porcupine.process(pcm) >= 0:
            print("🟢 Wake word detected.")
            break
