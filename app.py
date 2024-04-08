#!/usr/bin/python3

import argparse

from src.extractor import EmailAttachmentExtractor


def main():
    parser = argparse.ArgumentParser(description="Extract attachments from .eml files.")
    parser.add_argument("-i", "--input", type=str, help="Directory containing .eml files")
    parser.add_argument( "-o", "--output", type=str, help="Directory to save attachments")
    args = parser.parse_args()

    extractor = EmailAttachmentExtractor(args.input, args.output)
    extractor.extract_and_save_attachments()

if __name__ == "__main__":
    main()