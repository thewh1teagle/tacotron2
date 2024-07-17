from pathlib import Path
import soundfile as sf
import librosa
from tqdm import tqdm

# Define paths
input_path = Path('waves')  # Path to the directory containing the wave files
output_path = Path('resampled')  # Path to save the resampled files

# Create output directory if it doesn't exist
output_path.mkdir(parents=True, exist_ok=True)

# Get list of input files
input_files = list(input_path.glob('*.wav'))

# Iterate over each file in the input directory with tqdm for progress
for input_file in tqdm(input_files, desc='Resampling', unit='file'):
    # Read audio file
    audio_data, sample_rate = librosa.load(input_file, sr=None)
    
    # Resample to 22050 Hz
    resampled_data = librosa.resample(audio_data, orig_sr=sample_rate, target_sr=22050)
    
    # Construct the output file path
    output_file = output_path / input_file.name
    
    # Save resampled audio
    sf.write(output_file, resampled_data, 22050)

print("Resampling completed!")
