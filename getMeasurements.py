import cv2
import numpy as np

def get_dimensions(img, contours):
    width = ""
    thickness = ""

    for cnt in contours:
        # Get bounding rectangle
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        if (w>h):
            width = round(w, 3)
            thickness = round(h, 3)
        else:
            width = round(h, 3)
            thickness = round(w, 3)

    print(width)
    print(thickness)

    return width, thickness

# Example usage:
# Assuming you have an image 'img1' and a list of contours 'contours'
# widths, heights = draw_object_boundaries(img1, contours)
# Now 'widths' will contain a list of width values, and 'heights' will contain a list of height values.
