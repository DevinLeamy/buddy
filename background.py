R     = (255, 0,   0)
G     = (0,   255, 0)
Y     = (255, 255, 0)
W     = (255, 255, 255)

ERROR_RATING = -1

ERROR_BACKGROUND = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, W, W, W, W, R, R,
    R, R, W, R, R, R, R, R,
    R, R, W, W, W, W, R, R,
    R, R, W, R, R, R, R, R,
    R, R, W, W, W, W, R, R,
    R, R, R, R, R, R, R, R,
]

def generate_background(rating):
    color = None

    if rating == ERROR_RATING:
        return ERROR_BACKGROUND
    elif rating <= 2:
        color = R
    elif rating <= 5:
        color = Y
    else:
        color = G

    matrix = [color for _ in range(0, 64)]

    return matrix

def combine_colors(background, foreground):
    for i in range(0, 64):
        if foreground[i] == W:
            background[i] = foreground[i]

    return background
