import glob
import os
import random

from PIL import Image

from app import utils


def delete_files(dir_path):
    """Helper method for deleting files in a directory

    Args:
        dir_path (string): The path containing files to be deleted.
        E.G. 'images/new/*.jpg'
    """
    files = glob.glob(dir_path)
    for f in files:
        os.remove(f)


def make_test_images(sizes, colours):
    """Helper method for creating images to test with,
    saves them to tests/images

    Args:
        sizes (list): list of tuples for image sizes.
        colours (list): list of colours to use.
    """
    for i, v in enumerate(sizes):
        colour = random.choice(colours)
        image = Image.new("RGB", v, color=colour)
        image.save(f"tests/images/{i}.png", format="png")


def test_numfiles():
    # Make some test images to use as files
    make_test_images(
        [(100, 200), (200, 300), (400, 400), (420, 629)],
        ["blue", "red", "yellow", "green"],
    )
    assert utils.numfiles("tests/images") == 5  # 4 + the __init__ file


def test_get_file_paths():
    # Make some test images to use as files
    make_test_images(
        [(100, 200), (200, 300), (400, 400), (420, 629)],
        ["blue", "red", "yellow", "green"],
    )
    paths = utils.get_file_paths("tests/images")
    assert paths == [
        "tests/images/3.png",
        "tests/images/1.png",
        "tests/images/0.png",
        "tests/images/2.png",
    ]


def test_max_image_size():
    """Test we can calculate the max image size from a directory of images"""
    # Make some test images
    make_test_images(
        [(100, 200), (200, 300), (400, 400), (420, 629)],
        ["blue", "red", "yellow", "green"],
    )
    # Get the max file size
    max_size = utils.get_max_image_size("tests/images")
    assert max_size == (420, 629)


# def test_resize_images():
#     # Make some test images
#     make_test_images(
#         [(100, 200), (200, 300), (400, 400), (420, 629)],
#         ["blue", "red", "yellow", "green"],
#     )
#     utils.resize_images(
#         directory_of_original_images="tests/images",
#         output_directory="tests/images/resized_images",
#     )

#     # Assert that 4 new image files were created
#     file_paths = [
#         os.path.join("tests/images/resized_images", filename)
#         for filename in os.listdir("tests/images/resized_images")
#         if filename.endswith(".png")
#     ]
#     assert file_paths
#     assert len(file_paths) == 4

#     # Assert that all the images are the same size, the height and width
#     # should be the same value as our largest image from the test images we
#     # created, E.G. 420x629 should square off to 629x629
#     for i in file_paths:
#         img = Image.open(i, "r")
#         assert img.size == (629, 629)


def test_calculate_m():
    m = utils.calculate_m(10)
    assert m == [1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert m[0] == 1
    assert m[1] == 2 * 2
    assert m[2] == 3 * 3
    assert m[3] == 4 * 4
    assert m[4] == 5 * 5
    assert m[5] == 6 * 6
    assert m[6] == 7 * 7
    assert m[7] == 8 * 8
    assert m[8] == 9 * 9


def test_grid():
    # Test we can calculate how many images we can fit on an even grid
    # make a larger list of possible grids, 2x2, 3x3 etc...
    m = utils.calculate_m(1000)
    # Number of files to work into a grid.
    # What's expected here is that
    # 3 images would need a 4x4 grid
    # 4 images would need a 2x2 grid etc
    n = 3
    assert utils.grid(n, m) == 4.0
    # test a few more
    assert utils.grid(10, m) == 16.0
    assert utils.grid(4, m) == 4.0
    assert utils.grid(1000, m) == 1024.0
