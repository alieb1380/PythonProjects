import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file from user
urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
loop = AudioSegment.from_wav("metallic-drums.wav")
# Play the result
play(loop)
# Repeat 2 times
loop2 = loop * 2
# Get length in milliseconds
length = len(loop2)
# Set fade time
fade_time = int(length * 0.5)
# Fade in and out
faded = loop2.fade_in(fade_time).fade_out(fade_time)

# Download another loop
urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
# Load into PyDub
beat = AudioSegment.from_wav("beat.wav")
# Mix with our original loop
mixed = beat[:length].overlay(loop2)

# Filter the beat at 3kHz
filtered = beat.low_pass_filter(3000)
# Mix loop2 with a reversed, panned version
loop = loop2.reverse().pan(-0.5).overlay(loop2.pan(0.5))
# Mix our filtered beat with the new loop at -3dB
final = filtered.overlay(loop2 - 3, loop=True)

final.export("final.mp3", format="mp3")

# Create an empty AudioSegment
result = AudioSegment.silent(duration=0)
# Loop over 0-14
for n in range(15):
    # Generate a sine tone with frequency 200 * n
    gen = sine(200 * n)
    # AudioSegment with duration 200ms, gain -3
    sine  = gen.to_audio_segment(duration=200).apply_gain(-3)
    # Fade in / out
    sine = sine.fade_in(50).fade_out(100)
    # Append the sine to our result
    result += sine
# Play the result
play(result)