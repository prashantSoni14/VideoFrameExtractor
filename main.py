import cv2
import os

# Function to extract frames
def FrameCapture(path1, filename, path2):
    # creating video object
    vidObj = cv2.VideoCapture(os.path.join(path1, filename))

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    # checks is video is open sccessfully or not.
    if vidObj.isOpened():
        print("Downloading Please wait")
        try:
            while success:
                # extracting frames
                success, image = vidObj.read()

                # Saves the frames with frame-count
                cv2.imwrite(os.path.join(path2, 'frame%d.jpg' % count), image)
                print("#", end="")
                if count%100 == 0:
                    print("\n")
                count += 1
        # Exception Handling
        except:
            print("\nImage Excrated in folder : " + os.getcwd()+"\\output\\")
    else:
        print("Not able to open Video, please check the input video name")


if __name__ == '__main__':
    # Calling the function Argument Video path, video name, output folder
    FrameCapture(".\\video\\", "invideo-ai-720 Epic Highway Drive_ Feel the Speed! 2024-07-13.mp4", ".\\output\\")