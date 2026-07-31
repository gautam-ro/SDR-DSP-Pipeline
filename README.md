# SDR Signal Processing & Spectral Analysis Pipeline

A Python-based digital signal processing (DSP) pipeline designed to process real-time and simulated In-Phase/Quadrature (IQ) radio frequency (RF) signals. The project implements windowing, Short-Time Fourier Transform (STFT), and Power Spectral Density (PSD) estimation to perform spectral analysis and signal detection.

---

##  Key Features

* **IQ Signal Generation & Acquisition:** Simulates continuous complex IQ streams with customizable carrier frequencies, bandwidths, and additive white Gaussian noise (AWGN).
* **STFT Spectral Analysis:** Implements Short-Time Fourier Transforms using `SciPy` to analyze time-varying frequency content.
* **Windowing & Leakage Reduction:** Applies Hann/Hamming windowing functions prior to FFT execution to suppress spectral leakage.
* **Power Spectral Density (PSD):** Converts raw complex FFT magnitudes into decibels for dynamic range visualization.
* **Real-Time Visualization:** Generates real-time spectrogram (waterfall) plots using `Matplotlib`.

---

##  Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:** `NumPy`, `SciPy`, `Matplotlib`

---

## 🛠️ Project Structure

```text
sdr-dsp-pipeline/
├── dsp_pipeline.py      # Core DSP logic (IQ generation, STFT, plotting)
├── spectrogram.png      # Sample output visualization
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
