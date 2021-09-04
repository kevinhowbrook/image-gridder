from app.image_grid import ImageGrid

from .test_utils import delete_files, make_test_images


def test_image_grid():
    make_test_images(
        [(100, 200), (200, 300), (400, 400), (420, 629)],
        ["blue", "red", "yellow", "green"],
    )
    # instantiation
    image_grid = ImageGrid(
        image_directory="tests/images",
        final_image_path="tests/images",
        final_image_name="final_test_image.jpg",
        resized_image_directory="tests/images/resized_images",
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)
    delete_files("tests/images/*.jpg")