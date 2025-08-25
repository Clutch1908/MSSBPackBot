from io import BytesIO
from PIL import Image
import discord

image_width = 150
image_height = 300

def build_pack_image(cardImageList):
    loadedImages = []
    for image in cardImageList:
        loadedImages.appened(load_image_for_card(image))
    
    total_width = len(loadedImages)*image_width
    total_height = 1*image_height
    pack_image = Image.new('RGBA', (total_width, total_height))
    x_offset = 0
    for loadedImage in loadedImages:
        pack_image.paste(loadedImage, (x_offset, 0))
        x_offset += image_width
    return pack_image

def convert_image_to_file(pack_image):
    with BytesIO() as image_binary:
        pack_image.save(image_binary, 'PNG')
        image_binary.seek(0)
        file = discord.File(fp=image_binary, filename='image.png')
        return file
    
def load_image_for_card(image):
    return Image.open(image).convert('RGBA')   