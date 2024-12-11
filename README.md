# wrdlst-gn

# Wordlist Generator Tool

A simple Python-based tool to generate custom wordlists by creating permutations of a given text. Ideal for penetration testers and digital forensics enthusiasts.

## Features
- Generates all permutations of a given text.
- Saves the output to a specified file.
- Optional verbose mode to display results in real time.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/g2eg02y/wrdlst-gn.git
   cd wordlist-gen
   ```
2. Run the setup script:
   ```bash
   sudo ./setup.sh
   ```

## Usage
```bash
wordlist-gen -t <text> -o <output_file> [-v]
```

### Example
1. Generate permutations and save them to `wordlist.txt`:
   ```bash
   wordlist-gen -t text -o wordlist.txt
   ```
2. Generate permutations with verbose output:
   ```bash
   wordlist-gen -t text -o wordlist.txt -v
   ```

## Notes
- **Performance**: Generating permutations can be resource-intensive for long strings.
- **Output File**: Ensure enough disk space for large wordlists.

## Contributing
Feel free to fork this repository and submit pull requests.
