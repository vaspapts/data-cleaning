import json

def extract_and_save_transcript_segments(input_json, output_json):
    with open(input_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    segments_data = []
    segment_id = 0
    
    # Navigate to initialSegments
    initial_segments = data['segments']
    end = initial_segments[0]['start']/2
    
    for i in range(len(initial_segments)-1):
        if i==20:
            break
        
        start = end
        end =   initial_segments[i]['end'] + (initial_segments[i+1]['start'] - initial_segments[i]['end'])/2
        segment_info = {
            'id': segment_id,
            'start': start,
            'end': end,
            'text': initial_segments[i]['text']
        }
        segments_data.append(segment_info)
        segment_id += 1
    
    # Save to new JSON file
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({'segments': segments_data}, f, ensure_ascii=False, indent=4)
    
    return segments_data

# Example usage
if __name__ == "__main__":
    segments = extract_and_save_transcript_segments('e-alithia.json', 'transcriptions-ealithia-2.json')
    
    # Print the extracted data to verify
    for segment in segments:
        print(f"Start: {segment['start']}")
        print(f"End: {segment['end']}")
        print(f"Text: {segment['text']}")
        print("-" * 50)