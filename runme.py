import subprocess
import os
import subprocess as sp
import commands
import numpy as np
import re
import time
from time import gmtime, strftime
import sys
from math import sin, cos, acos, fabs, pi, e, log10
import scipy as scp
import scipy.optimize as scpo
import pickle
import shutil
import shelve
import copy
import string
import inspect
from os.path import expanduser
import random
import multiprocessing 
from threading import Timer
kill = lambda process: process.kill()

home = expanduser("~")

k= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

ind=k[::-1].find('/')
ind=ind*-1
piper=k[:ind]
piper=piper.rstrip('/')
ind=piper[::-1].find('/')
ind=ind*-1
piper=piper[:ind]



pipepath=k+'/'
if len(sys.argv)>3:
    outfolder=sys.argv[3]
elif len(sys.argv)<4:
    outfolder=raw_input("Enter directory ")
choice2='y'

choice=2

if len(sys.argv)>6:
   choice2=sys.argv[6]

cw=os.getcwd()
lencw=len(cw)
if not (outfolder[:1]=='/'):
	outfolder=cw+'/'+outfolder


outfolder=outfolder.rstrip('/')
endfolder=outfolder
ind=endfolder[::-1].find('/')
if ind>0:
	ind=ind*-1
	endfolder=endfolder[ind:]
folder=outfolder+'/'
os.system('mkdir '+outfolder+'ms')
os.system('rm -rf '+outfolder+'out')
os.system('mkdir '+outfolder+'out')
msfolder=outfolder+'ms/'
outputfolder=outfolder+'out'

f=open(outputfolder+'/output.txt','a')




files = os.listdir(folder)
if len(sys.argv)>4:
   numb=sys.argv[4]
   num=int(numb)
elif len(sys.argv)<5:
   num=input("Enter userid ")


execfile(pipepath+'input.py')

refAnt='15'
filetype=[]


num3=num
num3=num
num2=num
if not os.path.exists(home+'/.aips'):
	os.system('mkdir ~/.aips')
if not os.path.exists(home+'/.aips/RUN'):
	os.system('mkdir ~/.aips/RUN')
if not os.path.exists(home+'/.boxfiles'):
	os.system('mkdir ~/.boxfiles')
laflag=0
flag=0
laflag=0
flag=0
for k in files:
	name=k
	name=name.rstrip('/')
	if name.endswith('.lta.1'):
		
		new_name=name.replace('.lta.1','_1.lta')
		os.system('mv '+folder+name+' '+folder+new_name)
		name = name[:-6]
		for kk in files:
			name1=kk
	   		if 'FLAGS' in kk and name in kk:
				new_name=name1.replace('.lta.1','_1.lta')
				os.system('mv '+folder+name1+' '+folder+new_name)

for k in files:
	name=k
	name=name.rstrip('/')
	if name.endswith('.lta.2'):
		
		new_name=name.replace('.lta.2','_2.lta')
		os.system('mv '+folder+name+' '+folder+new_name)
		name = name[:-6]
		for kk in files:
			name1=kk
	   		if 'FLAGS' in kk and name in kk:
				new_name=name1.replace('.lta.2','_2.lta')
				os.system('mv '+folder+name1+' '+folder+new_name)

for k in files:
	name=k
	name=name.rstrip('/')				
				
	if name.endswith('.lta'):
	    if (flag==0):
		os.system('mkdir '+outfolder+'lta')	
		flag=1	
	    os.system('listscan '+folder+name)
	    name = name[:-4]
	    if '.' in name:
    		 name1=name[:name.find('.')]
    	    else:
                 name1=name


	    os.system('rm TEST.FITS')
	    for kk in files:
        	if 'FLAGS' in kk and name in kk:
			fin = open(name1+'.log')
			fout = open(name+'fin.log', "wt")
			laflag=1
			kk1=kk
			for line in fin:
				newline=line
				a='ONLINE_FLAGS   NONE'
				b='ONLINE_FLAGS  '+outfolder+'/'+kk
			
				if a in line:
					newline=newline.replace(a,b)
				fout.write(newline)
			fin.close()

			fout.close()
			os.system('rm -rf '+name1+'.log')
			os.system('mv '+name+'fin.log '+name1+'.log')
	    os.system('gvfits '+name1+'.log')
	    if laflag==1:
		    os.system('mv '+folder+kk1+' '+outfolder+'lta/')
	    os.system('mv TEST.FITS '+folder+name+'.FITS')
	    if (os.path.exists(folder+name+'.FITS')):
	    	os.system('mv '+folder+name+'.lta '+outfolder+'lta/'+name+'.lta')
	    os.system('rm '+name1+'.log')
	    os.system('rm '+name1+'.plan')
