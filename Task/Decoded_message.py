import cv2
import os
import sys

# Input image path
input_image_path = "Encoded.TIFF"
stego_key_path = "stegokey.txt"

# Check if image exists
if not os.path.exists(input_image_path):
    print(f"Error: Input image '{input_image_path}' not found!")
    sys.exit()  # ✅ Correct way to exit script

# Check if stegokey exists
if not os.path.exists(stego_key_path):
    print(f"Error: Stego key file '{stego_key_path}' not found!")
    sys.exit()

# Read image
image = cv2.imread(input_image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ✅ Show the image and wait for any key to continue
cv2.imshow("Encoded Image", gray_image)
print("Press any key on the image window to decode the hidden message...")
cv2.waitKey(0)  # ✅ Wait indefinitely for a key press
cv2.destroyAllWindows()

# Read stegokey (number of pixels used)
with open(stego_key_path, "r") as f:
    c = f.read().strip()

if not c.isdigit():
    print("Error: Stego key is invalid or empty!")
    sys.exit()

c = int(c)
print(f"Bits to extract: {c}")

# Extract pixels used for encoding
target_pix = [gray_image[0][a] for a in range(c)]

# Convert pixels to binary
binary_pix = [bin(p)[2:].zfill(8) for p in target_pix]

# Extract the last bit of each binary value
tampered_pix = [b[-1] for b in binary_pix]

# Group bits into 7-bit chunks
com_bin = []
k = 0
while k < len(tampered_pix):
    chunk = tampered_pix[k:k+7]
    if len(chunk) == 7:
        com_bin.append("".join(chunk))
    k += 7

# Convert binary to ASCII
recover_ascii = [int(b, 2) for b in com_bin]

# Replace 123 with space
recover_ascii = [32 if val == 123 else val for val in recover_ascii]

# Convert to characters and form the message
decoded_message = "".join(chr(val) for val in recover_ascii)

print("\nDecoded Hidden Message:")
print(decoded_message)

