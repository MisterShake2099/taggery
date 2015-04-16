This script creates new filenames for music files based on tag information.
It currently does this by copying the original file with a new name. The
ability to then delete the original file (simulating an overwrite) will be
added at a later date.

@title: taggery
@author: MisterShake2099

Command line arguments:
@src: a relative or absolute filepath containing source audio files.
@dst: a relative or absolute filepath to put processed audio files.
@mode: an optional argument specifying which mode to use.
        Modes are 'copy' and 'overwrite'.