files = os.listdir(folder)	    

for k in files:
	name=k
	name=name.rstrip('/')
	if name.endswith('.lta'):
	    if (flag==0):
		os.system('mkdir '+outfolder+'lta')	
		flag=1	
	    os.system('listscan '+folder+name)
	    name = name[:-4]
	    if '.' in name:
    		 name1=name[:name.find('.')]
    	    else:
                 name1=name
 	    os.system('rm TEST.FITS')
	    os.system('gvfits '+name1+'.log')
	    os.system('mv '+folder+name+'.lta '+outfolder+'lta/'+name+'.lta')
	    os.system('mv TEST.FITS '+folder+name+'.FITS')
	    os.system('rm '+name1+'.log')
	    os.system('rm '+name1+'.plan')

os.system('mv '+folder+'*FLAGS* '+outfolder+'lta/')
for k in files:
	if 'FIT' not in k and 'fit' not in k:
		os.system('mv '+folder+k+' '+outfolder+'lta/')
os.system('mv '+folder+'*obslogs* '+outfolder+'lta/')
fits=''
files = os.listdir(folder)	
rnum=0 
ref=0    
linescript=[]

for k in files:
	name=k
	name=name.rstrip('/')
	if len(name)>20:
		
		new_name=name[:17]+name[-5:]
		os.system('mv '+folder+name+' '+folder+new_name)


files = os.listdir(folder)	


for k in files:
	name=k
	name1=k
	name=name.rstrip('/')
	if name.endswith('.FITS'):
	    fits='.FITS'
	    name = name[:-5]
	if name.endswith('.fits'):
	    fits='.fits'
	    name = name[:-5]

	msname=msfolder+name+'.ms'
	chakka=folder+k

	default(importuvfits)
	fitsfile=chakka
	
	
	vis=msname
	
	importuvfits()
	ref=ref+1

	ms_active=msname
	
	try:	
	    execfile(pipepath+'info_xtract.py')
	
	    execfile(pipepath+'aips_script_write.py')
	    execfile(pipepath+'log.py')
	except KeyboardInterrupt, keyboardException:
	    print ("Keyboard Interrupt: " + str(keyboardException))
	


	if fracband>0.12:
		num4=num3+rnum
		rnum=rnum+1
		execfile(pipepath+'clean.py')
	linescript.append(notarg)		





	num=num+1

msfolder=msfolder.rstrip('/')
if choice==2:
	files = os.listdir(outfolder)



lenfiles=len(files)
hm=''



indices = [i for i,x in enumerate(filetype) if x == 1]
	

for j in range(lenfiles):
	
	num3=num3+1
conorq='q'



num3=num3-lenfiles

writethat = open(''+outputfolder+'/socode.sh',"w")
writethat.write(' \n')
if os.path.exists(home+'/.bashrc'):
	writethat.write('. ~/.bashrc \n')
writethat.write('export BOX='+home+'/.boxfiles'+'\n')
writethat.write('export OUT='+outputfolder+'\n')

writethat.write('export INP='+outfolder+'\n')
writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
if os.path.exists(home+'/runme'):
	writethat.write('. ~/runme \n')
writethat.write('aips notv'+'\n')
writethat.close()
os.system('chmod +x '+outputfolder+'/socode.sh')



os.system('rm -rf '+outfolder+'ms')
p=[]
write=[None]*lenfiles
read=[None]*lenfiles
for j in range(lenfiles):

	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid



	
	writethat = open(''+outputfolder+'/socode.sh',"w")
	writethat.write(' \n')

	writethat.write('#!/bin/sh \n')

	if os.path.exists(home+'/.bashrc'):
		writethat.write('. ~/.bashrc \n')

	
	writethat.write('export BOX='+home+'/.boxfiles'+'\n')
	writethat.write('export OUT='+outputfolder+'\n')
	writethat.write('export INP='+outfolder+'\n')
	writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
	if os.path.exists(home+'/runme'):
		writethat.write('. ~/runme \n')
	writethat.write('aips notv pr=1 << XXX \n')
	writethat.write(str(num4)+'\n')
	readthat=open(home+'/.aips/RUN/E1'+userid+'.'+userid)	
	for line in readthat:
		writethat.write(line)
	readthat.close()	
	readthat=open(home+'/.aips/RUN/E2'+userid+'.'+userid)	
	for line in readthat:
		writethat.write(line)
	readthat.close()

	writethat.write('kleenex \n')
	writethat.write('XXX \n')
	writethat.close()

	kkk=home+"/.boxfiles/FLAG."+userid
	os.system('rm -rf '+kkk)




	p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
	time.sleep(60)
	p[j].communicate()
