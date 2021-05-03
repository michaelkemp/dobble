import cairosvg
from PIL import Image, ImageChops

for i in range(0, 57):
	svgfile = "img-" + str(i).zfill(2) + ".svg"
	pngfile = "tmp-" + str(i).zfill(2) + ".png"
	cairosvg.svg2png(url=svgfile, write_to=pngfile, scale=15.0) # 48 * 15 = 720

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

for i in range(0, 57):
	tmpfile = "tmp-" + str(i).zfill(2) + ".png"
	pngfile = "image-" + str(i).zfill(2) + ".png"
	im = Image.open(tmpfile)
	im = trim(im)
	MAX_SIZE = (500, 500)
	im.thumbnail(MAX_SIZE)
	wide, high = im.size
	card = Image.new('RGBA', (500, 500), (255, 0, 0, 0))
	card.paste(im, (250-(wide//2),250-(high//2)), im)
	card.save(pngfile)
