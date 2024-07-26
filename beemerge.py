import argparse
import glob
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Merge video frames into a picture with moving elements trajectories.')
parser.add_argument('-s', '--start_idx', type=int, default=0, help='Index of the first frame.')
parser.add_argument('-n', '--nb_frames', type=int, default=50, help='Number of frames to merge.')
parser.add_argument('-t', '--threshold', type=int, default=10, help='Threshold for frame difference detection.')
parser.add_argument('-d', '--directory', type=str, default='frames', help='Name of the directory containing frames as individual image files.')
parser.add_argument('-o', '--output', type=str, default='', help='Name of the output. Display result if not set.')
args = parser.parse_args()

img_list = glob.glob(f"{args.directory}/frame*.jpg")
img_list.sort()
nb_imgs = len(img_list)
end_idx = min(args.start_idx + args.nb_frames, nb_imgs)

first_img = True
prev_img = image.imread(img_list[args.start_idx])
result = prev_img.copy()
n = 0

for f in tqdm(img_list[args.start_idx:end_idx]):
  cur_img = image.imread(f)
  if not first_img:
    diff = np.clip(cur_img.astype(np.float32) - prev_img.astype(np.float32), 0, 255)
    diff = (np.mean(diff, 2)[:, :, np.newaxis] > args.threshold) * prev_img
    diff = (np.mean(diff - prev_diff, 2)[:, :, np.newaxis] > args.threshold) * diff
    mask = diff == 0
    result = result * mask + diff
    prev_diff = diff
    result = np.clip(result, 0, 255)
    n += 1
  else:
    first_img = False
    prev_diff = np.zeros_like(cur_img)
  prev_img = cur_img

if args.output == '':
  plt.imshow(result)
  plt.show()
else:
  plt.imsave(args.output, result)
