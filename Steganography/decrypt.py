import cv2

# Ask user for encrypted image path
img_path = input("Enter the path of the encrypted image: ")
img = cv2.imread(img_path)

# Check if image loaded successfully
if img is None:
    print(f"❌ Error: Could not load image at {img_path}. Check the file path and format.")
    exit()

n, m, z = 0, 0, 0
retrieved_password = ""
retrieved_message = ""

# Extract stored password
while True:
    char = chr(img[n, m, z])
    if char == "*":  # Stop at separator (*)
        break
    retrieved_password += char
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Move to the next character after '*'
z = (z + 1) % 3
if z == 0:
    m += 1
if m >= img.shape[1]:  
    m = 0
    n += 1

# Extract message
while True:
    char = chr(img[n, m, z])
    if char == "#":  # Stop at separator (#)
        break
    retrieved_message += char
    z = (z + 1) % 3
    if z == 0:
        m += 1
    if m >= img.shape[1]:  
        m = 0
        n += 1

# Ask for password
entered_password = input("Enter passcode for Decryption: ")

if entered_password == retrieved_password:
    print("✅ Decryption successful! Message:", retrieved_message)
else:
    print("❌ Access Denied! Incorrect password.")
    print("🔍 Entered Password:", repr(entered_password))
