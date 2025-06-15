"""
Module: log_analyzer
This script reads and analyzes a log file, counting log entries by their levels 
(INFO, DEBUG, ERROR, WARNING). Optionally, it can filter and display all entries 
of a specified log level.
Usage:
To get general log statistics:
`python log_analyzer.py <path_to_log_file.log>`

To get statistics and detailed logs for a specific level (e.g., ERROR):
`python log_analyzer.py <path_to_log_file.log> error`
"""
import sys
import collections

def parse_log_line(line: str) -> dict:
    """
    Parses a single log line into its components: date, time, level, and message.
    Args:
        line (str): A single log entry string.
    Returns:
        dict: A dictionary containing the parsed components 
        with keys 'date', 'time', 'level', 'message'.
              Returns an empty dictionary for malformed lines.
    """
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}

    date, time, level, message = parts
    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message.strip()
    }

def load_logs(file_path: str) -> list:
    """
    Loads log entries from a specified file, parsing each line.
    Args:
        file_path (str): The path to the log file.
    Returns:
        list: A list of dictionaries, where each dictionary represents a parsed log entry.
              Returns an empty list if the file cannot be read or is empty.
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_entry = parse_log_line(line)
                if parsed_entry:
                    logs.append(parsed_entry)
    except FileNotFoundError:
        print(f"Error: Log file not found at '{file_path}'")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters a list of log entries by a specific log level.
    Args:
        logs (list): A list of parsed log dictionaries.
        level (str): The log level to filter by (e.g., 'INFO', 'ERROR').
    Returns:
        list: A new list containing only log entries that match the specified level.
    """
    target_level = level.upper()
    return [log for log in logs if log.get('level') == target_level]

def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of log entries for each log level.
    Args:
        logs (list): A list of parsed log dictionaries.
    Returns:
        dict: A dictionary where keys are log levels (str) and values are their counts (int).
    """
    levels = [log['level'] for log in logs if 'level' in log]
    return dict(collections.Counter(levels))

def display_log_counts(counts: dict) -> None:
    """
    Displays the counts of log entries per level in a formatted table.
    Args:
        counts (dict): A dictionary with log levels as keys and their counts as values.
    """
    print("Level            | Count")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<16} | {counts[level]:<9}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_log_file> [log_level]")
        sys.exit(1)

    script_file_path = sys.argv[1]
    filter_level = sys.argv[2] if len(sys.argv) > 2 else None

    all_logs = load_logs(script_file_path)
    log_counts = count_logs_by_level(all_logs)
    display_log_counts(log_counts)

    if filter_level:
        print(f"\nDetails for log level '{filter_level.upper()}':")
        detailed_logs = filter_logs_by_level(all_logs, filter_level)
        if detailed_logs:
            for entry in detailed_logs:
                print(f"{entry['date']} {entry['time']} - {entry['message']}")
        else:
            print(f"No logs found for level '{filter_level.upper()}'.")
