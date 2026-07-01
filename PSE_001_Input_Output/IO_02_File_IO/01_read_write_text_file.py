# IO - Read and Write Text Files
# -----------------------------------------------------------------------------
# File IO is used when a program needs to save data to disk or read existing
# data from disk.
#
# Common text-file operations:
#
# - Write text to a file
# - Read the whole file
# - Read the file line by line
#
# This example uses a temporary directory so running it does not create extra
# files in the repository.
# -----------------------------------------------------------------------------

from pathlib import Path
from tempfile import TemporaryDirectory


def main():
    with TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "notes.txt"

        # Write text to a file.
        file_path.write_text(
            "Python IO\n"
            "Read files\n"
            "Write files\n",
            encoding="utf-8",
        )

        # Read the whole file as one string.
        content = file_path.read_text(encoding="utf-8")

        print("===== Full Content =====")
        print(content)

        # Read the file line by line.
        print("===== Lines =====")
        lines = file_path.read_text(encoding="utf-8").splitlines()

        for line_number, line in enumerate(lines, start=1):
            print(f"{line_number}: {line}")


if __name__ == "__main__":
    main()