for k in range(lenfiles):	
	p[k].communicate()

nsigma=10	
for manga in range(0):
	for j in range(lenfiles):
		
		num4=num3+j
		userid = base_repr(num4, 36)
		if (len(userid)==1) and not (len(userid)>=3):
			userid= '00'+userid
		else:
			userid= '0'+userid
	
		if choice==2:
			execfile(home+'/.boxfiles/flagfilegenerator_'+userid+'.py')
	
	
	p=[]
	write=[None]*lenfiles
	read=[None]*lenfiles
	for j in range(lenfiles):
	
		
		num4=num3+j
		userid = base_repr(num4, 36)
		if (len(userid)==1) and not (len(userid)>=3):
			userid= '00'+userid
		else:
			userid= '0'+userid
	

	
	
		writethat = open(''+outputfolder+'/socode.sh',"w")
		writethat.write(' \n')
	
		writethat.write('#!/bin/sh \n')

		if os.path.exists(home+'/.bashrc'):
			writethat.write('. ~/.bashrc \n')
	
		
		writethat.write('export BOX='+home+'/.boxfiles'+'\n')
		writethat.write('export OUT='+outputfolder+'\n')
		writethat.write('export INP='+outfolder+'\n')
		writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
		if os.path.exists(home+'/runme'):
			writethat.write('. ~/runme \n')
		writethat.write('aips notv pr=1 << XXX \n')
		writethat.write(str(num4)+'\n')
		readthat=open(home+'/.aips/RUN/E2'+userid+'.'+userid)	
		for line in readthat:
			writethat.write(line)
		readthat.close()	

		writethat.write('kleenex \n')
		writethat.write('XXX \n')
		writethat.close()




		p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
		time.sleep(60)
		p[j].communicate()
	for k in range(lenfiles):	
		
		p[k].communicate()

	nsigma=nsigma-3.5


	
for j in indices:
	num4=num3+j
	
	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid

	if choice==2:
		execfile(home+'/.boxfiles/flagfilegenerator_'+userid+'.py')

p=[]
write=[None]*lenfiles
read=[None]*lenfiles	
if choice==2:
	for j in indices:
	
		
		num4=num3+j
		userid = base_repr(num4, 36)
		if (len(userid)==1) and not (len(userid)>=3):
			userid= '00'+userid
		else:
			userid= '0'+userid
	

		
		writethat = open(''+outputfolder+'/socode.sh',"w")
		writethat.write(' \n')
	
		writethat.write('#!/bin/sh \n')

		if os.path.exists(home+'/.bashrc'):
			writethat.write('. ~/.bashrc \n')
	
		
		writethat.write('export BOX='+home+'/.boxfiles'+'\n')
		writethat.write('export OUT='+outputfolder+'\n')
		writethat.write('export INP='+outfolder+'\n')
		writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
		if os.path.exists(home+'/runme'):
			writethat.write('. ~/runme \n')
		writethat.write('aips notv pr=1 << XXX \n')
		writethat.write(str(num4)+'\n')
		readthat=open(home+'/.aips/RUN/E2'+userid+'.'+userid)	
		for line in readthat:
			writethat.write(line)
		readthat.close()	

		writethat.write('kleenex \n')
		writethat.write('XXX \n')
		writethat.close()



		p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
		time.sleep(60)
		p[j].communicate()
for k in p:	
	k.communicate()




for j in range(lenfiles):
	
	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid
	if j in indices:
		nsigma=2.5
	else:
		nsigma=3		
	if choice==2:
		execfile(home+'/.boxfiles/flagfilegenerator_'+userid+'.py')
	


