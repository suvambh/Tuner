# 🎧 Audio Frequency Analysis — Tutorial & Setup Guide

This project helps you analyze audio using Python by extracting frequency components from a signal using the Fast Fourier Transform (FFT). It also includes a setup script for easy environment management.

---

## 🔧 Project Setup

Use the `install_scripts.sh` script to set up your Python environment.

### 🔍 What `create_myvnv.sh` Does

The `create_myvnv.sh` script automates the setup of a Python virtual environment for your project. Specifically, it:

- ✅ Creates a virtual environment (default name: `venv`, or a custom name you pass as an argument)
- ⚙️ Activates the environment
- 📦 Installs dependencies listed in `requirements.txt` (if the file exists)

This helps ensure a consistent setup across different machines and team members.

---

To create and use a Python virtual environment, follow these steps. But keep in mind that the script does this automatically for us here:

First, ensure Python is installed. You can check by running `python3 --version` or `python --version`.

Navigate to your project folder using the terminal.

To create a virtual environment, use the following command:

`python3 -m venv venv`

This creates a folder called `venv` that contains an isolated Python installation.

To activate the environment:

* On **macOS/Linux**, run:
  `source venv/bin/activate`

* On **Windows**, run:
  `venv\Scripts\activate`

After activation, your terminal prompt will show the environment name (usually `(venv)`), indicating that you're now working inside the virtual environment. 

While activated, any Python packages you install using pip will only be available inside this environment.

To install packages, use:

`pip install package-name`

To freeze the installed packages into a file:

`pip freeze > requirements.txt`

To deactivate the environment when you're done working:

`deactivate`

This returns your terminal to the system’s default Python environment.

Summary of commands:

1. `python3 --version`
2. `cd your-project-folder`
3. `python3 -m venv venv`
4. `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
5. `pip install package-name`
6. `pip freeze > requirements.txt`
7. `deactivate`


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
