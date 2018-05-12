import argparse
import cv2
import os
import natsort


def make_cli_parser(args=None):
    # parse arguments
    cliparser = argparse.ArgumentParser()
    cliparser.add_argument("-i", "--image-folder", required=True,
                           help="path to images dataset...")
    cliparser.add_argument("-v", "--output-video-name", required=True,
                           help="path to images dataset...")
    cliparser.add_argument("-e", "--extension", default=".jpg",
                           help="extension needs to be considered...")
    return cliparser


def get_images_from_folder(image_folder):
    return [img for img in os.listdir(image_folder) if img.endswith(".jpg")]


def convert_images_to_video(args):
    image_folder = args['image_folder']
    images = get_images_from_folder(image_folder)
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(args['output_video_name'], -1, 1, (width, height))

    for image in natsort.natsorted(images):
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()


def main():
    args = vars(make_cli_parser().parse_args())
    convert_images_to_video(args)

if __name__ == '__main__':
    main()
