import os

from PIL import Image


def numfiles(directory):
    """Counts the number of files in a directory

    Args:
        directory (string): Path to directory

    Returns: (int): The number of files in the directory
    """
    return sum(
        1
        for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f)) and f[0] != "."
    )


def get_file_paths(directory):
    """Returns a list of all file pages from a given directory

    Args:
        directory (string): The path of the directory containing the files

    Returns:
        list: of all file paths
    """
    return [
        os.path.join(directory, filename)
        for filename in os.listdir(directory)
        if filename.endswith(".png") or filename.endswith(".jpg")
    ]


def get_max_image_size(directory):
    """Returns the max image size from a directory of images.

    Args:
        directory (string): the path of the directory containing images.

    Returns:
        tuple: of the max image size, E.G: (100, 200)
    """
    file_paths = [
        os.path.join(directory, filename)
        for filename in os.listdir(directory)
        if filename.endswith(".png") or filename.endswith(".jpg")
    ]

    # Get the largest image size
    sizes = [Image.open(f, "r").size for f in file_paths]
    return max(sizes)


def resize_images(
    directory_of_original_images,
    output_directory,
    individual_image_resize_offset,
    resize_image_canvas_colour,
    custom_dimention=None,
):
    """Takes all the images from a directory and saves them as uniformed
    resized images. All the images need to be the same square size to
    fit in a large grid together.

    Args:
        directory_of_original_images (string): The path to the directory
            containing the original images.
        output_directory (string): The path to save the resized images in.
        custom_dimesions (tuple): Force the resized image to match a custom
            dimension, E.G. 350 for a 350x350 image resize,
        resize_image_canvas_colour (tuple): The background colour of the
            resized image
    """
    file_paths = [
        os.path.join(directory_of_original_images, filename)
        for filename in os.listdir(directory_of_original_images)
        if filename.endswith(".png") or filename.endswith(".jpg")
    ]

    # Get the largest image size
    max_img_h = (
        custom_dimention or get_max_image_size(directory_of_original_images)[1]
    )

    for i in file_paths:
        # Each book image will be placed on a canvas of the max size.
        # so resave each image onto a new image with the new size
        img = Image.open(i, "r")
        img_w, img_h = img.size
        filename = img.filename.split("/")[-1]
        # use largest height to make the canvas square
        background = Image.new(
            "RGB", (max_img_h, max_img_h), resize_image_canvas_colour
        )
        bg_w, bg_h = background.size
        if individual_image_resize_offset:
            off_x, off_y = individual_image_resize_offset
            offset = ((bg_w - img_w) // off_x, (bg_h - img_h) // off_y)
            background.paste(img, offset)
        else:
            background.paste(img)
        background.save(f"{output_directory}/{filename}")


def calculate_m(limit=100000):
    # TODO - rename this
    """Get a list of squared numbers, this give us the number of
    rows and columns to use for the main grid canvas we will place images on,
    E.G.
    4 images = 2 x 2 grid
    6 = 3 x 3 grid

    Args:
        limit (int): the upper count to calculate squared numbers.
        a limit of 10 produces: [1, 4, 9, 16, 25, 36, 49, 64, 81]
        which would be [1, 2x2, 3x3, 4x4, 5x5, 6x6, 7x7, 8x8, 9x9]


    Return: (list) of squared numbers up to the limit value"""
    return [i * i for i in range(1, limit)]


def grid(n, m):
    """Given the amount of images we ar working with work out what grid (or m)
    we will need.

    Args:
        n (int): the number of image files
        m (list): of ints from calculate_m()

    Returns: (float)

    """
    for i, m in enumerate(m):
        if m - n > 0 or m - n == 0:
            # loop stops when the amount of images can fit in a grid
            # eg ((m = 9) - (word_count = 5) = greater than 0 so use 9 (3x3)
            return float(m)
