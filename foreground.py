from sense_hat import SenseHat

sense = SenseHat()

W = (255, 255, 255)
O = (0, 0, 0)
happy = [
O, O, O, O, O, O, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, O, O, O, O, O, O,
O, W, O, O, O, O, W, O,
O, O, W, W, W, W, O, O,
O, O, O, O, O, O, O, O]

medium = [
O, O, O, O, O, O, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, W, W, W, W, W, W, O,
O, O, O, O, O, O, O, O
]

sad = [
O, O, O, O, O, O, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, W, O, O, W, O, O,
O, O, O, O, O, O, O, O,
O, O, W, W, W, W, O, O,
O, W, O, O, O, O, W, O,
O, O, O, O, O, O, O, O
]

def generate_foreground(rating):
    if rating <= 2:
        return sad
    elif rating <= 5:
        return medium
    else:
        return happy
