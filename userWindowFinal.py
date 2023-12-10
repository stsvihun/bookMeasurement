import tkinter as tk
from tkinter import ttk
import tksheet
import cv2
import os
import numpy as np
import time
import math
import object_detector
import bounded_rectangle
import getMeasurements
import images
import excel

# Click event
def click():
    action.configure(text="Getting Measurements...")
    
    def continue_processing():
        # initialize camera index
        camera1 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        camera2 = cv2.VideoCapture(2, cv2.CAP_DSHOW)

        # captureImage
        images.capture_image(camera1, "captured_image1.jpg")
        images.capture_image(camera2, "captured_image2.jpg")

        img1 = cv2.imread("captured_image1.jpg")
        assert os.path.exists("captured_image1.jpg")

        img2 = cv2.imread("captured_image2.jpg")
        assert os.path.exists("captured_image2.jpg")

        img1 = img1[125:295, 0:600]
        img2 = img2[80:240, 50:700]

        #Load Object Detector
        contours = object_detector.detect_objects(img1)
        bounded_rectangle.draw_object_boundaries(img1, contours)
        width, spineW = getMeasurements.get_dimensions(img1, contours)

        time.sleep(1)

        contours = object_detector.detect_objects(img2)
        bounded_rectangle.draw_object_boundaries(img2, contours)
        height, spineH = getMeasurements.get_dimensions(img2, contours)

        print(height)
        print(width)
        print(spineW)
        print(spineH)

        width =(0.5979*width)-11.655
        print(width)
        width = math.ceil(width)
        height =(0.7823*height) -6.9339
        print(height)
        height = math.ceil(height)
        spineW =(0.5564*spineW)-3.2133
        spineH =(0.8184*spineH)-5.3682

        print("spineW: " + str(spineW))
        print("spineH: " + str(spineH))
        if (spineW > spineH):
            spine = spineW
        else:
            spine = spineH
        spine = math.ceil(spine)
        print("height: " + str(height))
        print("width: " + str(width))
        print("spine: " + str(spine))

        # Get existing data from the sheet
        current_data = sheet.get_sheet_data()

        # Append the new values to the existing data
        new_row = [height, width, spine]
        current_data.append(new_row)

        # Set the updated data to the sheet
        sheet.set_sheet_data(current_data)

        excel.append_data_to_excel(height, width, spine, 'dimensions.xlsx')
        action.configure(text="Get Measurements")  # Reset the button text

    # Schedule the continue_processing function to run after 1000 milliseconds (1 second)
    win.after(1000, continue_processing)

win = tk.Tk()
win.title("Book Measurement Control Window")

# Adding Button with increased padding to make it appear larger
action = ttk.Button(win, text="Get Measurements", command=click, padding=(20, 10))
action.pack(side=tk.TOP, pady=10)  # Place the button at the top with some padding

# Create TkSheet (Table) with column labels
column_labels = ["Height (mm)", "Width (mm)", "Spine (mm)"]
sheet = tksheet.Sheet(win, headers=column_labels)
sheet.enable_bindings(("single_select", "row_select", "column_width_resize", "arrowkeys",
                       "right_click_popup_menu", "rc_select", "rc_insert_row", "rc_delete_row",
                       "copy", "cut", "paste", "delete", "undo", "edit_cell", "select_row", "shift_select"))
sheet.pack(expand=tk.YES, fill=tk.BOTH)  # Allow the sheet to expand in both directions

# Set the window size (width x height)
win.geometry("400x400")

# Keep window on top
win.attributes('-topmost', True)

win.mainloop()
