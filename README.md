# fft-embeddings
from the time domain to the frequency domain and back again, this time with text embeddings!

### what this repo does:
1. split a large corpus of text into overlapping segments (see `split_utils.split_text()`)
1. transpose the resulting time-domain embeddings (that is, a list of embeddings representing the sequential pieces of text) into the frequency domain with librosa's FFT implementation
1. do some signal processing in the frequency domain to, in principle, boost the signal-to-noise ratio of the embeddings (currently only lowpass filter is supported lmao)
1. transpose back to the time domain with librosa's ISTFT implementation where you can once again do all the classic embeddings-y things like semantic search, classification, etc.

### a cool visualization

spectrogram for channel 5 of openai's embeddings on the Gettysburg Address:
![spectro_5](spectro_5.png)