import pytest
from pathlib import Path
from src.extractor import EmailAttachmentExtractor
from unittest.mock import patch, mock_open

# Sample content of a basic .eml file with a textual attachment encoded in base64
sample_eml_content = """From: sender@example.com
To: recipient@example.com
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="sep"

--sep
Content-Type: text/plain

This is the body of the email.
--sep
Content-Type: application/octet-stream; name="sample.txt"
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="sample.txt"

U2FtcGxlIHRleHQgaW5zaWRlIHRoZSBmaWxlLg==
--sep--
"""


def test_attachment_extraction(tmp_path):
    # Setup a dummy .eml file
    eml_path = tmp_path / "test.eml"
    eml_path.write_text(sample_eml_content)

    # Execute extraction
    extractor = EmailAttachmentExtractor(str(tmp_path), str(tmp_path))
    extractor.extract_and_save_attachments()

    # Verify the attachment was saved
    assert (tmp_path / "sample.txt").exists()


def test_filename_conflict_resolution(tmp_path):
    # Prepare mock existing file
    existing_file = tmp_path / "sample.txt"
    existing_file.touch()  # Create an empty file to simulate conflict

    # Write the .eml file
    eml_path = tmp_path / "test.eml"
    eml_path.write_text(sample_eml_content)

    # Execute extraction
    extractor = EmailAttachmentExtractor(str(tmp_path), str(tmp_path))
    extractor.extract_and_save_attachments()

    # Verify a new file with a counter is created
    assert (tmp_path / "sample_1.txt").exists()


@pytest.mark.parametrize("corrupt_content", [
    "Content-Type: text/plain\n\nThis is incomplete.",
    ""
])
def test_handling_corrupt_files(tmp_path, corrupt_content):
    # Setup a corrupt .eml file
    eml_path = tmp_path / "corrupt.eml"
    eml_path.write_text(corrupt_content)

    # Execute extraction
    extractor = EmailAttachmentExtractor(str(tmp_path), str(tmp_path))
    extractor.extract_and_save_attachments()

    # Check that no new files were created
    assert list(tmp_path.iterdir()) == [eml_path]  # Only the corrupt file should exist
