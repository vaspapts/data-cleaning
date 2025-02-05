import soundfile as sf
import json
import os

def slice_wav_segments_soundfile(wav_file, json_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Load audio file
    audio_data, sample_rate = sf.read(wav_file)
    segments_data = []

    # Process each segment
    for i, segment in enumerate(data['segments']):
        # if i==20:
        #     break
        # print("No nothing else Segment:",i," start:", segment['start']," end:", segment["end"])
        
        # print("Segment:",i," start:", int(segment['start'])," end:", int(segment["end"]))
        # Convert seconds to samples
        start_sample = int(segment['start'] * sample_rate)
        end_sample = int(segment['end'] * sample_rate)
        
        # Extract and save segment
        output_filename = f"segment_{i:04d}.wav"
        output_path = os.path.join(output_dir, output_filename)
        
        sf.write(output_path, audio_data[start_sample:end_sample], sample_rate)
        
        segment_info = {
            'audio_title': output_filename,
            'text': segment['text']
        }
        segments_data.append(segment_info)

        print(f"Exported: {output_filename}")
        print(f"Text: {segment['text']}")
        print("-" * 50)
        
    output_json_path = os.path.join(output_dir, "full_transcribe.json")
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump({'segments': segments_data}, f, ensure_ascii=False, indent=4)

# Example usage
if __name__ == "__main__":
    wav_file = "e-alithia.wav"  # Replace with your WAV file path
    json_file = "transcriptions-ealithia.json"    # Your JSON file with segments
    output_dir = "e-alithia-wavs-hf"      # Directory where egments will be saved
    
    slice_wav_segments_soundfile(wav_file, json_file, output_dir)