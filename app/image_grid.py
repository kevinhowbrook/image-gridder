import math

from PIL import Image, ImageDraw

from . import utils

# TODO: Explain HOW IT WORKS


class ImageGrid:
    """The main image grip class to generate the final image of combined,
    resized tiles:

    Args:
        custom_dimension_for_single_items (int): This will override the size
            that images are resized as individual tiles, useful if you have
            lots of varied image sizes
        image_border_width (int): Applys a px width border to the single tiles
        image_border_colour (tuple): RGB values, E.G. (255, 255, 255)
        individual_image_resize_offset (tuple): This is pretty experimental,
            without it, individual resized images anchor to the top left of the
            tile, set to (2, 2) should centre them, E.G:
            no offset [x ][x ][x ]
            offset (2, 2) [x][x][x]
        final_image_name (string): The filename of the final output image, E.G
            "file.jpg"
        final_image_path (string): The path where to save the final image.
        resized_image_directory (string): The path where to save the resized
            images.
        image_directory (string): The path where the images are you want to
            resize and combine into a grid - this should be your original
            images directory
        canvas_colour (string): Colour of the main canvas
        resize_image_canvas_colour (tuple): The background colour of the
            individual tile images that are resized.

    """

    def __init__(
        self,
        custom_dimension_for_single_items=None,
        image_border_width=0,
        image_border_colour=(255, 255, 255),
        individual_image_resize_offset=None,
        final_image_name="final.jpg",
        final_image_path="./",
        resized_image_directory="images/resized",
        image_directory="images",
        canvas_colour="white",
        resize_image_canvas_colour=(255, 255, 255),
        *args,
        **kwargs,
    ):
        self.canvas_colour = canvas_colour
        self.resize_image_canvas_colour = resize_image_canvas_colour
        self.image_directory = image_directory
        self.resized_image_directory = resized_image_directory
        self.final_image_path = final_image_path
        self.final_image_name = final_image_name
        self.image_border_width = image_border_width
        self.numfiles = utils.numfiles(image_directory)
        self.individual_image_resize_offset = individual_image_resize_offset
        self.max_image_size = utils.get_max_image_size(image_directory)[1]
        self.image_border_colour = (image_border_colour,)
        self.custom_dimension_for_single_items = (
            custom_dimension_for_single_items
        )
        # TODO - rename m
        self.m = math.sqrt(utils.grid(self.numfiles, utils.calculate_m()))
        self.canvas_size = int(self.m) * self.max_image_size
        self.canvas = Image.new(
            "RGB",
            (self.canvas_size, self.canvas_size),
            color=self.canvas_colour,
        )

    def resize_images(self):
        utils.resize_images(
            directory_of_original_images=self.image_directory,
            output_directory=self.resized_image_directory,
            custom_dimention=self.custom_dimension_for_single_items,
            individual_image_resize_offset=self.individual_image_resize_offset,
            resize_image_canvas_colour=self.resize_image_canvas_colour,
        )
        # return the list of files we resized
        return utils.get_file_paths(self.resized_image_directory)

    def make_main_grid_image(self, resized_image_filepaths):
        j = 0  # vertical counter
        k = 0  # horizontal counter
        s = self.max_image_size
        for i, v in enumerate(resized_image_filepaths):
            print(f"making image {i}")
            squares_per_row = int(self.m)
            if i % squares_per_row == 0 and i != 0:
                j += 1
                k = 0
            points = (
                (k * s, j * s),
                (k * s, j * s + s),
                (k * s + s, j * s + s),
                (k * s + s, j * s),
            )
            image = Image.open(v, "r")
            self.canvas.paste(image, points[0])
            ImageDraw.Draw(self.canvas).line(
                (points[0], points[1], points[2], points[3], points[0]),
                fill=self.image_border_colour,
                width=self.image_border_width,
            )
            k += 1
        self.canvas.save(
            f"{self.final_image_path}/{self.final_image_name}"
        )  # save the image.
