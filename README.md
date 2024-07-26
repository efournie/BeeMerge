# BeeMerge

This is a simple python script merging frames of a video into a single composite image with moving elements merged.

## Prerequisites

The script uses Matplotlib, NumPy and tqdm. They can be installed either with
	pip install matplotlib tqdm numpy
or
	sudo apt install python3-matplotlib python3-numpy python3-tqdm

Video frames can be placed into any directory but they have to be named "frame-XXX.jpg" where XXX is the frame number. 
They can be generated for example with ffmpeg:
	ffmpeg -i video.mp4 frame-%03d.jpg

## Usage

	usage: beemerge.py [-h] [-s START_IDX] [-n NB_FRAMES] [-t THRESHOLD]
	                   [-d DIRECTORY] [-o OUTPUT]

	Merge video frames into a picture with moving elements trajectories.

	optional arguments:
	  -h, --help            show this help message and exit
	  -s START_IDX, --start_idx START_IDX
	                        Index of the first frame.
	  -n NB_FRAMES, --nb_frames NB_FRAMES
	                        Number of frames to merge.
	  -t THRESHOLD, --threshold THRESHOLD
	                        Threshold for frame difference detection.
	  -d DIRECTORY, --directory DIRECTORY
	                        Name of the directory containing frames as individual
	                        image files.
	  -o OUTPUT, --output OUTPUT
	                        Name of the output. Display result if not set.

## Example
	python beemerge.py --start_idx 225 --nb_frames 50 --output result.png

[Example result](result.png)
