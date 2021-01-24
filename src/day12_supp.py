from math import sin, cos, radians


def rotate(px, py, degrees):
    """
    Function for coordinate rotation
    """

    # Transform degrees to radians
    angle = radians(degrees)

    # Perform rotation and return coordinates
    qx = cos(angle) * px - sin(angle) * py
    qy = sin(angle) * px + cos(angle) * py
    return qx, qy
