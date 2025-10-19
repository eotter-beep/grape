<img width="1640" height="664" alt="New Project" src="https://github.com/user-attachments/assets/80df58ef-e3ee-4fe6-b930-651ebc51da8f" />

# Grape

Grape is a audio driver for realistic audio, using 30332 audio channels, making a realistic immersion, heres how the science works

## 🎧 Why Grape Audio Driver Sounds So Realistic

The Grape Audio Driver produces audio that feels remarkably *real* to the human ear — not because of brute-force DSP, but because of how it models the way sound is **perceived**, not just **recorded**.

### 🧩 Audio2Vec Feature Embeddings
Instead of handling raw waveforms directly, Grape uses **Audio2Vec** to convert sound into semantic vector representations.  
This captures subtle characteristics like timbre, harmonic relationships, and transient behavior. When reconstructed, these embeddings produce smoother and more coherent sonic textures — closer to how real acoustic spaces sound.

### ⚛️ Quantum-Probabilistic Audio Modeling (QPAM)
At its core, Grape uses a **quantum-inspired audio scheme (QPAM)** from `quantumaudio`.  
QPAM encodes phase and amplitude information as probabilistic distributions rather than static values.  
This provides:
- **Sub-sample phase accuracy**, improving spatial detail and clarity.  
- **Perceptual noise shaping**, pushing quantization noise into inaudible regions.  
- **Dynamic micro-variations**, mimicking the natural randomness found in real-world audio.

### ⏱️ Temporal Stability via Async Streams
By leveraging `anyio`’s asynchronous memory streams, Grape maintains consistent data flow and timing coherence.  
Even small micro-jitter corrections have a big psychoacoustic effect — ensuring that transients and rhythmic content remain natural and lifelike.

### 🧠 Psychoacoustic Alignment
Every step of Grape’s pipeline aligns with human hearing characteristics:
- Natural masking curves  
- Smooth frequency roll-offs  
- Dynamic range management guided by auditory thresholds  

The result is an audio output that *feels analog*, even though it’s completely digital.


### Do this before running ⚠️⚠️

To not get package errors before running, run `python3 venv.py`

You may run it with `python driver.py`
