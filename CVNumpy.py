import cv2
import numpy as np

def detect_ui_elements(image_path):
  """
  Detects UI elements in an image and provides a textual description.

  Args:
    image_path: Path to the image file.

  Returns:
    A string describing the detected UI elements.
  """

  img = cv2.imread(image_path)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 50, 150)

  contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  descriptions = []
  for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)

    # Simple shape classification (basic)
    if w/h > 2 or h/w > 2: 
      descriptions.append(f"Possible input field or button at ({x}, {y}) with width {w} and height {h}")
    elif area > 1000: 
      descriptions.append(f"Possible navigation bar or large button at ({x}, {y}) with width {w} and height {h}")
    else:
      descriptions.append(f"Detected UI element at ({x}, {y}) with width {w} and height {h}")

  return "\n".join(descriptions)

# Example usage
image_path = 'image.png' 
element_descriptions = detect_ui_elements(image_path)
print(element_descriptions)