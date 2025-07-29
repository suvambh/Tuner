# 🎧 Audio Frequency Analysis — Tutorial & Setup Guide

This project helps you analyze audio using Python by extracting frequency components from a signal using the Fast Fourier Transform (FFT). It also includes a setup script for easy environment management.

---

## 🔧 Project Setup

Use the `install_scripts.sh` script to set up your Python environment.

### 🔍 What `create_myvnv.sh` Does

The `install_scripts.sh` script automates the setup of a Python virtual environment for your project. Specifically, it:

- ✅ Creates a virtual environment (default name: `venv`, or a custom name you pass as an argument)
- ⚙️ Activates the environment
- 📦 Installs dependencies listed in `requirements.txt` (if the file exists)
- 📄 Freezes and saves exact package versions to `locked_requirements.txt` inside the virtual environment for reproducibility

This helps ensure a consistent setup across different machines and team members.

---

## 🔬 Code Breakdown

### `windowed = data * np.hanning(len(data))`

Applies a Hann window to the signal to reduce spectral leakage before performing the FFT.

---

### `mag = np.abs(np.fft.rfft(windowed))`

Computes the magnitude spectrum of the real-valued FFT result.

---

### `freqs = np.fft.rfftfreq(len(windowed), d=1/sr)`

Generates the frequency axis corresponding to each FFT bin.

---

## 📊 Summary

| Variable   | Meaning                                         |
| ---------- | ----------------------------------------------- |
| `windowed` | Smoothed audio waveform                         |
| `mag`      | Strength of each frequency component            |
| `freqs`    | Actual frequencies in Hz (e.g., 82.4 Hz for E2) |

---

## 🚀 Example: Visualize the Spectrum

```python
import matplotlib.pyplot as plt

plt.plot(freqs, mag)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum")
plt.show()
