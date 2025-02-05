def process_text_file(input_filename, output_filename):
    # Initialize counters
    total_lines = 0
    nodot_lines = 0
    comma_lines = 0
    
    # Open files with UTF-8 encoding
    with open(input_filename, 'r', encoding='utf-8') as input_file, \
         open(output_filename, 'w', encoding='utf-8') as output_file:
        # Read the file line by line
        for line in input_file:
            total_lines += 1
            # Remove trailing whitespace
            stripped_line = line.rstrip()
            
            # Check if the line ends with a period
            if not stripped_line.endswith('.'):
                # No dot found, now check for comma
                if not stripped_line.endswith(','):
                    output_file.write(stripped_line + "[COMMA]\n")
                    comma_lines += 1
                else:
                    output_file.write(stripped_line + "[NODOT]\n")
                nodot_lines += 1
            else:
                # If period exists, write the original line
                output_file.write(line)
    
    # Calculate percentages
    nodot_percentage = (nodot_lines / total_lines) * 100 if total_lines > 0 else 0
    comma_percentage = (comma_lines / total_lines) * 100 if total_lines > 0 else 0
    clean_lines_percentage = ((total_lines - nodot_lines - comma_lines) / total_lines) * 100 if total_lines > 0 else 0
    
    return nodot_lines, comma_lines, total_lines, nodot_percentage, comma_percentage, clean_lines_percentage

# Example usage
if __name__ == "__main__":
    input_file = "the-end.txt"    # Replace with your input filename
    output_file = "the-end-output.txt"  # Replace with your desired output filename

    try:
        nodot_count, comma_count, total_count, nodot_percent, comma_percent, clean_lines_percentage = process_text_file(input_file, output_file)
        print("\nFile processing completed successfully!")
        print(f"Total number of lines: {total_count}")
        print(f"Lines without dots: {nodot_count} ({nodot_percent:.2f}% of total lines)")
        print(f"Lines with commas: {comma_count} ({comma_percent:.2f}% of total lines)")
        print(f"Clean lines: {total_count - nodot_count - comma_count} ({clean_lines_percentage:.2f}% of total lines)")
    except Exception as e:
        print(f"An error occurred: {e}")