p=[]
write=[None]*lenfiles
read=[None]*lenfiles
for j in range(lenfiles):
	name1=files[j]
	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid



	

	writethat = open(''+outputfolder+'/socode.sh',"w")
	writethat.write(' \n')

	writethat.write('#!/bin/sh \n')

	if os.path.exists(home+'/.bashrc'):
		writethat.write('. ~/.bashrc \n')

	
	writethat.write('export BOX='+home+'/.boxfiles'+'\n')
	writethat.write('export OUT='+outputfolder+'\n')
	writethat.write('export INP='+outfolder+'\n')
	writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
	if os.path.exists(home+'/runme'):
		writethat.write('. ~/runme \n')
	writethat.write('aips notv pr=1 << XXX \n')
	writethat.write(str(num4)+'\n')
	readthat=open(home+'/.aips/RUN/E3'+userid+'.'+userid)	
	for line in readthat:
		writethat.write(line)
	readthat.close()	

	writethat.write('kleenex \n')
	writethat.write('XXX \n')
	writethat.close()


	p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
	time.sleep(60)
	p[j].communicate()



	fin = open(folder+name1)
	line=fin.readlines()[0]
	npols=int(line[line.find('NAXIS3')+29:line.find('NAXIS3')+30])
	fin.close()
	if npols==4:
		execfile(home+'/.boxfiles/flagfilegeneratorpd_'+userid+'.py')



for k in p:	
	k.communicate()


p=[]
write=[None]*lenfiles
read=[None]*lenfiles
ind=0
for j in range(lenfiles):
	name1=files[j]
	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid



	

	fin = open(folder+name1)
	line=fin.readlines()[0]
	npols=int(line[line.find('NAXIS3')+29:line.find('NAXIS3')+30])
	if npols==4:
		writethat = open(''+outputfolder+'/socode.sh',"w")
		writethat.write(' \n')

		writethat.write('#!/bin/sh \n')

		if os.path.exists(home+'/.bashrc'):
			writethat.write('. ~/.bashrc \n')

		
		writethat.write('export BOX='+home+'/.boxfiles'+'\n')
		writethat.write('export OUT='+outputfolder+'\n')
		writethat.write('export INP='+outfolder+'\n')
		writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
		if os.path.exists(home+'/runme'):
			writethat.write('. ~/runme \n')
		writethat.write('aips notv pr=1 << XXX \n')
		writethat.write(str(num4)+'\n')
		readthat=open(home+'/.aips/RUN/E3A'+userid+'.'+userid)	
		for line in readthat:
			writethat.write(line)
		readthat.close()	

		writethat.write('kleenex \n')
		writethat.write('XXX \n')
		writethat.close()


		p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
		time.sleep(60)
		p[ind].communicate()

		ind=ind+1

		fin.close()
	

for k in p:	
	k.communicate()



p=[]
write=[None]*lenfiles
read=[None]*lenfiles		


for j in range(lenfiles):
	if choice==2:

		default(importuvfits)
		fitsfile=outputfolder+'/im/delme'+str(j+1)+'.fits'
		vis=outputfolder+'/im/delme'+str(j+1)+'.ms'
		importuvfits()
		tb.open(outputfolder+'/im/delme'+str(j+1)+'.ms'+'/FIELD')
		field_names=tb.getcol('NAME')
		tb.close()

		jj=0   
		flagg=1
		
		for l in field_names:
			if (l.find('_')==-1):
				flagg=flagg*0.0  # to make sure 'the underscore is not genuiely in the name'
				
			jj=jj+1	
		
		
		jj=0     
		for l in field_names:
			if (l.find('_')>-1) and flagg==1:
				field_names[jj]=field_names[jj][:-field_names[jj][::-1].find('_')].rstrip('_')
				#field_names[j]=field_names[j].rstrip('_')
			jj=jj+1	



		tb.open(outputfolder+'/im/delme'+str(j+1)+'.ms'+'/FIELD',nomodify=False)
		tb.putcol('NAME',field_names)
		tb.close()

		os.system('rm -rf '+outputfolder+'/im/delme'+str(j+1)+'.fits')
		default(flagdata)
		vis=outputfolder+'/im/delme'+str(j+1)+'.ms'
		action='apply'
		mode='rflag'
		field='' 
		extendflags=False
		flagdata()
		default(flagdata)
		vis=outputfolder+'/im/delme'+str(j+1)+'.ms'
		extendflags=False
		action='apply'
		mode='tfcrop'
		flagdata()

		default(exportuvfits)
		fitsfile=outputfolder+'/im/delme'+str(j+1)+'.fits'
		writestation=False
		vis=outputfolder+'/im/delme'+str(j+1)+'.ms'
		exportuvfits()
		os.system('rm -rf '+outputfolder+'/im/delme'+str(j+1)+'.ms*')








