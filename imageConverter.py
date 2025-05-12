from PIL import Image

# Color mapping dictionary
colors = {
    (224, 236, 211): (34, 177, 76),     # nature
    (246, 239, 228): (0, 0, 0),         # building
    (251, 248, 243): (195, 195, 195),   # concrete
    (255, 255, 255): (127, 127, 127),   # road
    (254, 251, 213): (127, 127, 127),   # road, yellow
    (213, 232, 235): (63, 72, 204),     # water
}

# Function to map a color to its closest match in the dictionary
def colorMap(color):
    closestColor = min(colors.keys(), key=lambda k: sum((a - b) ** 2 for a, b in zip(color[:3], k)))
    return colors[closestColor]

# Function to convert the image using the new color scheme
def convertImage(oldName: str, newName: str):
    image = Image.open(oldName).convert('RGBA')
    pixels = image.load()

    width, height = image.size

    # Iterate through each pixel and apply the color mapping
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            new_color = colorMap((r, g, b))
            pixels[x, y] = (*new_color, a)

    # Go through the image again and remove random pixels
    # We decide if it is a random pixel if it pixel has < 4 of the color in it's neighborhood (including itself)
    for y in range(height):
        for x in range(width):

            r1, g1, b1, a1 = pixels[x, y]
            neighborhood = []

            # Find the colors of the pixels in it's neighborhood
            for i in range(-1, 2):
                for j in range(-1, 2):
                    try:
                        r2, g2, b2, a2 = pixels[x + i, y + j]
                        neighborhood.append((r2, g2, b2))
                    except IndexError:
                        continue

            # Count the number of pixels in the neighborhood that are the same color
            count = neighborhood.count((r1, g1, b1))

            # If there are less than 4 of the same color in the neighborhood, set it to the most common color in the neighborhood
            if count < 4:
                r, g, b = max(neighborhood,key=neighborhood.count)
                pixels[x, y] = (r, g, b, a1)

    image.save(newName)