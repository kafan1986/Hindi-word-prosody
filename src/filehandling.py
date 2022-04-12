# -*- coding: utf-8 -*-
from tkinter import END
import tkinter.filedialog
import os
import subprocess
import tkinter.font
#reload(sys)
from Syll_label import Labeling, TempDICT
from phoneme import Phoneme
from tqdm import tqdm
# reload(sys)
# sys.setdefaultencoding('utf-8')
def load_file(entries):
	fileinput=open(tkinter.filedialog.askopenfilename(),'r')
	path=os.getcwd()
	fileoutput=open(path+"/"+"PLS_XML_W3C_Format_Lexicon.txt", 'a')
	fileoutput1=open(path+"/"+"PLS_Festival_Format_Lexicon.txt", 'a')
	for word in tqdm(fileinput):
		hindi_input=word.rstrip()
		entries['Hindi Input'].delete(0,END)
		entries['Hindi Input'].insert(0,word)
		Phoneme(entries)
		# fileoutput.write("<lexeme>\n")
		# fileoutput.write("<Grapheme>"+(word).rstrip()+"</Grapheme>"+"\n"+"<PLSB>"+ entries['Prosodic Label(PLSB)'].get() +"</PLSB>"+'\n'+ "<Phoneme>"+entries['Phoneme Level(IPA)'].get()+"</Phoneme>"+'\n' )
		# fileoutput.write("</lexeme>\n")

		# fileoutput1.write("( "+(word).rstrip()+"\t"+entries['Phoneme Level(ASCII)'].get()+" )\n" )
		# subprocess.call(["sed -i 's/\\\t)//g'",path+"/"+"PLS_Festival_Format_Lexicon.txt"], shell=True)
	print("--------- TempDICT ---------")
	tmp = TempDICT()
	tmp_view = sorted( ((v,k) for k,v in tmp.items()), reverse=True)
	print("len: ",len(tmp_view))
	for v,k in tmp_view:
		print("%s: %d" % (k,v))
