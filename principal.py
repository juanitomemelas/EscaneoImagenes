# Import required packages
import cv2
import pytesseract
import os
from objetos.imagen import Imagen
import utilerias



# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'



def lecturaImagen(fileName, fileNameTXT):
    # Read image from which text needs to be extracted
    img = cv2.imread(fileName)
    # Preprocessing the image starts
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Applying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # A text file is created and flushed
    file = open(fileNameTXT, "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    textoEncontrado =""
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        # Open the file in append mode
        file = open(fileNameTXT, "a")        
        # Apply OCR on the cropped image        
        # Appending the text into file
        txt = pytesseract.image_to_string(im2[y:y + h, x:x + w])
        file.write(txt)
        # Close the file
        file.close
        textoEncontrado = "".join(txt)

    img1 = Imagen(fileName, textoEncontrado,fileNameTXT) # imagenes_nombre, imagenes_texto, imagenes_ruta):
    print(img1.imagenes_texto)



# assign directory
directory = 'C:/Users/mahon/Pictures/Screenshots'
# its required to define if it's a img
xs = ['.png', '.jpg', '.bmp'] 


# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
#        print(f)
#        print(os.path.splitext(os.path.basename(f))[0])
        if  any(os.path.splitext(os.path.basename(f))[1] in s for s in xs):
            lecturaImagen(f, os.path.splitext(os.path.basename(f))[0]+'.txt')
    