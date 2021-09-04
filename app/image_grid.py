import math

from PIL import Image, ImageDraw

from . import utils


class ImageGrid:
    def __init__(
        self,
        final_image_border_width=0,
        final_image_name="final.jpg",
        final_image_path="./",
        resized_image_directory="images/resized",
        image_directory="images",
        canvas_colour="white",
        *args,
        **kwargs,
    ):
        self.canvas_colour = canvas_colour
        self.image_directory = image_directory
        self.resized_image_directory = resized_image_directory
        self.final_image_path = final_image_path
        self.final_image_name = final_image_name
        self.final_image_border_width = final_image_border_width
        self.numfiles = utils.numfiles(image_directory)
        self.max_image_size = utils.get_max_image_size(image_directory)[1]
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
                fill="white",
                width=self.final_image_border_width,
            )
            k += 1
        self.canvas.save(
            f"{self.final_image_path}/{self.final_image_name}"
        )  # save the image.
