import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import soundfile as sf

# ───── Load WAV file ─────
filename = "detuned.wav"  # change this to your WAV file
data, sr = sf.read(filename, dtype='float32')
if data.ndim > 1:
    data = data.mean(axis=1)  # stereo → mono

print(f"Loaded {filename} | Samples: {len(data)} | Sample rate: {sr}")

# ───── FFT Analysis ─────
windowed = data * np.hanning(len(data))
mag = np.abs(np.fft.rfft(windowed))
freqs = np.fft.rfftfreq(len(windowed), d=1/sr)

df = pd.DataFrame({
    "frequency": freqs,
    "magnitude": mag
})
df = df[df["frequency"] < 1000]  # focus on guitar range

# ───── Guitar string reference notes ─────
GUITAR_NOTES = [
    ("E2", 82.41),
    ("A2", 110.00),
    ("D3", 146.83),
    ("G3", 196.00),
    ("B3", 246.94),
    ("E4", 329.63)
]

def find_closest_guitar_note(freq):
    min_diff = float('inf')
    closest = None
    for note, note_freq in GUITAR_NOTES:
        diff = abs(freq - note_freq)
        if diff < min_diff:
            min_diff = diff
            cents_off = 1200 * np.log2(freq / note_freq)
            closest = {
                "note": note,
                "note_freq": note_freq,
                "cents_off": cents_off
            }
    return closest

# ───── Plot spectrum ─────
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 5))
sns.lineplot(data=df, x="frequency", y="magnitude", label="Spectrum")
plt.title("Guitar Tuning: Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 400)

# Add vertical lines for standard guitar string frequencies
for note, freq in GUITAR_NOTES:
    plt.axvline(freq, color='gray', linestyle='--', linewidth=1, alpha=0.8)
    plt.text(freq, plt.ylim()[1]*0.8, note,
             rotation=90, fontsize=8, ha='center', va='bottom', color='gray')

plt.legend()
plt.tight_layout()
plt.savefig("spectrum_plot.png", dpi=150)
print("📊 Saved plot as spectrum_plot.png")

# ───── Compute tuning table ─────
N = 8  # top N frequency peaks
top_peaks = df.sort_values("magnitude", ascending=False).head(N)

results = []
for _, row in top_peaks.iterrows():
    freq = row["frequency"]
    mag = row["magnitude"]
    match = find_closest_guitar_note(freq)
    results.append({
        "Peak Frequency (Hz)": round(freq, 2),
        "Magnitude": round(mag, 1),
        "Closest Guitar Note": match['note'],
        "Note Frequency (Hz)": round(match['note_freq'], 2),
        "Cents Off": round(match['cents_off'], 2)
    })

results_df = pd.DataFrame(results)
print("\n🎯 Tuning Analysis (Guitar Strings Only):")
print(results_df.to_string(index=False))
