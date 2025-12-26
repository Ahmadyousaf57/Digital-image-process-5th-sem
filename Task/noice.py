import cv2
import numpy as np
import random

def add_salt_and_pepper_noise(image, prob=0.02):
    """
    Add salt and pepper noise to image.
    
    :param image: Input image (numpy array)
    :param prob: Probability of noise (default 0.02 = 2%)
    :return: Noisy image
    """
    output = np.copy(image)
    black = 0
    white = 255
    
    # Generate random noise
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r = random.random()
            if r < prob:   # pepper noise
                output[i][j] = black
            elif r > 1 - prob:  # salt noise
                output[i][j] = white
    
    return output


# ---- Example usage ----
# Load image
img = cv2.imread("download.jpeg", cv2.IMREAD_GRAYSCALE)  # use grayscale for clarity

# Apply salt & pepper noise
noisy_img = add_salt_and_pepper_noise(img, prob=0.05)

# Save and show result
cv2.imwrite("noisy_image.jpg", noisy_img)
cv2.imshow("Noisy Image", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
