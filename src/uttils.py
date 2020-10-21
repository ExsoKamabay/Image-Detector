from cv2utils import * ; from cv2 import *; from random import choice ;from json import * ;
from terminal_viewer import show_image ; from .TerminalBanner import Terminal_banner ;

class Img_Object_DetectorAI:
    def __init__(self):
        setattr(self,"colors",(choice(["#0066ff","#1e7b1e","#00b3b3"])));
    def banner(self):
        print(Terminal_banner(string="IMGOD",font1="isometric1",font2="isometric2",font3="isometric3",
                font4="isometric4",color=getattr(self,"colors"),bg_color=None).random_font,"  ",
                Terminal_banner(string=" Image Object Detector ",font="lalia",decoration="arrow_wave1",
                color=getattr(self,"colors"),bg_color=None).textArt);
        setattr(self,"xban",(Terminal_banner(decoration="fancy14",
        reverse=True,color=getattr(self,"colors"),bg_color=None).decoration));
    def detect_img(self,img):
        setattr(self,"image",(imread(img)));
        setattr(self,"write1",(FaceDnn().detect_faces(getattr(self,"image"))));
        setattr(self,"write2",(FaceCascade().detect_faces(getattr(self,"image"))));
        setattr(self,"write3",(EyeCascade().detect_eyes(getattr(self,"image"))));
        try:
            return ("confidence : %s - box : %s\nboxEye : X : %s - Y : %s"%(
                getattr(self,"write1")[0]["confidence"],getattr(self,"write2")[0]["box"],
                getattr(self,"write3")[0]["box"],getattr(self,"write3")[1]["box"]));
        except:
            return ("confidence : %s - box : %s\nboxEye : X : unknown - Y : unknown"%(
                getattr(self,"write1")[0]["confidence"],getattr(self,"write2")[0]["box"]));
    def packing_img(self,file):
        setattr(self,"reading",(loads(open(file).read())));
        for names,image in zip(
        getattr(self,"reading").keys(),
        getattr(self,"reading").values()):
            show_image(image,30);
            print(Terminal_banner(string="Name : "+names,
            color=getattr(self,"colors"),bg_color=None).strings);
            print(Terminal_banner(string=str(self.detect_img(image))+"\n",
            color=getattr(self,"colors"),bg_color=None).strings);