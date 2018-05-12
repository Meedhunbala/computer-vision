import argparse
import cv2


def make_cli_parser(args=None):
    # parse arguments
    cliparser = argparse.ArgumentParser()
    cliparser.add_argument("-i", "--input-path", required=True,
                           help="path to images dataset...")
    cliparser.add_argument("-o", "--output-path", required=True,
                           help="path to store frame ...")
    cliparser.add_argument("-f", "--filter-frame", default=False,
                           action='store_true',
                           help="store only the high resolution frames ...")
    cliparser.add_argument("-p", "--prefix", default="frame",
                           help="prefix for the new files ...")
    return cliparser


def convert_video_to_images(args):
    frame_cnt = 0
    vidcap = cv2.VideoCapture(args["input_path"])

    success, image = vidcap.read()
    success = True
    while success:
        if args['filter_frame']:
            vidcap.set(cv2.CAP_PROP_POS_MSEC, (frame_cnt * 1000))
        success, image = vidcap.read()
        output_path = "{0}/{1}-{2}.jpg".format(
            args['output_path'], args['prefix'], frame_cnt)
        cv2.imwrite(output_path, image)
        frame_cnt = frame_cnt + 1


def main():
    args = vars(make_cli_parser().parse_args())
    convert_video_to_images(args)

if __name__ == '__main__':
    main()
