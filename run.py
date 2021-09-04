from app.image_grid import ImageGrid

if __name__ == "__main__":
    # instantiation
    image_grid = ImageGrid(
        image_directory="images",
        image_border_width=2,
        custom_dimension_for_single_items=350,
        individual_image_resize_offset=(2, 2),
        image_border_colour=(123, 123, 123),
    )
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    print(image_grid.__dict__)
