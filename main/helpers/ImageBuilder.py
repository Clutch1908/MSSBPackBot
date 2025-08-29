from io import BytesIO
from PIL import Image
import discord

image_width = 300
image_height = 450
pack_size = 5

def build_pack_image(cardImageList):
    loadedImages = []
    for image in cardImageList:
        loadedImages.append(load_image(image))
    
    total_width = len(loadedImages)*((image_width+10))
    total_height = 1*image_height
    pack_image = Image.new('RGBA', (total_width, total_height))
    x_offset = 10
    for loadedImage in loadedImages:
        pack_image.paste(loadedImage, (x_offset, 0))
        x_offset += (image_width + 10)
    return pack_image

def build_opening_image(pack_images):
    total_width = pack_size * ((image_width+10))
    total_height = len(pack_images) * (image_height + 5)
    opening_image = Image.new('RGBA', (total_width, total_height))
    x_offset = 10
    y_offset = 0
    for image in pack_images:
        opening_image.paste(image, (x_offset, y_offset))
        #push next pack image down by the total height plus the buffer of 5 pixels
        y_offset += (image_height + 5)
    return opening_image

def convert_image_to_file(image):
    with BytesIO() as image_binary:
        image.save(image_binary, 'PNG')
        image_binary.seek(0)
        file = discord.File(fp=image_binary, filename='image.png')
        return file
        
def load_image(image):
    return Image.open(image).convert('RGBA')   
