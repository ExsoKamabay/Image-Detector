from .TerminalBanner import Terminal_banner ;
from random import choice ; from terminal_viewer import show_image
warna = choice(["#0066ff","#1e7b1e","#00b3b3"]);
__hlp = str(Terminal_banner(string="""\n\n
input : <type> <infile>,
type  : IMG/JSON  - infile : input file path,
usage : img test.jpg - JSON test.json,
exit  : exit,
_________________________________________
create file json,'name':'path file image'
Example : keyword names up to you!
    {
        'name1':'test1.jpg',
        'name2':'test2.png',
        'name3':'test3.jpeg'
    }
------------------------------------------

Name app : IMGOD (Image Object Detector),
Author : Exso Kamabay,
mail : lexyong@gmail.com,
copyright : 21102020,\n\n%s
"""%(Terminal_banner(string=" LICENCE MIT ",font="lalia",color=warna,
    bg_color=None,decoration="diamond3").textArt),color=warna,bg_color=None).strings)
def help_me():
    return __hlp;