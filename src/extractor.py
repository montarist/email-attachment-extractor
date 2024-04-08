import os
from email import policy
from email.parser import BytesParser
from pathlib import Path


class EmailAttachmentExtractor:
    """
    A class to extract attachments from .eml files stored in a specified directory.

    Attributes:
        input_directory (Path): The directory where .eml files are stored.
        output_directory (Path): The directory where attachments will be saved.
    """

    def __init__(self, input_dir, output_dir):
        """
        Initializes the EmailAttachmentExtractor with specified input and output directories.

        Args:
            input_dir (str): The path to the directory containing .eml files.
            output_dir (str): The path to the directory where attachments should be saved.
        """
        self.input_directory = Path(input_dir)
        self.output_directory = Path(output_dir)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def extract_and_save_attachments(self):
        """
        Processes all .eml files in the input directory to extract and save attachments.
        """
        for eml_file in self.input_directory.glob('*.eml'):
            self._save_attachments_from_eml(eml_file)
            print(f"Processed {eml_file}")

    def _save_attachments_from_eml(self, file_path):
        """
        Extracts and saves attachments from a single .eml file.

        Args:
            file_path (Path): The path to the .eml file to process.
        """
        with open(file_path, 'rb') as file:
            msg = BytesParser(policy=policy.default).parse(file)

        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                filename = part.get_filename()
                if filename:
                    file_path = self.output_directory / filename
                    if file_path.exists():
                        file_path = self._resolve_filename_conflict(file_path)
                    with open(file_path, 'wb') as f:
                        f.write(part.get_payload(decode=True))
                    print(f"Saved {filename} to {file_path}")

    def _resolve_filename_conflict(self, existing_path):
        """
        Resolves filename conflicts by appending a counter to the filename.

        Args:
            existing_path (Path): The path where a filename conflict occurred.

        Returns:
            Path: A new file path with a counter appended to ensure uniqueness.
        """
        base, extension = os.path.splitext(existing_path.name)
        counter = 1
        while existing_path.exists():
            new_filename = f"{base}_{counter}{extension}"
            existing_path = existing_path.parent / new_filename
            counter += 1
        return existing_path
