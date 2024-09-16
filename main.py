from os import write

import cv2
import os

video = cv2.VideoCapture("./BadAppleBadBAD6Short.mp4")

if not os.path.exists("frames"):
    os.makedirs("frames")

currentframe = 0

with open("BadApple.as", "w") as program:
    program.write("LDI r10 240\nLDI r11 241\nLDI r12 242\nLDI r13 245\nLDI r14 246\n")

    while True:
        ret, frame = video.read()

        try:
            width, height, _ = frame.shape
        except AttributeError:
            break

        program.write(f"STR r14 r0 r0\n")

        if ret:
            for i in range(height):
                for j in range(width):
                    pixel = frame[j, i]
                    luminance = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]

                    if luminance > 127:
                        program.write(f"LDI r1 {31 - i}\n")
                        program.write(f"LDI r2 {31 -j}\n")
                        program.write("STR r10 r1 r0\n")
                        program.write("STR r11 r2 r0\n")
                        program.write(f"STR r12 r0 r0\n")
                    # else:
                    #     print(0)
            program.write(f"STR r13 r0 r0\n")

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1

        if currentframe > 6:
            break
    program.write(f"HLT")


# Release all space and windows once done
video.release()
cv2.destroyAllWindows()