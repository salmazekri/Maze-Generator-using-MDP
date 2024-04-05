def hex_to_rgb(hex_color):
    return [int(hex_color[i:i + 2], 16) for i in range(1, 6, 2)]

def rgb_to_hex(rgb_color):
    rgb_color = [int(x) for x in rgb_color]
    return "#" + "".join(["0{:x}".format(v) if v < 16 else "{:x}".format(v) for v in rgb_color])

def create_color_info(gradient):
    return {"hex": [rgb_to_hex(rgb) for rgb in gradient],
            "red": [rgb[0] for rgb in gradient],
            "green": [rgb[1] for rgb in gradient],
            "blue": [rgb[2] for rgb in gradient]}

def linear_gradient(start_hex, end_hex="#FFFFFF", steps=50):
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    rgb_list = [start_rgb]

    for step in range(1, steps):
        current_rgb = [
            int(start_rgb[channel] + (step / (steps - 1)) * (end_rgb[channel] - start_rgb[channel]))
            for channel in range(3)
        ]
        rgb_list.append(current_rgb)

    return create_color_info(rgb_list)
