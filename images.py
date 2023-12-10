import cv2

def capture_image(camera, filename):
    if camera.isOpened():
        #camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        #camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        
        ret, frame = camera.read()

        if ret:
            # Save the captured frame to a file
            cv2.imwrite(filename, frame)
            print(f"Image captured and saved as '{filename}'")
        else:
            print("Error: Could not capture an image from the camera.")
        #release camera
        camera.release()
    else:
        print("Error: Camera not opened.")
    cv2.destroyAllWindows()