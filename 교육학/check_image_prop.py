from PIL import Image

src_path = r'C:/Users/LENOVO/.gemini/antigravity/brain/022db66e-d9b4-4946-a17a-1330d1eea034/.user_uploaded/media_1791709337620_23f9b2a6.png'
img = Image.open(src_path)
print("Image size:", img.size)
print("Image mode:", img.mode)
print("Image format:", img.format)
