#!/usr/bin/python

# This script creates new filenames for music files based on tag information.
# It currently does this by copying the original file with a new name. The
# ability to then delete the original file (simulating an overwrite) will be
# added at a later date.

# @title: taggery
# @author: MisterShake2099

# Command line arguments:
# @src: a relative or absolute filepath containing source audio files.
# @dst: a relative or absolute filepath to put processed audio files.
# @mode: an optional argument specifying which mode to use.
# Modes are 'copy' and 'overwrite'.

import argparse

from mutagen.flac import FLAC
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.ogg import OGG
from mutagen.mp4 import MP4

# Receive and parse invocation.
parser = argparse.ArgumentParser(description="parsing the input")
parser.add_argument(
    "src",
    help="filepath to source directory")
parser.add_argument(
    "dst",
    default="./destination",
    help="filepath to destination directory (used only in copy mode)")
parser.add_argument(
    "--mode",
    choices=["copy", "overwrite"],
    default="copy",
    help="Select a mode. Defaults to copy.")
args = parser.parse_args()

print("Running '{}'".format(__file__))

print(args.src)
print(args.dst)
print(args.mode)


fields = args.src


def taggery():

    for file in fields:
        if file is FLAC:
            audio = FLAC("example.flac")
        if file is ID3:
            audio = ID3("example.mp3")
        if file is MP3:
            audio = MP3("example.mp3")
        if file is MP4:
            audio = MP4("example.mp4")
        if file is OGG:
            audio = OGG("example.ogg")

    print(audio)

    # create copy of each file and use stored fields to name file

    # copyfile(args.src, args.dst)
