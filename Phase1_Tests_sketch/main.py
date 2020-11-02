import cv2
import numpy as np
if __name__ == '__main__':
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    img_counter = 0
    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        # 2D curve
        y = np.array([122, 224, 210, 350, 380, 250, 490, 623, 811, 819, 800]) # Given y points
        x = np.array([536, 480, 390, 366, 270, 240, 180, 210, 280, 400, 501]) # Given x points
        z = np.polyfit(x, y, 2) # Line fit

        linespace = np.linspace(0, 1000, 100)
        draw_x = linespace
        draw_y = np.polyval(z, draw_x)  # evaluate the polynomial

        draw_points = np.asarray([draw_x, draw_y]).T.astype(np.int32)  # needs to be int32 and transposed

        cv2.polylines(frame, [draw_points], False, (255, 0, 0), 5, 8,0)  # args: image, points, closed, color

        cv2.line(frame, (0, 0), (511, 511), (255, 255, 0), 10)  # Draw line

        # Overlay image on the background
        img1 = cv2.imread('opencv_frame_0.png')

        # Overlay picture to video feed
        frame = cv2.addWeighted(frame, 0.5, img1, 0.5, 0.0)

        # Take picture of the webcam
        if key == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
        # exit on ESC
        if key == 27:
            break

    cv2.destroyWindow("preview")
    vc.release()
