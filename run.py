from app.image_grid import ImageGrid

if __name__ == "__main__":
    # instantiation
    image_grid = ImageGrid(image_directory="images")
    # resize all our images
    resized_images = image_grid.resize_images()
    # make the final image
    image_grid.make_main_grid_image(resized_image_filepaths=resized_images)

    print(image_grid.__dict__)
