import random

from app.image_grid import ImageGrid
from tests.test_utils import delete_files, make_test_images

# list of colours for creating images with
list_of_colours = [
    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(1, 1000)
]

if __name__ == "__main__":
    """Example of an image made up of 4 different sized images,"""
    # Make some images for the example run
    make_test_images(
        [(100, 200), (200, 300), (400, 400), (420, 629)],
        list_of_colours,
        path="images/",
    )

    # instantiation
    image_grid = ImageGrid(
        image_directory="images",
        image_border_width=5,
        individual_image_resize_offset=(2, 2),
        image_border_colour=(0, 0, 0),
        resize_image_canvas_colour=(125, 125, 125),
        canvas_colour="white",
        final_image_name="4-images.jpg",
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    # Clean up
    delete_files("images/*.png")
    delete_files("images/resized/*.png")

    """Example of an image made up of 9 images,
    """
    # Make some images for the example run
    make_test_images(
        [
            (100, 200),
            (200, 300),
            (400, 400),
            (420, 629),
            (100, 200),
            (200, 300),
            (400, 400),
            (420, 629),
            (420, 350),
        ],
        list_of_colours,
        path="images/",
    )

    # instantiation
    image_grid = ImageGrid(
        image_directory="images",
        image_border_width=5,
        individual_image_resize_offset=(2, 2),
        image_border_colour=(0, 0, 0),
        resize_image_canvas_colour=(125, 125, 125),
        canvas_colour="white",
        final_image_name="9-images.jpg",
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    # Clean up
    delete_files("images/*.png")
    delete_files("images/resized/*.png")

    """Example of an image made up of 4 equal images,
    """
    # Make some images for the example run
    make_test_images(
        [(400, 400), (400, 400), (400, 400), (400, 400)],
        list_of_colours,
        path="images/",
    )

    # instantiation
    image_grid = ImageGrid(
        image_directory="images",
        image_border_width=5,
        individual_image_resize_offset=(2, 2),
        image_border_colour=(0, 0, 0),
        resize_image_canvas_colour=(125, 125, 125),
        canvas_colour="white",
        final_image_name="4-equal-images.jpg",
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    # Clean up
    delete_files("images/*.png")
    delete_files("images/resized/*.png")

    """Example of an image made up of 100 equal images,
    """
    # Make some images for the example run
    image_list = [(400, 400) for _ in range(1, 100)]
    make_test_images(image_list, list_of_colours, path="images/")

    # instantiation
    image_grid = ImageGrid(
        image_directory="images",
        image_border_width=5,
        individual_image_resize_offset=(2, 2),
        image_border_colour=(0, 0, 0),
        resize_image_canvas_colour=(125, 125, 125),
        canvas_colour="white",
        final_image_name="100-equal-images.jpg",
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    # Clean up
    delete_files("images/*.png")
    delete_files("images/resized/*.png")
