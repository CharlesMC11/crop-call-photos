"""
An automation utility for image preprocessing. It leverages OpenCV-Python and NumPy to isolate active video call windows
and remove surrounding black borders, seamlessly preserving metadata with ExifTool.
"""

from argparse import ArgumentParser
from pathlib import Path

from crop_call_photos import main

if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory", type=Path, help="directory containing images to crop"
    )
    args = parser.parse_args()

    main(args.directory)
