from PIL import Image, ImageDraw, ImageFont
def get_image(title):
    img = Image.new('RGB', (60, 30), color = (0,0,0))
    img = img.resize((300, 450))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 20)
    draw.text((50, 225), title, font=font)
    img.save('static/{}.png'.format(title))
    return 'static/{}.png'.format(title) 