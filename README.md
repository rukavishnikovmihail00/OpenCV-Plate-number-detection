# OpenCV-Plate-number-detection
There is a Python script that detects a russian plate number from loaded picture using OpenCV

Firstly you need to add the path to your picture. The picture has to include at least one plate number(with english letters).
It loads the photo into the neural network and teaches it to detect the number. PyTesseract helps me recognize the number: I crop the image as a rectangle and use imate_to_text function to get the number as a line.
