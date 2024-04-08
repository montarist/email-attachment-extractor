
# Email Attachment Extractor
[![Python application test](https://github.com/montarist/email-attachment-extractor/actions/workflows/python_app_test_workflow.yml/badge.svg)](https://github.com/montarist/email-attachment-extractor/actions/workflows/python_app_test_workflow.yml)

## Overview
This tool extracts attachments from emails stored in .eml files. It is designed to be simple to use and effective at handling large batches of emails.

## Features
- Extract attachments from .eml files in a specified directory.
- Save attachments to a designated output directory.
- Handle filename conflicts by appending a counter to the existing filename.

## Prerequisites
- Python 3.8 or newer

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-attachment-extractor.git
   cd email-attachment-extractor
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the tool, execute the following command from the terminal:
```bash
./app -i <input_directory> -o <output_directory>
```
Replace `<input_directory>` and `<output_directory>` with the paths to your directories where the .eml files are stored and where you want the attachments to be saved, respectively.

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
