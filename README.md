# Computer-vision
open CV project repo
utils - has some useful tools for opencv projects.

## Prerequisities

1. Install required module.
   
   pip install -r requirements/development-requirements.txt
   
   pip install .


## Utils

1. `videos_to_images.py` - Converts videos into images.

	Usage:
		`video_to_images.py [-h] -i INPUT_PATH -o OUTPUT_PATH [-f] [-p PREFIX]`

		optional arguments:
		  -h, --help            show this help message and exit
		  -i INPUT_PATH, --input-path INPUT_PATH
		                        path to images dataset...
		  -o OUTPUT_PATH, --output-path OUTPUT_PATH
		                        path to store frame ...
		  -f, --filter-frame    store only the high resolution frames ...
		  -p PREFIX, --prefix PREFIX
		                        prefix for the new files ...



2. `images_to_video.py` - Converts images to video.

	Usage:
	 	`images_to_video.py [-h] -i IMAGE_FOLDER -v OUTPUT_VIDEO_NAME`
		                          [-e EXTENSION]

		optional arguments:
		  -h, --help            show this help message and exit
		  -i IMAGE_FOLDER, --image-folder IMAGE_FOLDER
		                        path to images dataset...
		  -v OUTPUT_VIDEO_NAME, --output-video-name OUTPUT_VIDEO_NAME
		                        path to images dataset...
		  -e EXTENSION, --extension EXTENSION
		                        extension needs to be considered...


