#!/usr/bin/env python3

import argparse
from itertools import permutations
import math
import os
import sys
import gzip
from threading import Thread

def validate_input(text):
    """Validate the input text for length and characters."""
    if len(text) > 12:
        print("Error: Input text is too long. Generating permutations for strings longer than 12 characters is resource-intensive.")
        sys.exit(1)

def generate_permutations_chunk(text, output_file, verbose, start, end):
    """Generate permutations for a chunk of indices."""
    perm = permutations(text)
    with open(output_file, "a") as file:
        for i, p in enumerate(perm):
            if start <= i < end:
                word = "".join(p)
                file.write(word + "\n")
                if verbose:
                    print(word)

def generate_permutations(text, output_file, verbose, compressed):
    """Generate all permutations and save to a file or compressed file."""
    try:
        total_permutations = math.factorial(len(text))

        # Decide on file mode based on compression
        if compressed:
            output_file += ".gz"
            with gzip.open(output_file, "wt") as file:
                perm = permutations(text)
                for p in perm:
                    word = "".join(p)
                    file.write(word + "\n")
                    if verbose:
                        print(word)
        else:
            with open(output_file, "w") as file:
                perm = permutations(text)
                for p in perm:
                    word = "".join(p)
                    file.write(word + "\n")
                    if verbose:
                        print(word)

        print(f"Wordlist saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def check_disk_space(output_file, total_permutations, text_length):
    """Check if there is enough disk space for the wordlist."""
    free_space = os.statvfs(os.path.dirname(output_file) or os.getcwd()).f_bavail * os.statvfs(os.path.dirname(output_file) or os.getcwd()).f_frsize
    estimated_size = total_permutations * (text_length + 1)  # Rough estimation of size in bytes

    if free_space < estimated_size:
        print("Error: Not enough disk space available to generate the wordlist.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate a custom wordlist with permutations of a given text.")
    parser.add_argument("-t", "--text", required=True, help="Text for generating permutations")
    parser.add_argument("-o", "--output", required=True, help="Output file to save the wordlist")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show permutations on the screen")
    parser.add_argument("-c", "--compressed", action="store_true", help="Compress the output file as .gz")
    parser.add_argument("-m", "--multithread", action="store_true", help="Enable multithreaded generation for large inputs")

    args = parser.parse_args()

    validate_input(args.text)

    total_permutations = math.factorial(len(args.text))
    check_disk_space(args.output, total_permutations, len(args.text))

    if args.multithread:
        # Multithreading setup
        num_threads = 4  # Adjust based on system capability
        chunk_size = total_permutations // num_threads
        threads = []

        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < num_threads - 1 else total_permutations
            thread = Thread(target=generate_permutations_chunk, args=(args.text, args.output, args.verbose, start, end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    else:
        generate_permutations(args.text, args.output, args.verbose, args.compressed)

if __name__ == "__main__":
    main()
