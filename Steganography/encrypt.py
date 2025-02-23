import cv2

# Ask user for image path
img_path = input("Enter the path of the image to encrypt: ")
img = cv2.imread(img_path)

# Check if image loaded successfully
if img is None:
    print(f"❌ Error: Could not load image at {img_path}. Check the file path and format.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

n, m, z = 0, 0, 0

# Store password first with a separator (*)
for char in password + "*":
    img[n, m, z] = ord(char) % 256  # Ensure pixel value is valid
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Store message with another separator (#)
for char in msg + "#":
    img[n, m, z] = ord(char) % 256
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Ask user for output file path
output_path = input("Enter the path to save the encrypted image: ")
cv2.imwrite(output_path, img)

print("✅ Encryption complete! Password and message stored in:", output_path)

