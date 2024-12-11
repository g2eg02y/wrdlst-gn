#!/usr/bin/env python3

import argparse
from itertools import permutations
import sys

def generate_permutations(text, output_file, verbose):
    try:
        # Generate all permutations
        perm = permutations(text)
        with open(output_file, "w") as file:
            for p in perm:
                word = "".join(p)
                file.write(word + "\n")
                if verbose:
                    print(word)
        print(f"Wordlist saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Generate a custom wordlist with permutations of a given text.")
    parser.add_argument("-t", "--text", required=True, help="Text for generating permutations")
    parser.add_argument("-o", "--output", required=True, help="Output file to save the wordlist")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show permutations on the screen")

    args = parser.parse_args()
    generate_permutations(args.text, args.output, args.verbose)

if __name__ == "__main__":
    main()
