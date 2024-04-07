import cv2
import pytesseract
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to convert image to text
def image_to_text(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to do OCR on the grayscale image
    text = pytesseract.image_to_string(gray_image)

    return text

# Path to the image file
image_path = 'sample_image.jpg'

# Convert image to text
text = image_to_text(image_path)

# Speak the text
speak(text)
