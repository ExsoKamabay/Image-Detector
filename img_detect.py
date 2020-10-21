from src import * ; from random import choice ; from terminal_viewer import show_image ; from os import system ;
class Image_Detector(Img_Object_DetectorAI):
    def __init__(self):
        Img_Object_DetectorAI().banner();
        setattr(self,'color',(choice(["#0066ff","#1e7b1e","#00b3b3"])))
    def main(self):
        print(Terminal_banner(decoration='champion1',
        color=getattr(self,"color"),bg_color=None,reverse=False).decoration,
        Terminal_banner(string=" FILE ",color=getattr(self,"color"),bg_color=None).strings,
        Terminal_banner(string=" type infile ",font="lalia",decoration="block1",
        color=getattr(self,"color"),bg_color=None).textArt)
        setattr(self,"xban",(Terminal_banner(decoration='champion1',
        color=getattr(self,"color"),bg_color=None,reverse=False).decoration));
        setattr(self,"input",(input(getattr(self,"xban")).split()));
        if not getattr(self,"input") or getattr(self,"input")[0] == str("exit"):
            print(Terminal_banner(string="\n\t:)\n"*2,
            color=getattr(self,"color"),bg_color=None).strings);
        elif getattr(self,"input")[0] in ['IMG','img']:
            show_image(getattr(self,"input")[1],30);
            print(Terminal_banner(string='\nName : not yet known!\n'+Img_Object_DetectorAI().detect_img(
            getattr(self,"input")[1]),color=getattr(self,"color"),bg_color=None).strings+'\n\n');self.main();
        elif getattr(self,"input")[0] in ['HELP','help']:
            system("clear");Img_Object_DetectorAI().banner();
            print(help_me());self.main();
        elif getattr(self,"input")[0] in ['JSON','json']:
            Img_Object_DetectorAI().packing_img(getattr(self,"input")[1]);self.main();
        else:
            print(Terminal_banner(string="\n\t\tInvalid! :) %s\n"%(getattr(self,"input")),
            color=getattr(self,"color"),bg_color=None).strings);
if __name__=="__main__":Image_Detector().main();