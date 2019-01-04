from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
def watermark_text(i_path,o_path,text,pos):
	pic=Image.open(i_path)
	drawing=ImageDraw.Draw(pic)
	black=(3,8,12)
	font=ImageFont.truetype("Arial.ttf",40)
	drawing.text(pos,text,fill=black,font=font)
	pic.save(o_path)

if __name__=='__main__':
	i_path=sys.argv[1]
	o_path=sys.argv[2]
	x=int(sys.argv[3])
	y=int(sys.argv[4])
	pos=(x,y)
	watermark_text(i_path,o_path,"sample text",pos)
