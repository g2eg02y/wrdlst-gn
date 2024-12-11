# wrdlst-gn

# Wordlist Generator Tool

A simple Python-based tool to generate custom wordlists by creating permutations of a given text. Ideal for penetration testers and digital forensics enthusiasts.

## Features
- Generates all permutations of a given text.
- Saves the output to a specified file.
- Supports gzip compression for output files to save disk space.
- Optional verbose mode to display results in real time.
- Multithreading support for efficient generation on large inputs.
- Input validation to prevent resource-intensive operations for long strings.
- Disk space check to ensure sufficient storage for the generated wordlist.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/g2eg02y/wrdlst-gn.git
   cd wrdlst-gn
   ```
2. Run the setup script:
   ```bash
   sudo ./setup.sh
   ```

## Usage
```bash
wrdlst-gn -t <text> -o <output_file> [-v] [-c] [-m]
```

### Options
- `-t`, `--text`: Text for generating permutations (required).
- `-o`, `--output`: Output file to save the wordlist (required).
- `-v`, `--verbose`: Display generated permutations in real time (optional).
- `-c`, `--compressed`: Save the output file as a compressed `.gz` file (optional).
- `-m`, `--multithread`: Enable multithreaded generation for large inputs (optional).

### Examples
1. Generate permutations and save them to `wordlist.txt`:
   ```bash
   wrdlst-gn -t text -o wordlist.txt
   ```
2. Generate permutations with verbose output:
   ```bash
   wrdlst-gn -t text -o wordlist.txt -v
   ```
3. Generate permutations and save the output as a compressed file:
   ```bash
   wrdlst-gn -t text -o wordlist.txt -c
   ```
4. Generate permutations using multithreading:
   ```bash
   wrdlst-gn -t text -o wordlist.txt -m
   ```

## Notes
- **Performance**: Generating permutations can be resource-intensive for long strings. The tool limits input to 12 characters to avoid overwhelming system resources.
- **Disk Space**: Ensure enough disk space is available for the generated wordlist. The tool estimates required space before generation.
- **Compression**: Use the `--compressed` flag to save space by compressing the output file.

## Contributing
Feel free to fork this repository and submit pull requests.