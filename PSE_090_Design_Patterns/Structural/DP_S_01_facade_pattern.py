# Design Patterns - Facade Pattern
# -----------------------------------------------------------------------------
# The Facade Pattern is a structural design pattern that provides a simple,
# unified interface to a complex subsystem.
#
# It hides internal complexity and exposes only what the client needs.
#
# Instead of the client interacting with multiple components directly,
# the Facade acts as a single entry point.
#
# -----------------------------------------------------------------------------
# In this example:
#
# A video processing system consists of multiple subsystems:
#
# - VideoDecoder
# - AudioExtractor
# - VideoCompressor
# - FileWriter
#
# Without Facade:
# The client must coordinate all these components manually.
#
# With Facade:
# The client calls a single method: convert_video()
# -----------------------------------------------------------------------------

import time

# -----------------------------------------------------------------------------
# Subsystems
# -----------------------------------------------------------------------------


class VideoDecoder:
    def decode(self, video_file: str):
        print(f"[Decoder] Decoding video: {video_file}")
        time.sleep(1)


class AudioExtractor:
    def extract(self, video_file: str):
        print(f"[Audio] Extracting audio from: {video_file}")
        time.sleep(1)


class VideoCompressor:
    def compress(self, video_file: str):
        print(f"[Compressor] Compressing video: {video_file}")
        time.sleep(1)


class FileWriter:
    def write(self, output_file: str):
        print(f"[Writer] Saving output file: {output_file}")
        time.sleep(1)


# -----------------------------------------------------------------------------
# Facade
# -----------------------------------------------------------------------------


class VideoConversionFacade:
    """
    Facade class that hides complexity of video processing subsystem.
    """

    def __init__(self):
        self.decoder = VideoDecoder()
        self.audio = AudioExtractor()
        self.compressor = VideoCompressor()
        self.writer = FileWriter()

    def convert_video(self, input_file: str, output_file: str):
        print("\n[Facade] Starting video conversion pipeline...\n")

        self.decoder.decode(input_file)
        self.audio.extract(input_file)
        self.compressor.compress(input_file)
        self.writer.write(output_file)

        print("\n[Facade] Video conversion completed successfully!")


# -----------------------------------------------------------------------------
# Client
# -----------------------------------------------------------------------------


def main():
    facade = VideoConversionFacade()

    # Client interacts with only one simple interface
    facade.convert_video(input_file="input.mp4", output_file="output.mp4")


if __name__ == "__main__":
    main()
