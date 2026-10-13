# crop-call-photos

An automation utility for image pre­processing. It leverages OpenCV‐Python and NumPy to isolate active video call windows
and remove surrounding black borders, seamlessly preserving metadata with ExifTool.

## Motivation

A companion utility to [sst](https://github.com/CharlesMC11/sst.git), born from the need to automatically strip away the
heavy black letterboxing that accom­panies screen­shots of video calls with my girlfriend, after they have gone through
the metadata tagging pipeline.

## Architecture & Performance

Designed for efficiency, it utilizes:

- **OpenCV & NumPy**: For contour detec­tion, binarization thresholding, and bounding box extraction to
  isolate target video frames.
- **ExifTool**: Subprocess for metadata pre­servation, copying original creation tags directly onto the cropped
  output.
- **Atomic Operations**: Safe file replace­ments and low overhead, compressed tarball archiving (`originals.tar.gz`,
  `compresslevel=1`) to preserve raw captures without disk clutter.

*Note: Non‐black objects surrounding the black border (such as active GUI windows) require pre‐cropping.*
