

def generate_colors(color_type, n):
    import random
    import string
    colors = []

    for i in range(n):
        if color_type == 'hexa':
            color = '#'
            for j in range(6):
                color += random.choice(string.hexdigits)
            colors.append(color)
        elif color_type == 'rgb':
            r = str(int(random.random() * 256))
            g = str(int(random.random() * 256))
            b = str(int(random.random() * 256))
            color = "rgb(" + r + ", " + g + ", " + b + ")"
            colors.append(color)

    return colors


print(generate_colors('rgb', 10))
