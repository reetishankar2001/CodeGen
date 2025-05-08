import cv2
import numpy as np
import pytesseract
from PIL import Image
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('ui_element_classifier.h5')

def detect_and_classify_ui_elements(image_path):
  """
  Detects and classifies UI elements in an image, extracts text, 
  and maps text to corresponding elements.

  Args:
    image_path: Path to the image file.

  Returns:
    A list of dictionaries, where each dictionary represents a detected UI element 
    with its type, bounding box coordinates, and extracted text.
  """

  img = cv2.imread(image_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Use a pre-trained object detection model (e.g., Faster R-CNN, YOLO)
  # Here, we'll use a simplified example with edge detection and contour analysis
  edges = cv2.Canny(gray, 50, 150)
  contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  detected_elements = []
  for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    roi = img[y:y+h, x:x+w]  # Extract Region of Interest

    # Preprocess the ROI for classification
    roi = cv2.resize(roi, (224, 224))  # Resize for the model's input size
    roi = roi / 255.0  # Normalize pixel values

    # Predict the class of the UI element
    prediction = model.predict(np.expand_dims(roi, axis=0))
    class_idx = np.argmax(prediction)
    class_labels = ['button', 'input_field', 'navigation_bar', 'image', 'text'] 
    element_type = class_labels[class_idx]

    # Extract text from the ROI using Tesseract
    if element_type == 'text' or element_type == 'button': 
      roi_pil = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)) 
      text = pytesseract.image_to_string(roi_pil) 
    else:
      text = None

    # Create a dictionary to represent the detected element
    element = {
        'type': element_type,
        'bounding_box': (x, y, w, h),
        'text': text
    }
    detected_elements.append(element)

  return detected_elements

# Example usage
image_path = 'image.png'
detected_elements = detect_and_classify_ui_elements(image_path)

# Display the results
for element in detected_elements:
  print(f"Detected: {element['type']}")
  print(f"Bounding Box: {element['bounding_box']}")
  if element['text']:
    print(f"Extracted Text:", element['text'])