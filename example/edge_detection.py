import numpy as np
import cv2

# Custom Sobel operator kernels (Gx, Gy)
def get_custom_sobel_kernels():
    Gx = np.array([[-np.sqrt(2)/4, 0, np.sqrt(2)/4],
                   [-1, 0, 1],
                   [-np.sqrt(2)/4, 0, np.sqrt(2)/4]])
    
    Gy = np.array([[-np.sqrt(2)/4, -1, -np.sqrt(2)/4],
                   [0, 0, 0],
                   [np.sqrt(2)/4, 1, np.sqrt(2)/4]])
    
    return Gx, Gy

# Median filter for noise reduction
def apply_median_filter(img, kernel_size=5):
    return cv2.medianBlur(img, kernel_size)

# Calculating gradients with custom Sobel operator
def custom_sobel_operator(image, Gx, Gy):
    grad_x = cv2.filter2D(image, cv2.CV_64F, Gx)
    grad_y = cv2.filter2D(image, cv2.CV_64F, Gy)
    
    magnitude = cv2.magnitude(grad_x, grad_y)
    angle = cv2.phase(grad_x, grad_y, angleInDegrees=False)
    
    return magnitude, angle

# Adaptive thresholding based on iterative mean values
def calculate_threshold(gradient_magnitude, tolerance=1e-3):
    T0 = np.max(gradient_magnitude)
    T1 = np.min(gradient_magnitude)
    T = (T0 + T1) / 2
    
    while True:
        Ta_values = gradient_magnitude[gradient_magnitude >= T]
        Tb_values = gradient_magnitude[gradient_magnitude < T]
        
        Ta = np.mean(Ta_values) if len(Ta_values) != 0 else 0
        Tb = np.mean(Tb_values) if len(Tb_values) != 0 else 0
        
        new_T = (Ta + Tb) / 2
        
        if abs(new_T - T) < tolerance:
            break
        
        T = new_T
    
    return T

# Applying the Canny edge detection process with modifications
def Canny_detector(img):
    
    # Step 1: Convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Apply Median Filter for noise reduction
    img = apply_median_filter(img, kernel_size=5)
    
    # Step 3: Apply custom Sobel operator for gradient calculation
    Gx, Gy = get_custom_sobel_kernels()
    mag, ang = custom_sobel_operator(img, Gx, Gy)
    
    # Step 4: Calculate adaptive threshold
    adaptive_threshold = calculate_threshold(mag)
    
    # Step 5: Apply single threshold setting and binarization
    _, binary_output = cv2.threshold(mag, adaptive_threshold, 255, cv2.THRESH_BINARY)
    
    return binary_output

# Main execution for the image
frame = cv2.imread("input/pyramid.jpeg")  # Load your input image here

# Apply the modified Canny detector
canny_img = Canny_detector(frame)

# Save and display the result
cv2.imwrite("output/canny_edge_custom.jpg", canny_img)
cv2.imshow("Custom Canny Edge Detection", canny_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()