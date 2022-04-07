# -*- coding: utf-8 -*-
from tkinter import *
from itertools import groupby
import tkinter.filedialog
import codecs
import sys
import re
import os
import xlsxwriter
import subprocess
import xlrd
import tkinter.font
#reload(sys)
from IPAEquv import IPAEquivalent
from Labelchang1 import Labelchanger1
from Labelchang2 import Labelchanger2
from Syllabification import Syllabify
from Syll_label import Labeling
from phoneme import Phoneme
# reload(sys)
# sys.setdefaultencoding('utf-8')
def load_file(entries):
	fileinput=open(tkinter.filedialog.askopenfilename(),'r')
	path=os.getcwd()
	fileoutput=open(path+"/"+"PLS_XML_W3C_Format_Lexicon.txt", 'a')
	fileoutput1=open(path+"/"+"PLS_Festival_Format_Lexicon.txt", 'a')
	for word in fileinput:
		hindi_input=word.rstrip()
		entries['Hindi Input'].delete(0,END)
		entries['Hindi Input'].insert(0,word)
		Phoneme(entries)
		fileoutput.write("<lexeme>\n")
		fileoutput.write("<Grapheme>"+(word).rstrip()+"</Grapheme>"+"\n"+"<PLSB>"+ entries['Prosodic Label(PLSB)'].get() +"</PLSB>"+'\n'+ "<Phoneme>"+entries['Phoneme Level(IPA)'].get()+"</Phoneme>"+'\n' )
		fileoutput.write("</lexeme>\n")

		fileoutput1.write("( "+(word).rstrip()+"\t"+entries['Phoneme Level(ASCII)'].get()+" )\n" )
		subprocess.call(["sed -i 's/\\\t)//g'",path+"/"+"PLS_Festival_Format_Lexicon.txt"], shell=True)