p=[]
write=[None]*lenfiles
read=[None]*lenfiles
for j in range(lenfiles):

	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid



	
	writethat = open(''+outputfolder+'/socode.sh',"w")
	writethat.write(' \n')

	writethat.write('#!/bin/sh \n')

	if os.path.exists(home+'/.bashrc'):
		writethat.write('. ~/.bashrc \n')

	
	writethat.write('export BOX='+home+'/.boxfiles'+'\n')
	writethat.write('export OUT='+outputfolder+'\n')
	writethat.write('export INP='+outfolder+'\n')
	writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
	if os.path.exists(home+'/runme'):
		writethat.write('. ~/runme \n')
	writethat.write('aips notv pr=1 << XXX \n')
	writethat.write(str(num4)+'\n')
	readthat=open(home+'/.aips/RUN/E4'+userid+'.'+userid)	
	for line in readthat:
		writethat.write(line)
	readthat.close()	

	writethat.write('kleenex \n')
	writethat.write('XXX \n')
	writethat.close()





	p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))
	time.sleep(60)
	p[j].communicate()
for k in p:	
	k.communicate()








p=[]
write=[None]*lenfiles
read=[None]*lenfiles		

for m in range(max(linescript)):
	p=[None]*lenfiles
	write=[None]*lenfiles
	read=[None]*lenfiles	


	for j in range(lenfiles):
		if linescript[j]>m:
			
			num4=num3+j
			userid = base_repr(num4, 36)
				#print y
			if (len(userid)==1) and not (len(userid)>=3):
				userid= '00'+userid
				#print y
			else:
				userid= '0'+userid
				#print userid 
		



			

			writethat = open(''+outputfolder+'/socode.sh',"w")
			writethat.write(' \n')
		
			writethat.write('#!/bin/sh \n')

			if os.path.exists(home+'/.bashrc'):
				writethat.write('. ~/.bashrc \n')
		
			
			writethat.write('export BOX='+home+'/.boxfiles'+'\n')
			writethat.write('export OUT='+outputfolder+'\n')
			writethat.write('export INP='+outfolder+'\n')
			writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
			if os.path.exists(home+'/runme'):
				writethat.write('. ~/runme \n')
			writethat.write('aips notv pr=1 << XXX \n')
			writethat.write(str(num4)+'\n')
			readthat=open(home+'/.aips/RUN/E'+userid+str(m+1)+'.'+userid)	
			for line in readthat:
				writethat.write(line)
			readthat.close()	
		
			writethat.write('kleenex \n')
			writethat.write('XXX \n')
			writethat.close()


		
	
		
		
			p[j]=subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True)
			
			poll=p[j].poll()
			timestamp=15.*60.
			scaled=filesize/1e10
			for ij in range(288):
				time.sleep(scaled*timestamp)
				if not poll==None:
					break
				elif (ij+1)%96==0:
					writethat = open(''+outputfolder+'/socode_del.sh',"w")
					writethat.write(' \n')
					writethat.write('#!/bin/sh \n')
					if os.path.exists(home+'/.bashrc'):
						writethat.write('. ~/.bashrc \n')
					writethat.write('export BOX='+home+'/.boxfiles'+'\n')
					writethat.write('export OUT='+outputfolder+'\n')
					writethat.write('export INP='+outfolder+'\n')
					writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
					if os.path.exists(home+'/runme'):
						writethat.write('. ~/runme \n')
					writethat.write('aips notv pr=1 << XXX \n')
					writethat.write(str(num4)+'\n')
					readthat=open(home+'/.aips/RUN/SP'+userid+'.'+userid)	
					for line in readthat:
						writethat.write(line)
					readthat.close()	
					writethat.write('kleenex \n')
					writethat.write('XXX \n')
					writethat.close()
					stpsubp=subprocess.Popen(['. '+outputfolder+'/socode_del.sh'],stdout=f,stdin=None,shell=True)
					stpsubp.communicate()
			if ij==287:
				my_timer = Timer(5, kill, [p[j]])
				my_timer.cancel()
			os.system('rm -rf'+outputfolder+'/socode_del.sh')	
			p[j].communicate()
			time.sleep(60)

	for k in range(lenfiles):
		if linescript[k]>m:	
			p[k].communicate()


p=[]
j=0
for m in range(max(linescript)):
	for k in range(lenfiles):
		if linescript[k]>m:	
			if filetype[k]==1:
				num4=num3+k
				execfile(home+'/.boxfiles/clean0_'+str(num4)+'_'+str(m+1)+'.py')
				j=j+1

