from huggingface_hub import HfApi, create_repo
import os
import env_vars


from datasets import Dataset, Audio
import json
import os

def create_and_push_dataset(wav_dir, json_file, hf_repo_name, token):
    # Load the transcription JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Prepare the dataset dictionary
    dataset_dict = {
        'audio': [],
        'text': []
    }
    
    # Collect data
    for segment in data['segments']:
        audio_path = os.path.join(wav_dir, segment['audio_title'])
        if os.path.exists(audio_path):
            dataset_dict['audio'].append(audio_path)
            dataset_dict['text'].append(segment['text'])
    
    # Create the dataset
    dataset = Dataset.from_dict(dataset_dict)
    
    # Cast the audio column to Audio feature
    dataset = dataset.cast_column('audio', Audio())
    
    # Push to hub
    dataset.push_to_hub(
        hf_repo_name,
        token=token,
        private=True  # Set to False for public dataset
    )

if __name__ == "__main__":
    wav_dir = "e-alithia-wavs-hf"
    json_file = "e-alithia-wavs-hf/full_transcribe.json"
    repo_name = "vasil-papage/alithia-split"
    token = "HF_TOKEN"
    
    create_and_push_dataset(wav_dir, json_file, repo_name, token)
