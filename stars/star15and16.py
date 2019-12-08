from colorama import Fore, Style
from pprint import pprint


def split_image_into_layers(image_data, img_width, img_height):
    surface = img_width * img_height
    amount_of_layers = int(len(image_data) / surface)
    layers = []
    for layer_index in range(amount_of_layers):
        layer_data = image_data[layer_index * surface : (layer_index + 1) * surface]
        layer = {
            "index": layer_index,
            "data": layer_data,
            "zero_count": layer_data.count("0"),
            "one_count": layer_data.count("1"),
            "two_count": layer_data.count("2"),
        }
        layers.append(layer)
    return layers


def decode_image(layers):
    image = [int(pixel) for pixel in layers[0]["data"]]
    for layer in layers[1:]:
        pixel_index = 0
        for layer_pixel in map(int, layer["data"]):
            if image[pixel_index] == 2 and layer_pixel != 2:
                image[pixel_index] = layer_pixel
            pixel_index += 1
    return image


def run_star15():
    img_width, img_height = 25, 6
    with open("input/star15") as input_file:
        layers = split_image_into_layers(
            input_file.read().strip(), img_width, img_height
        )
    min_layer = min(layers, key=lambda layer: layer["zero_count"])
    one_multiplied_by_two = min_layer["one_count"] * min_layer["two_count"]
    return f"Final number: {one_multiplied_by_two}"


def run_star16():
    img_width, img_height = 25, 6

    with open("input/star15") as input_file:
        layers = split_image_into_layers(
            input_file.read().strip(), img_width, img_height
        )

    print(f"Final image:")
    image = decode_image(layers)
    for y in range(img_height):
        for x in range(img_width):
            pixel_index = y * img_width + x
            pixel_str = image[pixel_index] if image[pixel_index] == 1 else " "
            print(pixel_str, end=" ")
        print()
    return f"Image message: CYUAH"
