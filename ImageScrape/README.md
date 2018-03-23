## Google Image Downloader

Python script for downloading images from Google Image Search. Can be used to download images for machine learning training, or for any other image scraping need.

### Usage
Typical usage would be:

`python imageScrape.py -s "rainbow" -n 10000 --square --resize`

This downloads 10,000 square rainbow images, which have been resized to 200 x 200 pixels.

By default it will only download 10 jpg formatted images, and will not resize or download square images only. If you want to allow multiple image formats use `--all_types`.

	-s SEARCH		text for search query
    -n NUM_IMAGES           number of images to save
    --square                download only square images
	--resize              	resize images (defaults to 200 x 200)
	--width WIDTH           width to resize to
	--height HEIGHT         height to resize to
	--all_types             download multiple image types as available

### Requirements

- Python 2
- Requires Chrome Driver: [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/)
	- Download and copy path location to imageScrape.py line 43: `driver = webdriver.Chrome(<PATH TO CHROMEDRIVER HERE>)`
- selenium `conda install selenium` (if using conda)

Based on [https://github.com/atif93/google_image_downloader](https://github.com/atif93/google_image_downloader)
