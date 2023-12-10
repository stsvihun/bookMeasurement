import cv2
import numpy as np

def draw_object_boundaries(img, contours):
    for cnt in contours:
        # Get bounding rectangle
        rect = cv2.minAreaRect(cnt)
        (x, y), (w, h), angle = rect

        # Display rectangle
        box = cv2.boxPoints(rect)
        box = np.intp(box)

        # Draws bounding rectangle
        cv2.polylines(img, [box], True, (255, 0, 0), 2)

        # Draws center circle
        cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

        # Display measurements
        cv2.putText(img, "Width {}".format(round(w)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2,
                    (100, 200, 0), 2)
        cv2.putText(img, "Height {}".format(round(h)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2,
                    (100, 200, 0), 2)

        width = round(w, 3)
        height = round(h, 3)

    #cv2.imshow("Image", img)
    cv2.waitKey(0)

# Example usage:
# Assuming you have an image 'img1' and a list of contours 'contours'
# draw_object_boundaries(img1, contours)
