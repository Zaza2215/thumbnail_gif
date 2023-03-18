import os

from PIL import Image


def thumbnail_gif(path_file: str, save_path: str, resolution: tuple):
    if not os.path.isfile(path_file):
        raise ValueError(f"{path_file} is not a file")
    if '.gif' != os.path.splitext(path_file)[-1]:
        raise ValueError(f"Error extension, excepted .gif")

    gif_image = Image.open(path_file)
    # Get options of gif
    options = {
        'loop': gif_image.info['loop'],
        'duration': gif_image.info['duration']
    }
    frames = []

    # Iterate over each frame in the GIF
    for frame in range(gif_image.n_frames):
        # Seek to the current frame
        gif_image.seek(frame)

        # Convert the current frame to JPEG format
        jpg_image = gif_image.convert("RGB")
        jpg_image.thumbnail(resolution)
        frames.append(jpg_image)

    frames[0].save(
        save_path,
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        **options
    )


if __name__ == '__main__':
    thumbnail_gif('my_gif.gif', 'my_gif_t.gif', (320, 240))
