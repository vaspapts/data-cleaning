from find_dots_on_text_file import process_text_file
from remove_segmentsby_id import remove_segments_by_ids


if __name__ == "__main__":
    input_file = "data/the-end.txt"    # Replace with your input filename
    output_file = "data/the-end-output.txt"  # Replace with your desired output filename
    output_json = "data/the-end-output.json"

    try:
        danger_count, comma_count, total_count, danger_percent, comma_percent, clean_percent, problem_lines, comma_lines = process_text_file(input_file, output_file, output_json)
        print("\nFile processing completed successfully!")
        print(f"Total number of lines: {total_count}")
        print(f"Lines ending with commas: {comma_count} ({comma_percent:.2f}% of total lines)")
        print(f"Lines with other issues: {danger_count} ({danger_percent:.2f}% of total lines)")
        print(f"Clean lines: {total_count - danger_count - comma_count} ({clean_percent:.2f}% of total lines)")
        print(f"\nProblem line numbers have been saved to {output_json}")
    except Exception as e:
        print(f"An error occurred: {e}")