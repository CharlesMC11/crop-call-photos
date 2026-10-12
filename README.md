# crop-call-photos

An automation utility for image preprocessing. It leverages OpenCV-Python and NumPy to isolate active video call windows
and remove surrounding black borders, seamlessly preserving metadata with ExifTool.

## Motivation

A companion utility to [sst](https://github.com/CharlesMC11/sst.git), born from the need to automatically strip away the
heavy black letterboxing that accompanies screenshots of video calls with my girlfriend, after they have gone through
the metadata tagging pipeline.

## Architecture & Performance

Designed for efficiency, it utilizes:

- **OpenCV & NumPy**: For contour detection, binarization thresholding, and bounding box extraction to
  isolate target video frames.
- **ExifTool**: Subprocess for metadata preservation, copying original creation tags directly onto the cropped
  output.
- **Atomic Operations**: Safe file replacements and low-overhead compressed tarball archiving (`originals.tar.gz`,
  `compresslevel=1`) to preserve raw captures without disk clutter.

*Note: Non-black objects surrounding the black border (such as active GUI windows) require pre-cropping.*
