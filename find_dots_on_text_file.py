import json

def process_text_file(input_filename, output_filename, output_json):
    """ 
    Keep only lines that end with: . ? !  
    Mark with [DANGER] the broken lines
    Mark with [COMMA] the lines that end with comma
    """
    # Initialize counters
    total_lines = 0
    danger_lines = 0
    comma_lines = 0
    danger_lines_id = []
    lines_with_comma_id = []
    
    # Define valid ending punctuation
    valid_endings = ['.', '!', '?']
    
    # Open files with UTF-8 encoding
    with open(input_filename, 'r', encoding='utf-8') as input_file, \
         open(output_filename, 'w', encoding='utf-8') as output_file:
        # Read the file line by line
        for line in input_file:
            # Remove trailing whitespace
            stripped_line = line.rstrip()
            
            # Check if line ends with valid punctuation
            if any(stripped_line.endswith(end) for end in valid_endings):
                # If valid ending, write the original line
                output_file.write(line)
            elif stripped_line.endswith(','):
                # If ends with comma, add [COMMA]
                output_file.write(stripped_line + "[COMMA]\n")
                comma_lines += 1
                lines_with_comma_id.append(total_lines)
            else:
                # For all other cases, add [DANGER]
                output_file.write(stripped_line + "[DANGER]\n")
                danger_lines += 1
                danger_lines_id.append(total_lines)
            
            # count lines
            total_lines += 1
            
    # Create dictionary for JSON
    output_data = {
        "danger_lines": danger_lines_id,
        "lines_with_comma_id": lines_with_comma_id
        
    }

    # Write to JSON file
    with open(output_json, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
    
    # Calculate percentages
    danger_percentage = (danger_lines / total_lines) * 100 if total_lines > 0 else 0
    comma_percentage = (comma_lines / total_lines) * 100 if total_lines > 0 else 0
    clean_lines_percentage = ((total_lines - danger_lines - comma_lines) / total_lines) * 100 if total_lines > 0 else 0
        
    return danger_lines, comma_lines, total_lines, danger_percentage, comma_percentage, clean_lines_percentage, danger_lines_id, lines_with_comma_id