p=[]
write=[None]*lenfiles
read=[None]*lenfiles
for j in range(lenfiles):
	
	num4=num3+j
	userid = base_repr(num4, 36)
	if (len(userid)==1) and not (len(userid)>=3):
		userid= '00'+userid
	else:
		userid= '0'+userid

	writethat = open(''+outputfolder+'/socode.sh',"w")
	writethat.write(' \n')

	writethat.write('#!/bin/sh \n')

	if os.path.exists(home+'/.bashrc'):
		writethat.write('. ~/.bashrc \n')

	
	writethat.write('export BOX='+home+'/.boxfiles'+'\n')
	writethat.write('export OUT='+outputfolder+'\n')
	writethat.write('export INP='+outfolder+'\n')
	writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
	if os.path.exists(home+'/runme'):
		writethat.write('. ~/runme \n')
	writethat.write('aips notv pr=1 << XXX \n')
	writethat.write(str(num4)+'\n')
	readthat=open(home+'/.aips/RUN/LOGS'+userid+'.'+userid)	
	for line in readthat:
		writethat.write(line)
	readthat.close()	

	writethat.write('kleenex \n')
	writethat.write('XXX \n')
	writethat.close()

	p.append(subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True))

	time.sleep(60)
	p[j].communicate()
for k in range(lenfiles):	
	p[k].communicate()



if weighting == 'briggs':

	p=[]
	write=[None]*lenfiles
	read=[None]*lenfiles		
	if choice==2:
		for m in range(max(linescript)):
			p=[None]*lenfiles
			write=[None]*lenfiles
			read=[None]*lenfiles		
			for j in range(lenfiles):
				if filetype[j]==1 and linescript[j]>m:
					
					
					num4=num3+j
					userid = base_repr(num4, 36)
					if (len(userid)==1) and not (len(userid)>=3):
						userid= '00'+userid
					else:
						userid= '0'+userid
				
	
					writethat = open(''+outputfolder+'/socode.sh',"w")
					writethat.write(' \n')
				
					writethat.write('#!/bin/sh \n')
				
					if os.path.exists(home+'/.bashrc'):
						writethat.write('. ~/.bashrc \n')
				
					
					writethat.write('export BOX='+home+'/.boxfiles'+'\n')
					writethat.write('export OUT='+outputfolder+'\n')
					writethat.write('export INP='+outfolder+'\n')
					writethat.write('export RUNFIL=~/.aips/RUN'+'\n')
					if os.path.exists(home+'/runme'):
						writethat.write('. ~/runme \n')
					writethat.write('aips notv pr=1 << XXX \n')
					writethat.write(str(num4)+'\n')
					readthat=open(home+'/.aips/RUN/SCRIPT'+str(m+1)+'.'+userid)	
					for line in readthat:
						writethat.write(line)
					readthat.close()	
				
					writethat.write('kleenex \n')
					writethat.write('XXX \n')
					writethat.close()
				
				
				
				
				
					p[j]=subprocess.Popen(['. '+outputfolder+'/socode.sh'],stdout=f,stdin=None,shell=True)
					time.sleep(60)
	
	



writethat = open(outputfolder+'/commands',"w")
writethat.write(' \n')
writethat.write('export BOX=~/.boxfiles'+'\n')
writethat.write('export OUT='+outputfolder+'\n')

writethat.write('export INP='+outfolder+'\n')
writethat.write('export RUNFIL=~/.aips/RUN'+'\n')

writethat.write('aips notv'+'\n')


for j in range(lenfiles):
	num4=num3+j
	writethat.write(str(num3+j)+'\n')
	writethat.write("run scrpt"+'\n')
	writethat.write("run s2"+userid+"\n")
	writethat.write("run s3"+userid+"\n")
	writethat.write("run s4"+userid+"\n")
	for m in range(max(linescript)):
		if linescript[j]>m:
			writethat.write("run s5"+str(m+1)+'\n')
			writethat.write("run zap"+'\n')
			writethat.write("restart"+'\n')
	if 1 in filetype:	
		for j in range(lenfiles):
			num4=num3+j	
			writethat.write(r"execfile('"+home+'/.boxfiles/clean_'+str(num4)+".py')"+'\n')
		for j in range(lenfiles):
			num4=num3+j
			writethat.write(str(num4)+'\n')
			writethat.write('restart'+'\n')
writethat.close()

os.system('rm -rf '+outputfolder+'/im/delme*')
os.system('rm -rf ~/.boxfiles')
f.close()