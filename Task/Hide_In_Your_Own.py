import cv2
import os

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed")
        break
    cv2.imshow("Lets hide secret ....!", frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:  # ESC key
        print("OK thanks")
        break
    elif k % 256 == 32:  # SPACE key
        img_name = "orignal.jpg"
        cv2.imwrite(img_name, frame)
        print("captured")
        image = cv2.imread(img_name)
        cv2.imshow('frame', image)
        break

# ✅ FIX: Release the camera before closing windows
cam.release()
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("orignal gray Image", gray_image)
cv2.waitKey()

# name for hide in pic
name = input("Enter Secret Message : ")
print(name)

ascii = []
binary = []
for x in name:
    if (ord(x) == 32):
        ascii.append(123)
    else:
        ascii.append(ord(x))

for y in ascii:
    binary.append((bin(y)[2:]))
print(ascii)
print(binary)

list_bits = []
for y in binary:
    for x in y:
        list_bits.append(x)
print(list_bits)
print(len(list_bits))

with open("stegokey.txt", "w+") as f:
    f.write(str(len(list_bits)))

# selected pixels for hide name
target_pix = []
for a in range(len(list_bits)):
    target_pix.append(gray_image[0][a])
print(target_pix)

binary_pix = []  # converted into binary
for x in range(len(target_pix)):
    bv = (bin(target_pix[x])[2:])
    binary_pix.append(bv)
print(binary_pix)

# tampered binary pixels
tampered_binary_pix = []
for x in range(len(binary_pix)):
    tampered_binary_pix.append(binary_pix[x][:-1] + list_bits[x])
print(tampered_binary_pix)

# tampered decimal pixel values
tampered_deci_pix = []
for x in range(len(tampered_binary_pix)):
    tampered_deci_pix.append(int(tampered_binary_pix[x], 2))
print(tampered_deci_pix)

# Tampered the Picture (hidden msg)
for x in range(len(tampered_deci_pix)):
    gray_image[0][x] = tampered_deci_pix[x]

print("gray tampered", gray_image[0][:len(tampered_deci_pix)])

eni = "Encoded.TIFF"
cv2.imwrite(eni, gray_image)
ei = cv2.imread(eni)
gei = cv2.cvtColor(ei, cv2.COLOR_BGR2GRAY)
cv2.imshow("Tampered Image", gei)
print(gray_image.shape)
print(gei.shape)

print("encoded pic pixels", gei[0][:len(tampered_deci_pix)])
cv2.waitKey()
