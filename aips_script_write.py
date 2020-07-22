calprm7=0
calprm9=0
calprm7=0
calprm9=0
execfile(pipepath+'input.py')
from numpy import base_repr

os.system('mkdir /temp30/temp')
os.system('mkdir /temp30/temp/ASTRO5_1')
os.system('touch /temp30/temp/ASTRO5_1/SPACE')
if (channels[0]>1000):
    nplo = 6
else:
    nplo = 10


standard_source_names = [ '3C48', '3C147', '3C286']
two_band=[43, 61, 25.49]# yet to get for 3c468.1
p_band=[42.00, 52.30, 26.00]
l_band=[15.9, 22.3, 15.14]# yet to get
band2=[55.00,58.5,15.0]
m_band=[29.21, 36.00, 22.02 ]# yet to get for 3c468.1
freq = center_frequencies[0]/1e08
if (spw_bandwidths[0]<1000):
    spw_bandwidths[0]=spw_bandwidths[0]*1e6
fracband=spw_bandwidths[0]/center_frequencies[0]
chanwidth=spw_bandwidths[0]/channels[0]
firstchan=channels[0]/2-25 
lastchan=channels[0]/2+25
if firstchan<0:
    firstchan=1 
if lastchan>channels[0]: 
    lastchan=0 
if fracband<0.12:
    filetype.append(0)
else:
    filetype.append(1)
#freq_cl=1
meanlevel=[None]*100
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    j=0
    for k in standard_source_names:
        j=j+1
        if (field_names[y].find(k)>-1):
            #print k
            #print y
            if (freq<1.9):
                meanlevel[y]=band2[j-1]
                field_lim=250
            elif (1.9<freq<2.8):
                meanlevel[y]=two_band[j-1]
                field_lim=200
            elif (2.8<freq<4.6):
		if not usefreq_cl=='y':
                	freq_cl=3
		field_lim=160
                meanlevel[y]=p_band[j-1]        
            elif (4.6<freq<9.3):
		if not usefreq_cl=='y':		
                	freq_cl=2
                field_lim=100
                meanlevel[y]=m_band[j-1]  
            elif (9.3<freq<15):
                calprm7=3
		if not usefreq_cl=='y':		
                	freq_cl=4
                calprm9=1
                meanlevel[y]=l_band[j-1]        
                field_lim=50 



userid = base_repr(num, 36)
    #print y
if (len(userid)==1) and not (len(userid)>=3):
    userid= '00'+userid
    #print y
else:
    userid= '0'+userid
    #print userid 

fivepctch=int(0.03125*channels[0])
begch=fivepctch
endch=channels[0]-fivepctch

if (fivepctch < 3):
    begch=4
    endch=channels[0]-3
if (fivepctch > 20):
    begch=21
    endch=channels[0]-20

if (freq<1.9):
    sens=615.0/(0.33*(chanwidth*median_integration_time)**0.5)
    pbcoeff=[1, -3.366e-3, 46.159e-7,-29.963e-10,7.529e-13 ]
    pba=-3.366
    pbb=46.159
    pbc=-29.963
    pbd=7.529

    #chav=int(channels[0]/BBC_bandwidths[0]*0.25e6)
    uvlow='0.6'
    mf=30
elif (1.9<freq<2.8):
    sens=237.0/(0.33*(chanwidth*median_integration_time)**0.5)
    pbcoeff=[1, -3.366e-3, 46.159e-7,-29.963e-10,7.529e-13 ]
    pba=-3.366
    pbb=46.159
    pbc=-29.963
    pbd=7.529
    #chav=int(channels[0]/BBC_bandwidths[0]*0.35e6)
    uvlow='0.8'
    mf=24
elif (2.8<freq<4.6):
    sens= 106.0/(0.32*(chanwidth*median_integration_time)**0.5)
    uvlow='1'
    #chav=int(channels[0]/BBC_bandwidths[0]*0.5e6)
    pbcoeff=[1, -2.9061046e-3, 33.13585706e-7,  -17.23287036e-10,   3.45117443e-13 ]
    pba=-3.397
    pbb=47.192
    pbc=-30.931
    pbd=7.803
    mf=18
elif (4.6<freq<9.3):
    sens=102.0/(0.32*(chanwidth*median_integration_time)**0.5)
    pbcoeff=[1, -3.486e-3, 47.749e-7,-35.203e-10,10.399e-13 ]
    uvlow='3'
    #chav=int(channels[0]/BBC_bandwidths[0]*0.875e6)
    pba=-3.486
    pbb=47.749
    pbc=-35.203
    pbd=10.399
    mf=12
    
elif (9.3<freq<15):
    sens=73.0/(0.22*(chanwidth*median_integration_time)**0.5)
    pbcoeff=[1, -2.61055647e-3,24.37461198e-7,-9.44716181e-10, 1.29148631e-13]
    uvlow='5'
    pba=-2.27961
    pbb=21.4611
    pbc=-9.7929
    pbd=1.80153
    mf=10
    #chav=int(channels[0]/BBC_bandwidths[0]*1.25e6)
pb=4.4/freq
chav =[]
chav1=[]    
chavgw=[]
for i in range(1,notarg+1):
    chav.append(int(0.5*synth_beam[i-1]*(center_frequencies[0]-spw_bandwidths[0]/2)/pb/chanwidth/3600.0))
    chav1.append(int((endch-begch)/chav[i-1]+1))
    if fracband>0.12:
        chavgw.append(int((chav1[i-1])/freq_cl))
ch = -begch+endch+1
syscommand='rm -rf '+home+'/.aips/RUN/E1'+userid+'.'+userid
os.system(syscommand)

if not usemidchan=='y':
	midchan=channels[0]/2-13
	
	rmsvalue=[]
	for i in range(midchan,midchan+26):
	   default(visstat)
	   spw='0:'+str(i)+'~'+str(i)
	   vis=ms_active
	   x=str(flux_fiel[0])
	   field=x
	   p=visstat()
	   rmsvalue.append(p['DATA_DESC_ID=0']['stddev'])
	
	midchan=midchan+rmsvalue.index(min(rmsvalue))




    
niter=20000*(14/freq)**0.4 
clip=100*(14/freq)


writethat = open(home+'/.aips/RUN/CALB.'+userid,"w")
writethat.write('$ \n')



writethat.write('getn 1 \n \n')
writethat.write("inext 'cl' \n")    
writethat.write('extd \n')
writethat.write("inext 'sn' \n")    
writethat.write('extd \n')
writethat.write("clrmsg \n")

writethat.write("tget calib \n")
writethat.write('getn 1 \n \n')
writethat.write('dowait true \n')
writethat.write('dowait true \n')
writethat.write('dowait true \n')
writethat.write('go calib; wait calib ; end\n\n')
if not (flux_field==phase_field) and not (phase_field==[]):
    writethat.write("tget clcal \n")
    writethat.write('getn 1 \n \n')
    writethat.write("source ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("calsour ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('dowait true \n')
    writethat.write('dowait true \n')
    writethat.write('go clcal; wait clcal; end \n\n')
    
    writethat.write("tget getjy \n")
    writethat.write('getn 1 \n \n')
    writethat.write('dowait true \n')
    writethat.write('go getjy; wait getjy; end \n\n')
    
    writethat.write("inext 'cl' \n")    
    writethat.write('extd \n')

writethat.write("tget clcal \n")
writethat.write('getn 1 \n \n')
writethat.write("source ''\n")
writethat.write("calso ")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    writethat.write("'"+field_names[y]+"'")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('dowait true \n')
writethat.write('go clcal; wait clcal; end \n\n')


writethat.close()

npols=2
flag=0
fin = open(outputfolder+"/"+name1[:-5]+".listobs")
lines=fin.readlines()
count=0
for line in lines:
    if 'Corrs' in line: 
        flag=1
    if 'RL' in line and 'LR' in line and flag==1:
        npols=4
        break

fin.close()



writethat = open(home+'/.aips/RUN/STOP.'+userid,"w")
writethat.write('$ \n')
writethat.write("OPTELL     'CHAN'      \n")
writethat.write("TASK       'IMAGR'     \n")
writethat.write("NUMTELL       "+str(pr)+"       \n")
writethat.write("tell imagr niter 0 \n")
writethat.write("tell imagr niter 0 \n")
writethat.write("tell imagr niter 0 \n")

writethat.close()



writethat = open(home+'/.aips/RUN/E1'+userid+'.'+userid,"w")
writethat.write('$ \n')
writethat.write("task 'fitld' \n")
writethat.write('default \n')
writethat.write("datain 'INP:"+name1+"\n")
writethat.write('dowait true \n')
writethat.write('go fitld; wait fitld; end \n \n')

writethat.write('dowait true \n')
writethat.write('dowait true \n')

writethat.write("task 'indxr' \n")
writethat.write('getn 1 \n')
writethat.write('cparm 0 0 0.5 0 \n')
writethat.write('dowait true \n')
writethat.write('go indxr; wait indxr; end \n \n')



writethat.write("task 'listr' \n")
writethat.write('getn 1 \n')
writethat.write("optype  'scan' \n")
writethat.write("docrt -1 \n")
writethat.write("optype  'scan' \n")
writethat.write("OUTPRINT   'OUT:"+name1+".listr \n")
writethat.write('dowait true \n')
writethat.write('go listr; wait listr; end \n \n')



writethat.write("task 'quack' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('dowait true \n')
writethat.write('go quack; wait quack; end \n \n')

writethat.write("clrmsg \n")

writethat.write("task 'uvflg' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("bchan 1 \n")
writethat.write("echan "+str(begch)+" \n")
writethat.write('outfgver 1 \n')
writethat.write('dowait true \n')
writethat.write('go uvflg; wait uvflg; end \n \n')

writethat.write("task 'uvflg' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("bchan "+str(endch)+" \n")
writethat.write("echan 0 \n")
writethat.write('outfgver 1 \n')
writethat.write('dowait true \n')
writethat.write('go uvflg; wait uvflg; end \n \n')
 
if useflagfile=='y':
    writethat.write("task 'uvflg' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("intext '"+flagfile+" \n")  
    writethat.write('outfgver 1 \n')
    writethat.write('go uvflg; wait uvflg; end \n \n')
 

 
writethat.write("task 'setjy' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("optype 'calc' \n")
writethat.write("source ")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")

writethat.write("'\n")
writethat.write('dowait true \n')
writethat.write('go setjy; wait setjy; end \n\n')



writethat.write("task 'calib' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
writethat.write("calsour ")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('solint 1\n')
writethat.write("soltype 'L1R'"'\n')
writethat.write('uvrange '+uvlow+' 0\n')
writethat.write('refant '+refAnt+'\n')
writethat.write('dowait true \n')
writethat.write('go calib; wait calib ; end\n\n')

if not (flux_field==phase_field) and not (phase_field==[]):


    writethat.write("task 'clcal' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("source ")
    
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("calso ")
    
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write("OPCODE 'cali' \n")
    writethat.write("SAMPTYPE 'mwf' \n")
    writethat.write('dowait true \n')
    writethat.write('go clcal; wait clcal; end \n\n')
    
    writethat.write("task 'getjy' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("source ")
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write("calsour ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go getjy; wait getjy; end \n\n')
    
    writethat.write("inext 'cl' \n")    
    writethat.write('extd \n')




writethat.write("task 'clcal' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("source '' \n")
writethat.write("calso ")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    writethat.write("'"+field_names[y]+"'")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")

writethat.write("OPCODE 'cali' \n")
writethat.write("SAMPTYPE 'mwf' \n")
writethat.write('dowait true \n')
writethat.write('go clcal; wait clcal; end \n\n')


writethat.write("task 'prtab' \n")
writethat.write("default \n")
writethat.write("getn 1 \n")
writethat.write("inext 'su' \n")
writethat.write("docrt -1 \n")
writethat.write("OUTPRINT   'OUT:"+name1+".fluxes \n")
writethat.write('dowait true \n')
writethat.write('go prtab; wait prtab; end \n\n')




writethat.write("task 'clip' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("source '' \n")
writethat.write("docal 1 \n")
writethat.write("outfgver 1\n")
writethat.write('aparm 1000 0 0 0 \n')
writethat.write('dowait true \n')
writethat.write('go clip; wait clip; end \n\n')


writethat.write("task 'clip' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("docal 1 \n")
writethat.write("source ")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write("outfgver 1\n")

writethat.write('aparm 1000 0 0.001 0 \n')
writethat.write('dowait true \n')
writethat.write("stokes 'll' \n")
writethat.write('go clip; wait clip; end \n\n')
writethat.write("stokes 'rr' \n")
writethat.write('go clip; wait clip; end \n\n')


if fracband>0.12:
    writethat.write("task 'uvcop' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("flagver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go uvcop; wait uvcop; end\n \n')
    writethat.write('getn 1 ;clrstat; zap; recat \n \n')
    writethat.write('getn 1 \n \n')

for loopn in range(5):

    writethat.write("inext 'cl' \n")    
    writethat.write('extd \n')
    writethat.write("inext 'sn' \n")    
    writethat.write('extd \n')
    writethat.write("clrmsg \n")
    
    writethat.write("tget calib \n")
    writethat.write('getn 1 \n \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib ; end\n\n')
    if not (flux_field==phase_field) and not (phase_field==[]):
        writethat.write("tget clcal \n")
        writethat.write('getn 1 \n \n')
        writethat.write("source ")
        for i in range(1,noflux+1):
            x=(flux_fiel[i-1])
            y=int(x)    
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("calsour ")
        for i in range(1,noflux+1):
            x=(flux_fiel[i-1])
            y=int(x)    
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('dowait true \n')
        writethat.write('go clcal; wait clcal; end \n\n')
        
        writethat.write("tget getjy \n")
        writethat.write('getn 1 \n \n')
        writethat.write('dowait true \n')
        writethat.write('go getjy; wait getjy; end \n\n')
        
        writethat.write("inext 'cl' \n")    
        writethat.write('extd \n')
    
    writethat.write("tget clcal \n")
    writethat.write('getn 1 \n \n')
    writethat.write("source ''\n")
    writethat.write("calso ")
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        writethat.write("'"+field_names[y]+"'")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go clcal; wait clcal; end \n\n')
    
    
    
    for i in range(1,noflux+1):
    #    writethat.write("compress \n")
    #    writethat.write("compress \n")
        writethat.write("task 'clip' \n")
            
        writethat.write('default \n')
        writethat.write("outfgver 1 \n")
        writethat.write('getn 1 \n')
        writethat.write('bchan '+str(midchan)+' \n')
        writethat.write('echan '+str(midchan)+' \n') 
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        cliplevel1= meanlevel[y]+100*sens/1.3**loopn
        cliplevel2=meanlevel[y]-100*sens/1.3**loopn
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")

    
        writethat.write('docal 1 \n')
        #writethat.write('doband 3 \n')
        #writethat.write('bpver 0 \n')
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write('dowait true \n')
        writethat.write("stokes 'll' \n")
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')

    writethat.write("task 'clip' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write('bchan '+str(midchan)+' \n')
    writethat.write('echan '+str(midchan)+' \n') 
    writethat.write("source ")
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    #writethat.write("stokes 'rrll' \n")
    writethat.write("'\n")
    writethat.write("docal 1 \n")
    writethat.write('aparm '+str(10*mf*sens)+' 0 \n')
    writethat.write("outfgver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go clip; wait clip; end\n \n')


#writethat.write("inext 'cl' \n")    
#writethat.write('extd \n')
#writethat.write("inext 'sn' \n")    
#writethat.write('extd \n')
#writethat.write("clrmsg \n")

writethat.write("task 'snflg' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('dparm(8)=1 \n')
writethat.write("optype 'a&p' \n")
writethat.write("inext 'sn' \n")
#writethat.write("outfgver 1 \n")
writethat.write('dowait true \n')
writethat.write('go snflg; wait snflg; end\n \n')


writethat.write('getn 1  \n')
writethat.write("inext 'sn' \n")
writethat.write("extd \n")
writethat.write("inext 'cl' \n")
writethat.write("extd \n")

writethat.write("tget calib \n")
writethat.write('dowait true \n')
writethat.write('doflag 5 \n')
writethat.write("go calib ; wait calib\n")



#writethat.write("tget calib \n")
#writethat.write('getn 1 \n \n')
#writethat.write('dowait true \n')
#writethat.write('go calib; wait calib ; end\n\n')





if not (flux_field==phase_field) and not (phase_field==[]):
    writethat.write("tget clcal \n")
    writethat.write('getn 1 \n \n')
    writethat.write("source ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("calsour ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go clcal; wait clcal; end \n\n')
    
    writethat.write("tget getjy \n")
    writethat.write('getn 1 \n \n')
    writethat.write('dowait true \n')
    writethat.write('go getjy; wait getjy; end \n\n')
    
    writethat.write("inext 'cl' \n")    
    writethat.write('extd \n')

writethat.write("tget clcal \n")
writethat.write('getn 1 \n \n')
writethat.write("source ''\n")
writethat.write("calso ")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    writethat.write("'"+field_names[y]+"'")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('dowait true \n')
writethat.write('go clcal; wait clcal; end \n\n')


for i in range(1,noflux+1):
    writethat.write("task 'bpass' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write('docal -1 \n')
    writethat.write("inext '' \n")
    writethat.write('inver 0 \n')
    writethat.write('outver 1 \n')    
    writethat.write('bpassprm(10) 3 \n')
    writethat.write('bpassprm(5) 1 \n')
    writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("soltyp 'L1R'    \n")       
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')

writethat.write("task 'flgit' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("source ")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('aparm 100 '+str(mf*sens)+' '+str(mf*sens)+' 0 \n')
writethat.write("outfgver 3 \n")
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
writethat.write('go flgit; wait flgit; end\n \n')

writethat.write("task 'uvcop' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("flagver 3 \n")
writethat.write('dowait true \n')
writethat.write('go uvcop; wait uvcop; end\n \n')
writethat.write('getn 1 ;clrstat; zap; recat \n \n')
writethat.write('getn 1 \n \n')


writethat.write("inext 'bp' \n")
writethat.write("extd \n")

for i in range(1,noflux+1):
    writethat.write("task 'bpass' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write('docal -1 \n')
    writethat.write("inext '' \n")
    writethat.write('inver 0 \n')
    writethat.write('outver 1 \n')    
    writethat.write('bpassprm(10) 3 \n')
    writethat.write('bpassprm(5) 1 \n')
    writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("soltyp 'L1R'    \n")       
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')



for i in range(1,noflux+1):
    writethat.write("task 'clip' \n")
        
    writethat.write('default \n')
    writethat.write("outfgver 1 \n")
    writethat.write('getn 1 \n')
    writethat.write("source ")
    x=(flux_fiel[i-1])
    y=int(x)
    cliplevel1= meanlevel[y]+100*sens
    cliplevel2=meanlevel[y]-100*sens
    if (cliplevel2<0):
        cliplevel2=1
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
        
    writethat.write('docal 1 \n')
    writethat.write('doband 3 \n')
    writethat.write('bpver 0 \n')
    

    writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
    writethat.write('dowait true \n')
    writethat.write("stokes 'll' \n")
    writethat.write('go clip; wait clip; end \n\n')
    writethat.write("stokes 'rr' \n")
    writethat.write('go clip; wait clip; end \n\n')
    if fracband>0.12:
        writethat.write("task 'uvcop' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write("flagver 1 \n")
        
        writethat.write('dowait true \n')
        writethat.write('go uvcop; wait uvcop; end\n \n')
        writethat.write('getn 1 ;clrstat; zap; recat \n \n')
        writethat.write('getn 1 \n \n')




writethat.write("inext 'bp' \n")
writethat.write("extd \n")

for i in range(1,noflux+1):
    writethat.write("task 'bpass' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write('docal -1 \n')
    writethat.write("inext '' \n")
    writethat.write('inver 0 \n')
    writethat.write('outver 1 \n')    
    writethat.write('bpassprm(10) 3 \n')
    writethat.write('bpassprm(5) 1 \n')
    writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("soltyp 'L1R'    \n")       
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')




if fracband<0.12:
    writethat.write("clrmsg \n")
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        cliplevel1= meanlevel[y]+80*sens
        cliplevel2=meanlevel[y]-80*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("outfgver 1 \n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')
    
    
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("outfgver 1 \n")
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        
        cliplevel1= meanlevel[y]+70*sens
        cliplevel2= meanlevel[y]-70*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')
        
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("outfgver 1 \n")
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
          
        cliplevel1= meanlevel[y]+60*sens
        cliplevel2=meanlevel[y]-60*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')

if fracband>0.12:
    writethat.write("clrmsg \n")
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        cliplevel1= meanlevel[y]+100*sens
        cliplevel2=meanlevel[y]-100*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("outfgver 1 \n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')
    
    
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("outfgver 1 \n")
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        
        cliplevel1= meanlevel[y]+100*sens
        cliplevel2= meanlevel[y]-100*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')
    
    for i in range(1,noflux+1):
        writethat.write("tget clip \n")
        writethat.write('getn 1 \n \n')
        writethat.write("outfgver 1 \n")
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
          
        cliplevel1= meanlevel[y]+100*sens
        cliplevel2=meanlevel[y]-100*sens
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write("stokes 'll' \n")
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'rr' \n")
        writethat.write('go clip; wait clip; end \n\n')
    
    writethat.write("inext 'bp' \n")
    writethat.write("extd \n")
    
    for i in range(1,noflux+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')



writethat.write("task 'clip' \n")
writethat.write('default \n')
writethat.write("outfgver 1 \n")
writethat.write('getn 1 \n')
writethat.write("source ")
for i in range(1,notarg+1):
    x=(target_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('bpver 0 \n')
writethat.write('aparm '+str(clip)+' 0 \n')#individual

writethat.write('dowait true \n')
writethat.write('go clip; wait clip; end \n\n')

if fracband>0.12:
    writethat.write("task 'uvcop' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("flagver 1 \n")

    writethat.write('dowait true \n')
    writethat.write('go uvcop; wait uvcop; end\n \n')
    writethat.write('getn 1 ;clrstat; zap; recat \n \n')
    writethat.write('getn 1 \n \n')


writethat.write("task 'flgit' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write("source ")
for i in range(1,notarg+1):
    x=(target_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write("uvrange "+uvlow+" 0 \n")
writethat.write('aparm 1000 '+str(mf*sens)+' '+str(mf*sens)+' 0 \n')
writethat.write("outfgver 1 \n")
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
writethat.write('go flgit; wait flgit; end\n \n')

if fracband>0.12:
    writethat.write("task 'uvcop' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write("flagver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go uvcop; wait uvcop; end\n \n')
    writethat.write('getn 1 ;clrstat; zap; recat \n \n')
    writethat.write('getn 1 \n \n')




writethat.write("task 'flagr' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('outfgver 1 \n')
    

writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
#if fracband>0.12:
if useflagr_aips=='y':
	writethat.write('go flagr; wait flagr; end\n \n')




writethat.write("task 'rflag' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('outfgver 1 \n')
writethat.write('uvrange '+uvlow+' 0     \n')       
writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20  \n")
writethat.write("NOISE "+str(mf*sens)+" \n")
writethat.write("SCUTOFF "+str(10*mf*sens)+" \n")
writethat.write("STOKE 'RR' \n")
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
#if fracband>0.12:
if userflag_aips=='y':
	writethat.write('go rflag; wait rflag; end\n \n')

writethat.write("task 'rflag' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('outfgver 1 \n')
writethat.write('uvrange '+uvlow+' 0     \n')       
writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20 \n")
writethat.write("NOISE "+str(mf*sens)+" \n")
writethat.write("SCUTOFF "+str(10*mf*sens)+" \n")
writethat.write("STOKE 'LL' \n")
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
#if fracband>0.12:
if userflag_aips=='y':
	writethat.write('go rflag; wait rflag; end\n \n')



writethat.write("task 'rflag' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('outfgver 1 \n')
writethat.write('uvrange 0 '+uvlow+'    \n')       
writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20  \n")
writethat.write("NOISE "+str(1.5*mf*sens)+" \n")
writethat.write("SCUTOFF "+str(15*mf*sens)+" \n")
writethat.write("STOKE 'RR' \n")
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
#if fracband>0.12:
if userflag_aips=='y':
	writethat.write('go rflag; wait rflag; end\n \n')


writethat.write("task 'rflag' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal 1 \n')
writethat.write('doband 3 \n')
writethat.write('outfgver 1 \n')
writethat.write('uvrange 0 '+uvlow+'      \n')       
writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20 \n")
writethat.write("NOISE "+str(1.5*mf*sens)+" \n")
writethat.write("SCUTOFF "+str(15*mf*sens)+" \n")
writethat.write("STOKE 'LL' \n")
writethat.write('bpver 0 \n')
writethat.write('dowait true \n')
#if fracband>0.12:
if userflag_aips=='y':
	writethat.write('go rflag; wait rflag; end\n \n')






writethat.close()
writethat=open(home+'/.aips/RUN/E2'+userid+'.'+userid,"w")
writethat.write('$\n')


writethat.write("task 'uvflg'\n")
writethat.write("default\n")
writethat.write("getn 1\n")
writethat.write('outfgver 1 \n')
writethat.write("intext 'BOX:FLAG."+userid+"\n")
writethat.write("opcode 'flag'\n")
writethat.write('dowait true \n')
writethat.write("go uvflg; wait uvflg;\n")




writethat.write("inext 'bp' \n")
writethat.write("extd \n")

writethat.write("tget bpass \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('docal -1 \n')
writethat.write("inext '' \n")
writethat.write('inver 0 \n')
writethat.write('outver 1 \n')    
writethat.write('bpassprm(10) 3 \n')
writethat.write('bpassprm(5) 1 \n')
writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
writethat.write('uvrange '+uvlow+' 0     \n')       
writethat.write("soltyp 'L1R'    \n")       
writethat.write('refant '+refAnt+'\n')
writethat.write('tput bpass \n\n')



for i in range(1,noflux+1):
    writethat.write("tget bpass \n")
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')


if nophase==0:
    numm=noflux
    fiel=flux_fiel
else:
    numm=nophase
    fiel=phase_fiel



writethat.write("task 'possm'\n")
writethat.write("default\n")
writethat.write("getn 1\n")
writethat.write("doband 3\n")
writethat.write("bpver 0\n")
writethat.write("docal 1\n")
writethat.write("aparm 0\n")
writethat.write("aparm(1)= -1\n")
writethat.write("nplo 0\n")
writethat.write("stokes 'I' \n")
writethat.write("solin 0\n")
writethat.write("antennas 0\n")
writethat.write("tput possm\n")
    





for i in range(1,noflux+1):
    writethat.write("tget possm\n")
    writethat.write("source ")
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("outtext 'BOX:plot"+field_names[y]+"."+userid+"\n")
    writethat.write('dowait true \n')
    writethat.write("go possm; wait possm\n")
    
    os.system('rm -rf '+home+'/.boxfiles/plot'+field_names[y]+'.'+userid)




for i in range(1,numm+1):
    for lm in range(30):
        writethat.write("tget possm\n")

        writethat.write("source ")
        x=(fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
    
        writethat.write("stokes 'RR' \n")

        writethat.write("outtext 'BOX:plotrr"+field_names[y]+"."+userid+"."+str(lm)+"\n")
        writethat.write("antennas "+str(lm+1)+"\n")
        writethat.write('dowait true \n')
        writethat.write("go possm; wait possm\n")
        
        os.system('rm -rf '+home+'/.boxfiles/plotrr'+field_names[y]+'.'+userid+'.'+str(lm))

for i in range(1,numm+1):
    for lm in range(30):
        writethat.write("task 'possm'\n")
        writethat.write("source ")
        x=(fiel[i-1])
        y=int(x)
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("stokes 'LL' \n")
        writethat.write("outtext 'BOX:plotll"+field_names[y]+"."+userid+"."+str(lm)+"\n")
        writethat.write("antennas "+str(lm+1)+"\n")
        writethat.write('dowait true \n')
        writethat.write("go possm; wait possm\n")
        
        os.system('rm -rf '+home+'/.boxfiles/plotll'+field_names[y]+'.'+userid+'.'+str(lm))

if not nophase ==0:


    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        writethat.write("task 'possm'\n")
        writethat.write("source ")
        writethat.write("'"+field_names[y]+"''\n")
        writethat.write("stokes 'I' \n")
        writethat.write("outtext 'BOX:plot"+field_names[y]+"."+userid+"\n")
        writethat.write("antennas 0\n")
        writethat.write('dowait true \n')
        writethat.write("go possm; wait possm\n")
        
        os.system('rm -rf '+home+'/.boxfiles/plot'+field_names[y]+'.'+userid)




writethat.close()
os.system('rm -rf '+home+'/.boxfiles/flagfilegenerator_'+userid+'.py')
writethat=open(home+'/.boxfiles/flagfilegenerator_'+userid+'.py',"w")
writethat.write("from scipy.optimize import curve_fit \n")
writethat.write("k='"+home+"/.boxfiles/FLAG."+userid+"'\n")
writethat.write("os.system('rm -rf '+k)\n")
if not nophase ==0:
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        writethat.write("try:\n")
        writethat.write("   k='"+home+"/.boxfiles/plot"+field_names[y]+'.'+userid+"'\n")
        writethat.write("   if os.path.exists(k):\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("      flag=0\n")
        writethat.write("      a='doband 1'\n")
        writethat.write("      b='doband 3'\n")
        writethat.write("      \n")
        writethat.write("      for line in fin:\n")
        writethat.write("          if 'Channel' in line:\n")
        writethat.write("              flag=1\n")
        writethat.write("          newline=line      \n")
        writethat.write("          if 'FLAGGED' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'NaN' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'nfinity' in newline:\n")
        writethat.write("              newline=''    \n")        
        writethat.write("          if 'Header' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'RA' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'OBS' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'First channel plotted' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Bw' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Rest freq' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'DATA' in newline:\n")
        writethat.write("              newline=''    \n")
        
        
        
        writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
        writethat.write("          newline=newline.replace('I','00')     \n")
            
        writethat.write("          if flag==1:\n")
        writethat.write("              fout.write(newline)            \n")
        writethat.write("      \n")
        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
        writethat.write("      def func(x, a1,b1):\n")
        writethat.write("          return a1*x**b1\n")
        writethat.write("      popt, pcov = curve_fit(func, a, c,maxfev=500000)     \n")
            
        writethat.write("      flux=func(a,popt[0],popt[1])\n")
        writethat.write("      fluxerr=flux-c\n")
        writethat.write("      from numpy import mean, sqrt, square, arange\n")
        writethat.write("      rms = sqrt(mean(square(fluxerr)))\n")
        writethat.write("      index=0\n")
        writethat.write("      flagmechan=[]\n")
        writethat.write("      for k in fluxerr:\n")
        writethat.write("         if abs(k)>nsigma*rms:\n")
        writethat.write("             flagmechan.append(x[index])\n")
        writethat.write("         index=index+1 \n")
 


        writethat.write("      if "+str(midchan)+" in flagmechan:"+"\n")
        writethat.write("        for p in range(1000):"+"\n")
        writethat.write("          channell=random.randint(int("+str(midchan)+"/4),int("+str(midchan)+"*3/4))"+"\n")
        writethat.write("          if channell not in flagmechan:"+"\n")
        writethat.write("            midchannew=channell"+"\n")
        writethat.write("            break"+"\n")
        writethat.write("  "+"\n")
        writethat.write("        k='"+home+"/.aips/RUN/E2"+userid+"."+userid+"'\n")
        writethat.write("        k1='"+home+"/.aips/RUN/CALB."+userid+"'\n")

        writethat.write("  "+"\n")
        writethat.write("        fout = open(k+'fin', 'wt')"+"\n")  
        writethat.write("        fin = open(k1)"+"\n") 
        writethat.write(r"        fout.write('$ \n \n')"+"\n")        
        writethat.write(r"        fout.write('tget calib \n')"+"\n")
        writethat.write(r"        fout.write('ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 \n')"+"\n")
        writethat.write(r"        fout.write('tput calib \n')"+"\n")

        writethat.write("        for line in fin:"+"\n")
        writethat.write("            newline=line"+"\n")
        writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
        writethat.write("            fout.write(newline)"+"\n")
        writethat.write("        fin.close()"+"\n")

        writethat.write("        fin = open(k)"+"\n")
        writethat.write("  "+"\n")


        writethat.write(r"        fout.write('tget calib \n')"+"\n")
        writethat.write(r"        fout.write('ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 \n')"+"\n")
        writethat.write(r"        fout.write('tput calib \n')"+"\n")

        
        writethat.write("        for line in fin:"+"\n")
        writethat.write("            newline=line"+"\n")
        writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
        writethat.write("            fout.write(newline)"+"\n")
        writethat.write("        fout.close()"+"\n")
        writethat.write("         "+"\n")
        writethat.write("        fin.close()"+"\n")
        writethat.write("        os.system('rm -rf '+k)"+"\n")
        writethat.write("        os.system('mv '+k+'fin '+k)"+"\n")
        writethat.write("        k='"+home+"/.aips/RUN/E3"+userid+"."+userid+"'\n")
        writethat.write("        k1='"+home+"/.aips/RUN/CALB."+userid+"'\n")

        writethat.write("  "+"\n")
        writethat.write("        fout = open(k+'fin', 'wt')"+"\n")  
        writethat.write("        fin = open(k1)"+"\n") 
        writethat.write("        for line in fin:"+"\n")
        writethat.write("            newline=line"+"\n")
        writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
        writethat.write("            fout.write(newline)"+"\n")
        writethat.write("        fin.close()"+"\n")

        writethat.write("        fin = open(k)"+"\n")
        writethat.write("  "+"\n")
        writethat.write("        for line in fin:"+"\n")
        writethat.write("            newline=line"+"\n")
        writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
        writethat.write("            fout.write(newline)"+"\n")
        writethat.write("        fout.close()"+"\n")
        writethat.write("         "+"\n")
        writethat.write("        fin.close()"+"\n")
        writethat.write("        os.system('rm -rf '+k)"+"\n")
        writethat.write("        os.system('mv '+k+'fin '+k)"+"\n")

        writethat.write("      k='"+home+"/.boxfiles/FLAG."+userid+"'\n")
        writethat.write("      writethat=open(k,'a')\n")
        writethat.write("      for chann in flagmechan:\n")
        writethat.write("          writethat.write("+'"'+"ANTENNAS=0 BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" REASON='RFI'/  ! \n"+'"'+")\n")
        writethat.write("      writethat.close()\n")
        
        
        writethat.write("      k='"+home+"/.aips/RUN/E3"+userid+"."+userid+"'\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("   \n")
        writethat.write("      for line in fin:\n")
        writethat.write("         newline=line    \n")
        writethat.write("         newline=newline.replace('replaceme"+str(i)+"',str(popt[1]))    \n")
        writethat.write("         fout.write(newline)\n")

        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        
        writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plot"+field_names[y]+'.'+userid+"')\n")
        writethat.write("except:\n")
        writethat.write("   print 'Error'\n")        
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    writethat.write("try:\n")
    writethat.write("   k='"+home+"/.boxfiles/plot"+field_names[y]+'.'+userid+"'\n")
    writethat.write("   if os.path.exists(k):\n")
    writethat.write("      fin = open(k)\n")
    writethat.write("      fout = open(k+'fin', 'wt')\n")
    writethat.write("      #print k\n")
    writethat.write("      flag=0\n")
    writethat.write("      a='doband 1'\n")
    writethat.write("      b='doband 3'\n")
    writethat.write("      \n")
    writethat.write("      for line in fin:\n")
    writethat.write("          if 'Channel' in line:\n")
    writethat.write("              flag=1\n")
    writethat.write("          newline=line      \n")
    writethat.write("          if 'FLAGGED' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'NaN' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'nfinity' in newline:\n")
    writethat.write("              newline=''    \n")     
    writethat.write("          if 'Header' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'Source' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'RA' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'OBS' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'First channel plotted' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'Bw' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'Rest freq' in newline:\n")
    writethat.write("              newline=''    \n")
    writethat.write("          if 'DATA' in newline:\n")
    writethat.write("              newline=''    \n")
    
    writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
    writethat.write("          newline=newline.replace('I','00')     \n")
        
    writethat.write("          if flag==1:\n")
    writethat.write("              fout.write(newline)            \n")
    writethat.write("      \n")
    writethat.write("      fout.close()\n")
    writethat.write("      fin.close()\n")
    writethat.write("      os.system('rm -rf '+k)\n")
    writethat.write("      os.system('mv '+k+'fin '+k)\n")
    writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
    writethat.write("      def func(x, a1,b1):\n")
    writethat.write("          return a1*x**b1\n")
    writethat.write("      popt, pcov = curve_fit(func, a, c,maxfev=500000)     \n")
        
    writethat.write("      flux=func(a,popt[0],popt[1])\n")
    writethat.write("      fluxerr=flux-c\n")
    writethat.write("      from numpy import mean, sqrt, square, arange\n")
    writethat.write("      rms = sqrt(mean(square(fluxerr)))\n")
    writethat.write("      index=0\n")
    writethat.write("      flagmechan=[]\n")
    writethat.write("      for k in fluxerr:\n")
    writethat.write("         if abs(k)>nsigma*rms:\n")
    writethat.write("             flagmechan.append(x[index])\n")
    writethat.write("         index=index+1 \n")


    writethat.write("      if "+str(midchan)+" in flagmechan:"+"\n")
    writethat.write("        for p in range(1000):"+"\n")
    writethat.write("          channell=random.randint(int("+str(midchan)+"/4),int("+str(midchan)+"*3/4))"+"\n")
    writethat.write("          if channell not in flagmechan:"+"\n")
    writethat.write("            midchannew=channell"+"\n")
    writethat.write("            break"+"\n")
    writethat.write("  "+"\n")
    writethat.write("        k='"+home+"/.aips/RUN/E2"+userid+"."+userid+"'\n")
    writethat.write("        k1='"+home+"/.aips/RUN/CALB."+userid+"'\n")

    writethat.write("  "+"\n")
    writethat.write("        fout = open(k+'fin', 'wt')"+"\n")  
    writethat.write("        fin = open(k1)"+"\n") 
    writethat.write(r"        fout.write('$ \n \n')"+"\n")
    writethat.write(r"        fout.write('tget calib \n')"+"\n")
    writethat.write(r"        fout.write('ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 \n')"+"\n")
    writethat.write(r"        fout.write('tput calib \n')"+"\n")




    writethat.write("        for line in fin:"+"\n")
    writethat.write("            newline=line"+"\n")
    writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
    writethat.write("            fout.write(newline)"+"\n")
    writethat.write("        fin.close()"+"\n")

    writethat.write("        fin = open(k)"+"\n")
    writethat.write(r"        fout.write('$ \n \n')"+"\n")
    writethat.write(r"        fout.write('tget calib \n')"+"\n")
    writethat.write(r"        fout.write('ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 \n')"+"\n")
    writethat.write(r"        fout.write('tput calib \n')"+"\n")


    writethat.write("  "+"\n")
    writethat.write("        for line in fin:"+"\n")
    writethat.write("            newline=line"+"\n")
    writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
    writethat.write("            fout.write(newline)"+"\n")
    writethat.write("        fout.close()"+"\n")
    writethat.write("         "+"\n")
    writethat.write("        fin.close()"+"\n")
    writethat.write("        os.system('rm -rf '+k)"+"\n")
    writethat.write("        os.system('mv '+k+'fin '+k)"+"\n")
    writethat.write("        k='"+home+"/.aips/RUN/E3"+userid+"."+userid+"'\n")
    writethat.write("        k1='"+home+"/.aips/RUN/CALB."+userid+"'\n")

    writethat.write("  "+"\n")
    writethat.write("        fout = open(k+'fin', 'wt')"+"\n")  
    writethat.write("        fin = open(k1)"+"\n") 
    writethat.write("        for line in fin:"+"\n")
    writethat.write("            newline=line"+"\n")
    writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
    writethat.write("            fout.write(newline)"+"\n")
    writethat.write("        fin.close()"+"\n")

    writethat.write("        fin = open(k)"+"\n")
    writethat.write("  "+"\n")
    writethat.write("        for line in fin:"+"\n")
    writethat.write("            newline=line"+"\n")
    writethat.write("            newline=newline.replace('ichansel "+str(midchan)+" "+str(midchan)+" 1 0 ','ichansel '+str(midchannew)+' '+str(midchannew)+' 1 0 ')"+"\n")
    writethat.write("            fout.write(newline)"+"\n")
    writethat.write("        fout.close()"+"\n")
    writethat.write("         "+"\n")
    writethat.write("        fin.close()"+"\n")
    writethat.write("        os.system('rm -rf '+k)"+"\n")
    writethat.write("        os.system('mv '+k+'fin '+k)"+"\n")


    writethat.write("      k='"+home+"/.boxfiles/FLAG."+userid+"'\n")
    writethat.write("      writethat=open(k,'a')\n")
    writethat.write("      for chann in flagmechan:\n")
    writethat.write("          writethat.write("+'"'+"ANTENNAS=0 BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" REASON='RFI'/  ! \n"+'"'+")\n")
    writethat.write("      writethat.close()\n")
        
    writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plot"+field_names[y]+'.'+userid+"')\n")
    writethat.write("except:\n")
    writethat.write("   print 'Error'\n") 
for i in range(1,numm+1):
    for lm in range(30):
        x=(fiel[i-1])
        y=int(x)
        writethat.write("try:\n")    
        writethat.write("   k='"+home+"/.boxfiles/plotll"+field_names[y]+"."+userid+"."+str(lm)+"'\n")
        writethat.write("   if os.path.exists(k):\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("      flag=0\n")
        writethat.write("      a='doband 1'\n")
        writethat.write("      b='doband 3'\n")
        writethat.write("      \n")
        writethat.write("      for line in fin:\n")
        writethat.write("          if 'Channel' in line:\n")
        writethat.write("              flag=1\n")
        writethat.write("          newline=line      \n")
        writethat.write("          if 'FLAGGED' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'NaN' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'nfinity' in newline:\n")
        writethat.write("              newline=''    \n")         
        writethat.write("          if 'Header' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'RA' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'OBS' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'First channel plotted' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Bw' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Rest freq' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'DATA' in newline:\n")
        writethat.write("              newline=''    \n")
    
        writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
        writethat.write("          newline=newline.replace('LL','00')     \n")
            
        writethat.write("          if flag==1:\n")
        writethat.write("              fout.write(newline)            \n")
        writethat.write("      \n")
        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
        writethat.write("      def func(x, a1,b1):\n")
        writethat.write("          return a1*x**b1\n")
        writethat.write("      popt, pcov = curve_fit(func, a, c,maxfev=500000)     \n")
            
        writethat.write("      flux=func(a,popt[0],popt[1])\n")
        writethat.write("      fluxerr=flux-c\n")
        writethat.write("      from numpy import mean, sqrt, square, arange\n")
        writethat.write("      rms = sqrt(mean(square(fluxerr)))\n")
        writethat.write("      index=0\n")
        writethat.write("      flagmechan=[]\n")
        writethat.write("      for k in fluxerr:\n")
        writethat.write("         if abs(k)>nsigma*rms:\n")
        writethat.write("             flagmechan.append(x[index])\n")
        writethat.write("         index=index+1 \n")
    
        writethat.write("      k='"+home+"/.boxfiles/FLAG."+userid+"'\n")
        writethat.write("      writethat=open(k,'a')\n")
        writethat.write("      for chann in flagmechan:\n")
        writethat.write("          writethat.write("+'"'+"ANTENNAS="+str(lm+1)+" BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" STOKES='LL' REASON='RFI'/  ! \n"+'"'+")\n")
        writethat.write("      writethat.close()\n")
    
        writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plotll"+field_names[y]+"."+userid+"."+str(lm)+"')\n")
        writethat.write("except:\n")
        writethat.write("   print 'Error'\n") 

for i in range(1,numm+1):
    for lm in range(30):
        x=(fiel[i-1])
        y=int(x)
        writethat.write("try:\n")     
        writethat.write("   k='"+home+"/.boxfiles/plotrr"+field_names[y]+"."+userid+"."+str(lm)+"'\n")
        writethat.write("   if os.path.exists(k):\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("      flag=0\n")
        writethat.write("      a='doband 1'\n")
        writethat.write("      b='doband 3'\n")
        writethat.write("      \n")
        writethat.write("      for line in fin:\n")
        writethat.write("          if 'Channel' in line:\n")
        writethat.write("              flag=1\n")
        writethat.write("          newline=line      \n")
        writethat.write("          if 'FLAGGED' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'NaN' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'nfinity' in newline:\n")
        writethat.write("              newline=''    \n")         
        writethat.write("          if 'Header' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'RA' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'OBS' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'First channel plotted' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Bw' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Rest freq' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'DATA' in newline:\n")
        writethat.write("              newline=''    \n")
    
        writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
        writethat.write("          newline=newline.replace('RR','00')     \n")
            
        writethat.write("          if flag==1:\n")
        writethat.write("              fout.write(newline)            \n")
        writethat.write("      \n")
        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
        writethat.write("      def func(x, a1,b1):\n")
        writethat.write("          return a1*x**b1\n")
        writethat.write("      popt, pcov = curve_fit(func, a, c,maxfev=500000)     \n")
            
        writethat.write("      flux=func(a,popt[0],popt[1])\n")
        writethat.write("      fluxerr=flux-c\n")
        writethat.write("      from numpy import mean, sqrt, square, arange\n")
        writethat.write("      rms = sqrt(mean(square(fluxerr)))\n")
        writethat.write("      index=0\n")
        writethat.write("      flagmechan=[]\n")
        writethat.write("      for k in fluxerr:\n")
        writethat.write("         if abs(k)>nsigma*rms:\n")
        writethat.write("             flagmechan.append(x[index])\n")
        writethat.write("         index=index+1 \n")
    
        writethat.write("      k='"+home+"/.boxfiles/FLAG."+userid+"'\n")
        writethat.write("      writethat=open(k,'a')\n")
        writethat.write("      for chann in flagmechan:\n")
        writethat.write("          writethat.write("+'"'+"ANTENNAS="+str(lm+1)+" BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" STOKES='RR' REASON='RFI'/  ! \n"+'"'+")\n")
        writethat.write("      writethat.close()\n")
    
        writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plotrr"+field_names[y]+"."+userid+"."+str(lm)+"')\n")
        writethat.write("except:\n")
        writethat.write("   print 'Error'\n") 

if len(pacal_fiel)>0:
    writethat.write("listname='"+outputfolder+"/"+name1+".listr'" +"\n")
    writethat.write("fin=open(listname)" +"\n")
    writethat.write("" +"\n")
    writethat.write("flag=0" +"\n")
    writethat.write("for j in fin:" +"\n")
    writethat.write("     if '"+str(field_names[pacal_fiel[0]])+"' in j:" +"\n")
    writethat.write("        timerpacal=j[41]+' '+j[43:45]+' '+j[46:48]+' '+j[49:51]+', '+j[56:57]+' '+j[58:60]+' '+j[61:63]+' '+j[64:66]" +"\n")
    writethat.write("        #print j[14:38]" +"\n")
    writethat.write("        break" +"\n")
    writethat.write("" +"\n")
    writethat.write("fin.close()" +"\n")


    writethat.write("k='"+home+"/.aips/RUN/E3"+userid+"."+userid+"'\n")
    writethat.write("fin = open(k)\n")
    writethat.write("fout = open(k+'fin', 'wt')\n")
    writethat.write("#print k\n")
    writethat.write("\n")
    writethat.write("for line in fin:\n")
    writethat.write("   newline=line    \n")
    writethat.write("   newline=newline.replace('replacemetime',timerpacal)    \n")
    writethat.write("   fout.write(newline)\n")
    writethat.write("fout.close()\n")
    writethat.write("fin.close()\n")
    writethat.write("os.system('rm -rf '+k)\n")
    writethat.write("os.system('mv '+k+'fin '+k)\n")

if nodcal>0 and not usepacal=='y':

    writethat.write("listname='"+outputfolder+"/"+name1+".fluxes'" +"\n")
    writethat.write("fin=open(listname)" +"\n")
    writethat.write("" +"\n")
    writethat.write("flag=0" +"\n")
    writethat.write("for j in fin:" +"\n")
    writethat.write("     if '"+str(field_names[dcal_fiel[0]])+"' in j:" +"\n")
    writethat.write("        fluxdcal=j[44:49]" +"\n")
    writethat.write("        #print j[14:38]" +"\n")
    writethat.write("        break" +"\n")
    writethat.write("" +"\n")
    writethat.write("fin.close()" +"\n")


    writethat.write("k='"+home+"/.aips/RUN/E3"+userid+"."+userid+"'\n")
    writethat.write("fin = open(k)\n")
    writethat.write("fout = open(k+'fin', 'wt')\n")
    writethat.write("#print k\n")
    writethat.write("\n")
    writethat.write("for line in fin:\n")
    writethat.write("   newline=line    \n")
    writethat.write("   newline=newline.replace('replacemeflux',fluxdcal)    \n")
    writethat.write("   fout.write(newline)\n")
    writethat.write("fout.close()\n")
    writethat.write("fin.close()\n")
    writethat.write("os.system('rm -rf '+k)\n")
    writethat.write("os.system('mv '+k+'fin '+k)\n")




writethat.close()
writethat=open(home+'/.aips/RUN/E3'+userid+'.'+userid,"w")

if choice==2:
	writethat.write("$\n")
	writethat.write("task 'uvflg'\n")
	writethat.write("default\n")
	writethat.write("getn 1\n")
	writethat.write('outfgver 1 \n')
	writethat.write("intext 'BOX:FLAG."+userid+"\n")
	writethat.write("opcode 'flag'\n")
	writethat.write('dowait true \n')
	writethat.write("go uvflg; wait uvflg;\n")



	writethat.write("task 'uvcop' \n")
	writethat.write('default \n')
 	writethat.write('getn 1 \n')
 	writethat.write("flagver 1 \n")
 	writethat.write('dowait true \n')
 	writethat.write('go uvcop; wait uvcop; end\n \n')
	writethat.write('getn 1 ;clrstat; zap; recat \n \n')
writethat.write('getn 1 \n \n')


writethat.write("inext 'bp' \n")
writethat.write("extd \n")

for i in range(1,noflux+1):
    writethat.write("task 'bpass' \n")
    writethat.write('default \n')
    writethat.write('getn 1 \n')
    writethat.write('docal -1 \n')
    writethat.write("inext '' \n")
    writethat.write('inver 0 \n')
    writethat.write('outver 1 \n')    
    writethat.write('bpassprm(10) 3 \n')
    writethat.write('bpassprm(5) 1 \n')
    writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("soltyp 'L1R'    \n")       
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')

if phasebp=='y':
    for i in range(1,nophase+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 1 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(midchan)+' '+str(midchan)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("specindx replaceme"+str(i)+"\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')


writethat.write("task 'splat' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('aparm(1)=3 \n')
writethat.write('channel '+str(chav[0])+'\n')
writethat.write('ichansel '+str(begch)+' '+str(endch)+' 1 0  \n')
writethat.write('docal -1 \n')
writethat.write('chinc 0 \n')
writethat.write('doband 3 \n')
writethat.write('bchan '+str(begch)+' \n')
writethat.write('echan '+str(endch)+' \n')
writethat.write('bpver 0 \n')
writethat.write("source '' \n")
writethat.write('dowait true \n')
writethat.write('go splat; wait splat; end\n \n')


for i in range(1,noflux+1):
    writethat.write("task 'clip' \n")
        
    writethat.write('default \n')
    writethat.write("outfgver 1 \n")
    writethat.write('getn 2 \n')
    writethat.write("source ")
    x=(flux_fiel[i-1])
    y=int(x)
    cliplevel1= meanlevel[y]+75*sens
    cliplevel2=meanlevel[y]-75*sens
    if (cliplevel2<0):
        cliplevel2=1
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
        
    writethat.write('docal 1 \n')
    writethat.write("stokes 'll' \n")


    writethat.write('bpver 0 \n')
    writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
    writethat.write('dowait true \n')
    writethat.write('go clip; wait clip; end \n\n')
    writethat.write("stokes 'rr' \n")
    writethat.write('go clip; wait clip; end \n\n')



writethat.write("task 'clip' \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write("source ")
for i in range(1,notarg+1):
    x=(target_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")

writethat.write("'\n")
writethat.write("docal 1 \n")
writethat.write('aparm '+str(10*mf*sens)+' 0 \n')
writethat.write("outfgver 1 \n")
writethat.write('dowait true \n')
writethat.write('go clip; wait clip; end\n \n')

writethat.write("task 'setjy' \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write("inext 'sn' \n")
writethat.write("extd \n")
writethat.write("inext 'cl' \n")
writethat.write("extd \n")
writethat.write("optype 'calc' \n")
writethat.write("source ")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")

writethat.write("'\n")
writethat.write('dowait true \n')
writethat.write('go setjy; wait setjy; end \n\n')

writethat.write("tget calib \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write("calsour ")

for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")
writethat.write('ichansel '+str(chav1[0]/2)+' '+str(chav1[0]/2)+' 1 0\n')
writethat.write("soltype 'L1R'"'\n')
writethat.write('uvrange '+uvlow+' 0\n')
writethat.write('refant '+refAnt+'\n')
writethat.write('dowait true \n')
#writethat.write('doflag 1 \n')
writethat.write('go calib; wait calib; end \n\n')
if not (flux_field==phase_field) and not (phase_field==[]):
    writethat.write("tget clcal \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write("source ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("calsour ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)    
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("OPCODE 'cali' \n")
    writethat.write("SAMPTYPE 'mwf' \n")
    writethat.write('dowait true \n')
    writethat.write('go clcal; wait clcal; end \n\n')
    
    writethat.write("tget getjy \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write("source ")
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write("calsour ")
    for i in range(1,noflux+1):
        x=(flux_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    
    writethat.write("'\n")
    
    writethat.write('dowait true \n')
    writethat.write('go getjy; wait getjy; end \n\n')
    
    writethat.write("inext 'cl' \n")    
    writethat.write('extd \n')

writethat.write("tget clcal \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write("source '' \n")
writethat.write("calso ")
for i in range(1,nophase+1):
    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
for i in range(1,noflux+1):
    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
writethat.write("'\n")

writethat.write("OPCODE 'cali' \n")
writethat.write("SAMPTYPE 'mwf' \n")
writethat.write('dowait true \n')
writethat.write('go clcal; wait clcal; end \n\n')


for loopn in range(15):

    for i in range(1,noflux+1):
    #    writethat.write("compress \n")
    #    writethat.write("compress \n")
        writethat.write("task 'clip' \n")
            
        writethat.write('default \n')
        writethat.write("outfgver 1 \n")
        writethat.write('bchan '+str(chav1[0]/2)+' \n')
        writethat.write('echan '+str(chav1[0]/2)+' \n')        
        writethat.write('getn 2 \n')
        writethat.write("source ")
        x=(flux_fiel[i-1])
        y=int(x)
        cliplevel1= meanlevel[y]+70*sens/1.15**loopn
        cliplevel2=meanlevel[y]-70*sens/1.15**loopn
        if (cliplevel2<0):
            cliplevel2=1
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("stokes 'rr' \n")
    
        writethat.write('docal 1 \n')
        #writethat.write('doband 3 \n')
        #writethat.write('bpver 0 \n')
        writethat.write('aparm '+str(cliplevel1)+' 0 '+str(cliplevel2)+' 0 \n')
        writethat.write('dowait true \n')
        writethat.write('go clip; wait clip; end \n\n')
        writethat.write("stokes 'll' \n")
        writethat.write('go clip; wait clip; end \n\n')
    writethat.write("task 'clip' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write('bchan '+str(chav1[0]/2)+' \n')
    writethat.write('echan '+str(chav1[0]/2)+' \n')     
    writethat.write("source ")
    for i in range(1,nophase+1):
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
    
    writethat.write("'\n")
    writethat.write("docal 1 \n")
    writethat.write('aparm '+str(10*mf*sens)+' 0 \n')
    writethat.write("outfgver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go clip; wait clip; end\n \n')

    writethat.write('getn 2  \n')
    writethat.write("inext 'sn' \n")
    writethat.write("extd \n")
    writethat.write("inext 'cl' \n")
    writethat.write("extd \n")
    
    writethat.write("tget calib \n")
    writethat.write('dowait true \n')
    writethat.write("go calib ; wait calib\n")
    if not (flux_field==phase_field) and not (phase_field==[]):
        writethat.write("tget getjy \n")
        writethat.write('dowait true \n')
        writethat.write("go getjy; wait getjy \n")
    writethat.write("tget clcal \n")
    writethat.write('dowait true \n')
    writethat.write("go clcal; wait clcal \n")



writethat.write("task 'snflg' \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write('dparm(8)=1 \n')
writethat.write("optype 'a&p' \n")
#writethat.write("outfgver 1 \n")
writethat.write("inext 'sn' \n")
writethat.write('dowait true \n')
writethat.write('go snflg; wait snflg; end\n \n')


writethat.write('getn 2  \n')
writethat.write("inext 'sn' \n")
writethat.write("extd \n")
writethat.write("inext 'cl' \n")
writethat.write("extd \n")

writethat.write("tget calib \n")
writethat.write('dowait true \n')
writethat.write('doflag 5 \n')
writethat.write("go calib ; wait calib\n")


if not (flux_field==phase_field) and not (phase_field==[]):
    writethat.write("tget getjy \n")
    writethat.write('dowait true \n')
    writethat.write("go getjy; wait getjy \n")
writethat.write("tget clcal \n")
writethat.write('dowait true \n')
writethat.write("go clcal; wait clcal \n")




for i in range(1,noflux+1):
    writethat.write("task 'bpass' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write('docal -1 \n')
    writethat.write("inext '' \n")
    writethat.write('inver 0 \n')
    writethat.write('outver 1 \n')    
    writethat.write('bpassprm(10) 3 \n')
    writethat.write('bpassprm(5) 1 \n')
    writethat.write('ichansel '+str(chav1[0]/2)+' '+str(chav1[0]/2)+' 1 0 \n')
    writethat.write("calsour ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("soltyp 'L1R'    \n")       
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write('go bpass; wait bpass; end \n\n')

if phasebp=='y':
    for i in range(1,nophase+1):
        writethat.write("task 'bpass' \n")
        writethat.write('default \n')
        writethat.write('getn 2 \n')
        writethat.write('docal -1 \n')
        writethat.write("inext '' \n")
        writethat.write('inver 0 \n')
        writethat.write('outver 1 \n')    
        writethat.write('bpassprm(10) 3 \n')
        writethat.write('bpassprm(5) 1 \n')
        writethat.write('ichansel '+str(chav1[0]/2)+' '+str(chav1[0]/2)+' 1 0 \n')
        writethat.write("calsour ")
    
        x=(phase_fiel[i-1])
        y=int(x)
        
        writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("specindx replaceme"+str(i)+"\n")
        writethat.write('uvrange '+uvlow+' 0     \n')       
        writethat.write("soltyp 'L1R'    \n")       
        writethat.write('refant '+refAnt+'\n')
        writethat.write('dowait true \n')
        writethat.write('go bpass; wait bpass; end \n\n')


writethat.write('i=2 \n\n')
writethat.write('getn 1  \n')
writethat.write("inext 'sn' \n")
writethat.write("extd \n")
writethat.write("inext 'cl' \n")
writethat.write("extd \n")
writethat.write("task 'tacop' \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write('geto 1 \n')
writethat.write("inext 'sn' \n")
writethat.write('dowait true \n')
writethat.write('go tacop; wait tacop ; end\n \n')
writethat.write("tget tacop \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write('geto 1 \n')
writethat.write("inext 'cl' \n")
writethat.write('dowait true \n')
writethat.write('go tacop; wait tacop ; end\n \n')

writethat.write("tget tacop \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write('geto 1 \n')
writethat.write("inext 'fg' \n")
writethat.write('dowait true \n')
writethat.write('go tacop; wait tacop ; end\n \n')

if npols==4:
    writethat.write("task 'rldly' \n")
    writethat.write("default \n")
    writethat.write("docal 1 \n")
    writethat.write("doband 3 \n")
    writethat.write("getn 1 \n")
    writethat.write("solint ="+str(median_integration_time)+" \n")
    writethat.write("calsour ")
    for i in range(1,nopacal+1):
        x=(pacal_fiel[i-1])
        y=int(x)
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write('refant '+refAnt+'\n')


    writethat.write("timer replacemetime  \n")
    writethat.write('dowait true \n')
    writethat.write("dowait True \n")
    writethat.write("go rldly \n")
    
    writethat.write("task 'pcal' \n")
    writethat.write("default \n")
    writethat.write("getn 1 \n")
    writethat.write("soltype 'appr' \n")
    #writethat.write("uvrange 0,20 \n")
    writethat.write("spectral =0 \n")
    writethat.write("cparm(2)=1 \n")

    writethat.write("calsour ")
    if nodcal>0 and not usepacal=='y':
        for i in range(1,nodcal+1):
            x=(dcal_fiel[i-1])
            y=int(x)
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("domodel 1 \n")
        writethat.write("pmodel replacemeflux 0 \n")
    else:
        for i in range(1,nopacal+1):
            x=(pacal_fiel[i-1])
            y=int(x)
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
    
    writethat.write('refant '+refAnt+'\n')
    writethat.write("spectral 1 \n")
    writethat.write("docal 1 \n")
    writethat.write("doband 3 \n")
    writethat.write('dowait true \n')
    writethat.write("dowait true \n")
    writethat.write("go pcal \n")
    

    for lm in range(30):
        writethat.write("task 'possm'\n")
        writethat.write("default \n")
        writethat.write("getn 1\n")
        writethat.write("stokes 'LL'\n")
        writethat.write("outtext 'BOX:plotpdll."+userid+'.'+str(lm)+"\n")
        writethat.write('dowait true \n')
        writethat.write("antennas "+str(lm+1)+"\n")
        writethat.write('aparm(8) 6 \n')
        writethat.write("nplo 0\n")
    
        writethat.write("go possm; wait possm\n")
        os.system('rm -rf '+home+'/.boxfiles/plotpdll.'+userid+'.'+str(lm))
    for lm in range(30):    

        writethat.write("task 'possm'\n")
        writethat.write("default \n")
        writethat.write("getn 1\n")
        writethat.write("stokes 'RR'\n")  
        writethat.write("antennas "+str(lm+1)+"\n")
        writethat.write("outtext 'BOX:plotpdrr."+userid+'.'+str(lm)+"\n")
        writethat.write('dowait true \n')
        writethat.write('aparm(8) 6 \n')
        writethat.write("nplo 0\n")
    
        writethat.write("go possm; wait possm\n")
        os.system('rm -rf '+home+'/.boxfiles/plotpdrr.'+userid+'.'+str(lm))

    writethat.close()
    os.system('rm -rf '+home+'/.boxfiles/flagfilegeneratorpd_'+userid+'.py')
    writethat=open(home+'/.boxfiles/flagfilegeneratorpd_'+userid+'.py',"w")
    writethat.write("from scipy.optimize import curve_fit \n")
    writethat.write("k='"+home+"/.boxfiles/FLAGPD."+userid+"'\n")
    writethat.write("os.system('rm -rf '+k)\n")
    for lm in range(30): 

        writethat.write("try:\n")
        writethat.write("   k='"+home+"/.boxfiles/plotpdrr."+userid+'.'+str(lm)+"'\n")
        writethat.write("   flagmechan=[]\n")
        writethat.write("   if os.path.exists(k):\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("      flag=0\n")
        writethat.write("      a='doband 1'\n")
        writethat.write("      b='doband 3'\n")
        writethat.write("      \n")
        writethat.write("      for line in fin:\n")
        writethat.write("          if 'Channel' in line:\n")
        writethat.write("              flag=1\n")
        writethat.write("          newline=line      \n")
        writethat.write("          if 'PD TABLE' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source:' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'RA:    0  0  0.00' in newline:\n")
        writethat.write("              newline=''    \n")        
        writethat.write("          if 'No. channels' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Antenna' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'OBS' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'First channel plotted' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Bw' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Rest freq' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'DATA' in newline:\n")
        writethat.write("              newline=''    \n")
            
        writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
        writethat.write("          newline=newline.replace('FLAGGED','00')     \n")
        writethat.write("          newline=newline.replace('R','00')     \n")
              
        writethat.write("          if flag==1:\n")
        writethat.write("              fout.write(newline)            \n")
        writethat.write("      \n")
        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
        writethat.write("      index=0\n")
        writethat.write("      for i in c:\n")        
        writethat.write("         if abs(i)>0.4:\n")
        writethat.write("             flagmechan.append(x[index])\n")
        writethat.write("         index=index+1 \n")

        writethat.write("      k='"+home+"/.boxfiles/FLAGPD."+userid+"'\n")
        writethat.write("      writethat=open(k,'a')\n")
        writethat.write("      for chann in flagmechan:\n")
        writethat.write("          writethat.write("+'"'+"ANTENNAS="+str(lm+1)+" BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" REASON='RFI'/  ! \n"+'"'+")\n")
        writethat.write("      writethat.close()\n")

        
        #writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plotpdrr."+userid+'.'+str(lm)+"')\n")
        writethat.write("except:\n")
        writethat.write("   print 'Error'\n")        


        writethat.write("try:\n")
        writethat.write("   k='"+home+"/.boxfiles/plotpdll."+userid+'.'+str(lm)+"'\n")
        
        writethat.write("   flagmechan=[]\n")
        
        writethat.write("   if os.path.exists(k):\n")
        writethat.write("      fin = open(k)\n")
        writethat.write("      fout = open(k+'fin', 'wt')\n")
        writethat.write("      #print k\n")
        writethat.write("      flag=0\n")
        writethat.write("      a='doband 1'\n")
        writethat.write("      b='doband 3'\n")
        writethat.write("      \n")
        writethat.write("      for line in fin:\n")
        writethat.write("          if 'Channel' in line:\n")
        writethat.write("              flag=1\n")
        writethat.write("          newline=line      \n")
        writethat.write("          if 'PD TABLE' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source:' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'RA:    0  0  0.00' in newline:\n")
        writethat.write("              newline=''    \n")        
        writethat.write("          if 'No. channels' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Source' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Antenna' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'OBS' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'First channel plotted' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Bw' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'Rest freq' in newline:\n")
        writethat.write("              newline=''    \n")
        writethat.write("          if 'DATA' in newline:\n")
        writethat.write("              newline=''    \n")
            
        writethat.write("          newline=newline.replace('Channel','#Channel')    \n")
        writethat.write("          newline=newline.replace('FLAGGED','00')     \n")
        writethat.write("          newline=newline.replace('L','00')     \n")
              
        writethat.write("          if flag==1:\n")
        writethat.write("              fout.write(newline)            \n")
        writethat.write("      \n")
        writethat.write("      fout.close()\n")
        writethat.write("      fin.close()\n")
        writethat.write("      os.system('rm -rf '+k)\n")
        writethat.write("      os.system('mv '+k+'fin '+k)\n")
        writethat.write("      x,y,z,a,b,c,d = np.loadtxt(k, unpack=True)\n")
        writethat.write("      index=0\n")
        writethat.write("      for i in c:\n")        
        writethat.write("         if abs(i)>0.4:\n")
        writethat.write("             flagmechan.append(x[index])\n")
        writethat.write("         index=index+1 \n")

        writethat.write("      k='"+home+"/.boxfiles/FLAGPD."+userid+"'\n")
        writethat.write("      writethat=open(k,'a')\n")
        writethat.write("      for chann in flagmechan:\n")
        writethat.write("          writethat.write("+'"'+"ANTENNAS="+str(lm+1)+" BCHAN="+'"'+"+str(chann)+"+'"'+" ECHAN="+'"'+"+str(chann)+"+'"'+r" REASON='RFI'/  ! \n"+'"'+")\n")
        writethat.write("      writethat.close()\n")

        
        #writethat.write("   os.system('rm -rf "+home+"/.boxfiles/plotpdll."+userid+'.'+str(lm)+"')\n")
        writethat.write("except:\n")
        writethat.write("   print 'Error'\n")        


    writethat.close()    
    writethat=open(home+'/.aips/RUN/E3A'+userid+'.'+userid,"w")    
    writethat.write("$\n")
    writethat.write("task 'uvflg'\n")
    writethat.write("default\n")
    writethat.write("getn 1\n")
    writethat.write('outfgver 1 \n')
    writethat.write("intext 'BOX:FLAGPD."+userid+"\n")
    writethat.write("opcode 'flag'\n")
    writethat.write('dowait true \n')
    writethat.write("go uvflg; wait uvflg;\n")

    writethat.write("tget pcal \n")
    #writethat.write("default \n")
    writethat.write("getn 1 \n")
    writethat.write("inext 'pd' \n")
    writethat.write("extd \n")    
    writethat.write("inext 'cp' \n")
    writethat.write("extd \n")    
    writethat.write("soltype 'appr' \n")
    #writethat.write("uvrange 0,20 \n")
    writethat.write("spectral =0 \n")
    writethat.write("cparm(2)=1 \n")

    writethat.write("calsour ")
    if nodcal>0 and not usepacal=='y':
        for i in range(1,nodcal+1):
            x=(dcal_fiel[i-1])
            y=int(x)
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
        writethat.write("domodel 1 \n")
        #writethat.write("pmodel replacemeflux 0 \n")

    else:
        for i in range(1,nopacal+1):
            x=(pacal_fiel[i-1])
            y=int(x)
            writethat.write("'"+field_names[y]+"'")
        writethat.write("'\n")
    
    writethat.write('refant '+refAnt+'\n')
    writethat.write("spectral 1 \n")
    writethat.write("docal 1 \n")
    writethat.write("doband 3 \n")
    writethat.write('dowait true \n')
    writethat.write("dowait true \n")
    writethat.write("go pcal \n")
    


    writethat.write("task 'rldif' \n")
    writethat.write("default \n")
    writethat.write("getn 1 \n")
    writethat.write("docal 1 \n")
    writethat.write("doband 3 \n")
    writethat.write("doapply =1 \n")
    writethat.write("dopol 1 \n")
    writethat.write("spectral =1 \n")
    #writethat.write("uvrange 0,20 \n")
    writethat.write(" \n")
    writethat.write('dowait true \n')
    writethat.write("dowait true \n")
    writethat.write("solint ="+str(median_integration_time)+" \n")
    writethat.write("source ")
    for i in range(1,nopacal+1):
        x=(pacal_fiel[i-1])
        y=int(x)
        writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write('refant '+refAnt+'\n')
    writethat.write('dowait true \n')
    writethat.write("dowait True \n")
    writethat.write("go rldif \n")



writethat.write('dowait true \n')


writethat.write("task 'splat' \n")
writethat.write('default \n')
writethat.write('getn 1 \n')
writethat.write('aparm(1)=3 \n')
writethat.write('channel '+str(chav[0])+'\n')
writethat.write('ichansel '+str(begch)+' '+str(endch)+' 1 0  \n')
writethat.write('docal 1 \n')
writethat.write('chinc 0 \n')
writethat.write('doband 3 \n')
if npols==4:
	writethat.write('dopol 1 \n')
writethat.write('bchan '+str(begch)+' \n')
writethat.write('echan '+str(endch)+' \n')
writethat.write('bpver 0 \n')
writethat.write("source '' \n")
writethat.write('dowait true \n')
writethat.write('go splat; wait splat; end\n \n')

writethat.write("tget tacop \n")
writethat.write('default \n')
writethat.write('getn 2 \n')
writethat.write('geto 3 \n')
writethat.write("inext 'bp' \n")
writethat.write('dowait true \n')
writethat.write('go tacop; wait tacop ; end\n \n')


writethat.write('getn 2;clrstat; zap; recat \n')

if choice==2:
    writethat.write("task 'fittp'\n")
    writethat.write("default\n")
    writethat.write("getn 2\n")
    writethat.write("dataout 'OUT:im/delme"+str(ref)+".fits\n")
    writethat.write('dowait true \n')
    writethat.write("go fittp; wait fittp\n")
    writethat.close()
    writethat=open(home+'/.aips/RUN/E4'+userid+'.'+userid,"w")
    writethat.write('$\n')
    writethat.write("task 'fitld'\n")
    writethat.write('default \n')
    writethat.write("datain 'OUT:im/delme"+str(ref)+".fits\n")
    writethat.write('go fitld \n')
    writethat.write('dowait true \n')
    writethat.write('wait fitld \n\n')
    writethat.write("getn 3; inext 'an'; extd \n")
    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'an' \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")
    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'cl' \n")
    writethat.write("inver 1 \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")
    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'bp' \n")
    writethat.write("inver 1 \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")

   
    #writethat.write("task 'tacop' \n")
    #writethat.write("default \n")
    #writethat.write("getn 2 \n")
    #writethat.write("geto 3\n")
    #writethat.write("inext 'sn' \n")
    writethat.write('dowait true \n')
    #writethat.write("go tacop; wait tacop \n")
    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'nx' \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")
    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'xx' \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")

    writethat.write("task 'tacop' \n")
    writethat.write("default \n")
    writethat.write("getn 2 \n")
    writethat.write("geto 3\n")
    writethat.write("inext 'fg' \n")
    writethat.write('dowait true \n')
    writethat.write("go tacop; wait tacop \n")


    writethat.write("getn 2;clrstat; zap;recat \n")


writethat.close()


for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)
    writethat=open(home+'/.aips/RUN/E'+userid+''+str(i)+'.'+userid,"w")
    writethat.write("$ \n")
    writethat.write("task 'split' \n")#rembr to change bak to split
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    #writethat.write('aparm(1)=1 \n')
    #writethat.write('bchan '+str(begch)+' \n')
    #writethat.write('echan '+str(endch)+' \n')
    #writethat.write('nchav '+str(chav[i-1])+' \n')
    #writethat.write('chinc '+str(chav[i-1])+' \n')
    #writethat.write('ichansel '+str(begch)+' '+str(endch)+' 1 0  \n')
    #writethat.write('docal 1 \n')
    writethat.write('doband 3 \n')
    writethat.write('bpver 0 \n')
    writethat.write("source ")
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go split; wait split; end\n \n')
    os.system('rm -rf '+home+'/.boxfiles/hope1.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope2.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope3.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope4.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope5.'+userid+'.'+str(lm))
    syscommand='rm -rf '+home+'/.boxfiles/box.'+userid+'.'+str(lm)


    writethat.write("task 'clip' \n")
    writethat.write('default \n')
    writethat.write('j=1+i \n')
    writethat.write('getn j\n')

    writethat.write("source ")
    x=(target_fiel[i-1])
    y=int(x)
        
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    
    writethat.write('aparm '+str(10*mf*sens)+' 0 \n')
    writethat.write("outfgver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go clip; wait clip; end\n \n')


    os.system(syscommand)

    writethat.write("task 'setfc'\n")
    writethat.write('default\n')
    writethat.write('j=1+i \n')
    writethat.write('getn j\n')
    writethat.write('bparm '+str(pb)+' 2 0\n')# has to ndividualize for diff freq
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write('dowait true \n')
    writethat.write('go setfc; wait setfc; end\n')
    writethat.write('go setfc; wait setfc; end\n')

    writethat.write('wait setfc; end\n\n')
    os.system('rm -rf '+home+'/.boxfiles/hope1.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope2.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope3.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope4.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/hope5.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/box.'+userid+'.'+str(lm))
    os.system('rm -rf '+home+'/.boxfiles/obox.'+userid+'.'+str(lm))

    writethat.write("task 'imagr'\n")
    writethat.write("INNAME   ' '                        \n")
    writethat.write("INCLASS     ' '                         \n")
    writethat.write("INSEQ          0                       \n")
    writethat.write("INDISK       0                     \n")
    writethat.write("SOURCES      ' '                 \n")
    writethat.write("QUAL           -1                      \n")
    writethat.write("CALCODE     ' '                         \n")
    writethat.write("TIMERANG    0                   \n")
    writethat.write("SELBAND        -1                      \n")
    writethat.write("SELFREQ        -1                      \n")
    writethat.write("FREQID      -1                     \n")
    writethat.write("SUBARRAY       0                       \n")
    writethat.write("ANTENNAS    0                   \n")
    writethat.write("BASELINE    0                   \n")
    writethat.write("GAINUSE         0                      \n")
    writethat.write("DOPOL        -1                        \n")
    writethat.write("PDVER          0                       \n")
    writethat.write("BLVER        -1                        \n")
    writethat.write("FLAGVER         0                      \n")
    writethat.write("DOBAND      -1                     \n")
    writethat.write("BPVER        -1                        \n")
    writethat.write("SMOOTH     0                    \n")
    writethat.write("STOKES   ' '                        \n")
    writethat.write("BCHAN          1                       \n")
    writethat.write("ECHAN          0                       \n")
    writethat.write("CHINC          1                       \n")
    writethat.write("BIF              0                     \n")
    writethat.write("EIF              0                     \n")
    writethat.write("OUTNAME     ' '                         \n")
    writethat.write("OUTDISK         1                      \n")
    writethat.write("OUTSEQ       0                     \n")
    writethat.write("OUTVER       0                     \n")
    writethat.write("IN2NAME     ' '                         \n")
    writethat.write("IN2CLASS   ' '                      \n")
    writethat.write("IN2SEQ       0                     \n")
    writethat.write("IN2DISK         0                      \n")
    writethat.write("DO3DIMAG     -1                        \n")
    writethat.write("FLDSIZE      0                  \n")
    writethat.write("RASHIFT      0                  \n")
    writethat.write("DECSHIFT    0                   \n")
    writethat.write("UVTAPER         0            0     \n")
    writethat.write("UVRANGE         0            0     \n")
    writethat.write("GUARD          0             0     \n")
    writethat.write("ROTATE       0                     \n")
    writethat.write("ZEROSP     0                    \n")
    writethat.write("UVWTFN   ' '                        \n")
    writethat.write("UVSIZE       0           0     \n")
    writethat.write("ROBUST       0                     \n")
    writethat.write("UVBOX          0                       \n")
    writethat.write("UVBXFN       1                     \n")
    writethat.write("XTYPE          5                       \n")
    writethat.write("YTYPE          5                       \n")
    writethat.write("XPARM       0                   \n")
    writethat.write("YPARM       0                   \n")
    writethat.write("NITER          0                       \n")
    writethat.write("BCOMP       0                   \n")
    writethat.write("ALLOKAY         0                      \n")
    writethat.write("NBOXES       0                     \n")
    writethat.write("CLBOX       0                   \n")
    writethat.write("BOXFILE      ' '                 \n")
    writethat.write("OBOXFILE    ' '                  \n")
    writethat.write("GAIN            0.1                     \n")
    writethat.write("MINPATCH     51                        \n")
    writethat.write("BMAJ            0                      \n")
    writethat.write("BMIN            0                      \n")
    writethat.write("BPA              0                     \n")
    writethat.write("OVERLAP         0                      \n")
    writethat.write("ONEBEAM         0                      \n")
    writethat.write("OVRSWTCH       0                       \n")
    writethat.write("PHAT            0                      \n")
    writethat.write("FACTOR       0                     \n")
    writethat.write("CMETHOD     ' '                         \n")
    writethat.write("IMAGRPRM    0                   \n")
    writethat.write("IMAGRPRM    0                   \n")
    writethat.write("IM2PARM      0                  \n")
    writethat.write("NGAUSS       0                     \n")
    writethat.write("WGAUSS     0                    \n")
    writethat.write("FGAUSS     0                    \n")
    writethat.write("MAXPIXEL   20000                     \n")
    writethat.write("IN3NAME     ' '                         \n")
    writethat.write("IN3CLASS   ' '                      \n")
    writethat.write("IN3SEQ       0                     \n")
    writethat.write("IN3DISK         0                      \n")
    writethat.write("IN4NAME     ' '                         \n")
    writethat.write("IN4CLASS   ' '                      \n")
    writethat.write("IN4SEQ       0                     \n")
    writethat.write("IN4DISK         0                      \n")
    writethat.write("FQTOL        -1                        \n")
    writethat.write("DOTV           -1                      \n")
    writethat.write("LTYPE          3                       \n")
    writethat.write("BADDISK      0                  \n")


    writethat.write('getn j\n')
    writethat.write("stokes 'I'\n")
    writethat.write('channel 0\n')
    if fracband>0.12:
        writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
        writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
        writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
    else:
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      
    #writethat.write('flux '+str(rms_tot[i-1]*5)+'\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    writethat.write('robust 0       \n')  
      
    writethat.write('niter '+str(int(niter/20))+'\n')                   
    writethat.write("BOXFILE 'BOX:box."+userid+'.'+str(lm)+"\n")
    writethat.write("OBOXFILE 'BOX:obox."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    writethat.write('uvrange '+uvlow+' 0\n')    
    writethat.write('dowait true \n')
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrmsg \n")
    writethat.write('recat \n')

    writethat.write('x = 2*nfield+j-1 \n')
    writethat.write('dist= x \n')
    writethat.write("task 'imean' \n default \n")
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    #writethat.write('kk=6*kk/6 \n')

    writethat.write("task 'sabox'\n")
    writethat.write("inclass 'ICL001'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    

    writethat.write('aparm 5 7 0\n')# has to ndividualize for diff freq
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write("OBOXFILE 'BOX:hope1."+userid+"."+str(lm)+"\n")
    writethat.write('aparm(7) 10\n')
    writethat.write('aparm(6) 1\n')

    writethat.write('dowait true \n')

    writethat.write('go sabox\n')
    writethat.write('wait sabox; end\n\n')
    
    writethat.write('x=j+1\n')
    writethat.write('dist = x+2*nfield-1\n')
    writethat.write('for i =x to dist; getn i;clrstat; zap; end\n\n')
    
    writethat.write("task 'imagr'\n")
    writethat.write("INNAME   ' '                        \n")
    writethat.write("INCLASS     ' '                         \n")
    writethat.write("INSEQ          0                       \n")
    writethat.write("INDISK       0                     \n")
    writethat.write("SOURCES      ' '                 \n")
    writethat.write("QUAL           -1                      \n")
    writethat.write("CALCODE     ' '                         \n")
    writethat.write("TIMERANG    0                   \n")
    writethat.write("SELBAND        -1                      \n")
    writethat.write("SELFREQ        -1                      \n")
    writethat.write("FREQID      -1                     \n")
    writethat.write("SUBARRAY       0                       \n")
    writethat.write("ANTENNAS    0                   \n")
    writethat.write("BASELINE    0                   \n")
    writethat.write("GAINUSE         0                      \n")
    writethat.write("DOPOL        -1                        \n")
    writethat.write("PDVER          0                       \n")
    writethat.write("BLVER        -1                        \n")
    writethat.write("FLAGVER         0                      \n")
    writethat.write("DOBAND      -1                     \n")
    writethat.write("BPVER        -1                        \n")
    writethat.write("SMOOTH     0                    \n")
    writethat.write("STOKES   ' '                        \n")
    writethat.write("BCHAN          1                       \n")
    writethat.write("ECHAN          0                       \n")
    writethat.write("CHINC          1                       \n")
    writethat.write("BIF              0                     \n")
    writethat.write("EIF              0                     \n")
    writethat.write("OUTNAME     ' '                         \n")
    writethat.write("OUTDISK         1                      \n")
    writethat.write("OUTSEQ       0                     \n")
    writethat.write("OUTVER       0                     \n")
    writethat.write("IN2NAME     ' '                         \n")
    writethat.write("IN2CLASS   ' '                      \n")
    writethat.write("IN2SEQ       0                     \n")
    writethat.write("IN2DISK         0                      \n")
    writethat.write("DO3DIMAG     -1                        \n")
    writethat.write("FLDSIZE      0                  \n")
    writethat.write("RASHIFT      0                  \n")
    writethat.write("DECSHIFT    0                   \n")
    writethat.write("UVTAPER         0            0     \n")
    writethat.write("UVRANGE         0            0     \n")
    writethat.write("GUARD          0             0     \n")
    writethat.write("ROTATE       0                     \n")
    writethat.write("ZEROSP     0                    \n")
    writethat.write("UVWTFN   ' '                        \n")
    writethat.write("UVSIZE       0           0     \n")
    writethat.write("ROBUST       0                     \n")
    writethat.write("UVBOX          0                       \n")
    writethat.write("UVBXFN       1                     \n")
    writethat.write("XTYPE          5                       \n")
    writethat.write("YTYPE          5                       \n")
    writethat.write("XPARM       0                   \n")
    writethat.write("YPARM       0                   \n")
    writethat.write("NITER          0                       \n")
    writethat.write("BCOMP       0                   \n")
    writethat.write("ALLOKAY         0                      \n")
    writethat.write("NBOXES       0                     \n")
    writethat.write("CLBOX       0                   \n")
    writethat.write("BOXFILE      ' '                 \n")
    writethat.write("OBOXFILE    ' '                  \n")
    writethat.write("GAIN            0.1                     \n")
    writethat.write("MINPATCH     51                        \n")
    writethat.write("BMAJ            0                      \n")
    writethat.write("BMIN            0                      \n")
    writethat.write("BPA              0                     \n")
    writethat.write("OVERLAP         0                      \n")
    writethat.write("ONEBEAM         0                      \n")
    writethat.write("OVRSWTCH       0                       \n")
    writethat.write("PHAT            0                      \n")
    writethat.write("FACTOR       0                     \n")
    writethat.write("CMETHOD     ' '                         \n")
    writethat.write("IMAGRPRM    0                   \n")
    writethat.write("IMAGRPRM    0                   \n")
    writethat.write("IM2PARM      0                  \n")
    writethat.write("NGAUSS       0                     \n")
    writethat.write("WGAUSS     0                    \n")
    writethat.write("FGAUSS     0                    \n")
    writethat.write("MAXPIXEL   20000                     \n")
    writethat.write("IN3NAME     ' '                         \n")
    writethat.write("IN3CLASS   ' '                      \n")
    writethat.write("IN3SEQ       0                     \n")
    writethat.write("IN3DISK         0                      \n")
    writethat.write("IN4NAME     ' '                         \n")
    writethat.write("IN4CLASS   ' '                      \n")
    writethat.write("IN4SEQ       0                     \n")
    writethat.write("IN4DISK         0                      \n")
    writethat.write("FQTOL        -1                        \n")
    writethat.write("DOTV           -1                      \n")
    writethat.write("LTYPE          3                       \n")
    writethat.write("BADDISK      0                  \n")


    writethat.write('getn j\n')
    writethat.write('channel 0\n')
    if fracband>0.12:
        writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
        writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
        writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
    else:
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      
    #writethat.write('flux '+str(rms_tot[i-1]*5)+'\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    writethat.write('robust 0       \n')  
      
    writethat.write('im2parm 1 5 7 0.05 0 0 0 1 1 0\n')
    writethat.write('dotv -1\n')
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    writethat.write('niter '+str(int(niter))+'\n')                   
    writethat.write('flux =kk \n')    
    writethat.write("BOXFILE 'BOX:hope1."+userid+"."+str(lm)+"\n")
    writethat.write('uvrange '+uvlow+' 0\n')

    writethat.write('dowait true \n')
    writethat.write("stokes 'I'\n")
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write('recat \n')
    writethat.write("clrmsg \n")
    writethat.write('x = 2*nfield+j-1 \n')
    writethat.write('dist= x \n')
    writethat.write("task 'imean' \n default \n")
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('kk=3.5*kk/6 \n')

    writethat.write('x = nfield+j+1 \n')
    writethat.write("tget calib\n")
    writethat.write('default \n')
    writethat.write('x = nfield+j+1 \n')
    writethat.write('getn j \n')
    writethat.write('ncomp = -1000000\n')
    writethat.write('get2n x \n')
    writethat.write('aparm(9) 1 \n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')

    if fracband>0.12:
        writethat.write('ICHANSEL '+str(chav1[i-1]/2-chav1[i-1]/freq_cl)+' '+str(chav1[i-1]/2+chav1[i-1]/freq_cl)+' 1 0\n')#adjust with no of freq
    else:
        writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 2.5\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'P' \n")
    writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write("clrmsg \n")
    writethat.write('x = x-nfield-1 \n')
    writethat.write('x = 2*nfield+x+1 \n')
      
    writethat.write("task 'sabox'\n")
    writethat.write("inclass 'ICL001'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    

    writethat.write('aparm 4 6 0\n')# has to ndividualize for diff freq
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write("OBOXFILE 'BOX:hope2."+userid+"."+str(lm)+"\n")
    writethat.write('aparm(7) 10\n')
    writethat.write('aparm(6) 1\n')


    writethat.write('dowait true \n')
    writethat.write('go sabox\n')
    writethat.write('wait sabox; end\n\n')
    


    writethat.write("task 'imagr'\n")
    writethat.write("im2parm 3 4 6 0.05 0 0 0 1 1 0 \n")#dont put default. becoz we have to catch the returned values by setfc...go through all the inputs modified and change them.

    

    writethat.write('getn x\n')
    writethat.write("in2nam ''\n")
    writethat.write("in2clas ''\n")
    writethat.write("in2s 0 \n")
    writethat.write('channel 0\n')
    #writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      
    writethat.write('flux = kk\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    #writethat.write('uvrange '+uvlow+' 0   \n')        
    writethat.write('robust 0       \n')        
    writethat.write('niter 50000\n')                     
    writethat.write("BOXFILE 'BOX:hope2."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    if fracband>0.12:
        writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
        writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
        writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
    else:
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      

    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    writethat.write('uvrange '+uvlow+' 0\n')
    writethat.write('dowait true \n')
    writethat.write("stokes 'I'\n")
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrstat \n")
    writethat.write("recat \n")
    writethat.write("clrmsg \n")    
    writethat.write('num = 2*nfield+x-1 \n')
    writethat.write('dist= num \n')
    writethat.write('tget imean \n default \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write(' kk = 2.7*kk/6 \n\n')
    writethat.write('num = nfield+x+1 \n')
    writethat.write("tget calib \n")
    writethat.write('default \n')
    writethat.write('getn j \n')
    writethat.write("inext 'sn' \n")
    writethat.write('extd \n')  
    writethat.write('x = nfield+x+1 \n')
    writethat.write('get2n x \n')
    writethat.write('ncomp = -1000000\n')
    writethat.write('aparm(7) 3\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    if fracband>0.12:
        writethat.write('ICHANSEL '+str(chav1[i-1]/2-chav1[i-1]/freq_cl)+' '+str(chav1[i-1]/2+chav1[i-1]/freq_cl)+' 1 0\n')#adjust with no of freq
    else:
        writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 1.25\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'P' \n")
    writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')

    writethat.write('x = x-nfield-1 \n')
    
    writethat.write('x = 2*nfield+x+1 \n')
 
    if weighting=='natural':     
        writethat.write("task 'imagr'\n")
        writethat.write("im2parm 10 3 5 0.01 0 0 0 1 1 0 \n")
    
        writethat.write('getn x\n')
        writethat.write("in2nam ''\n")
        writethat.write("in2clas ''\n")
        writethat.write("in2s 0 \n")
        writethat.write('channel 0\n')
        #writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize
        if fracband>0.12:
            writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
            writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
            writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
        else:
            writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      
    
        writethat.write('flux = kk\n')# calculate on the basis of noise
        writethat.write('docal -1       \n')    
        writethat.write('do3dima 1      \n')    
        writethat.write('overlap 2      \n')    
        #writethat.write('uvrange '+uvlow+' 0   \n') 


        writethat.write('robust 5       \n')         
            
        writethat.write('niter 0\n')                     
        writethat.write("BOXFILE 'BOX:hope2."+userid+'.'+str(lm)+"\n")
        writethat.write('dotv -1\n')
        #writethat.write('wgauss 0, 30, 90, 270\n')
        #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
        #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
        #writethat.write('uvrange '+uvlow+' 0\n')
        writethat.write('dowait true \n')
        writethat.write("stokes 'I'\n")
        writethat.write('go imagr; wait imagr; end\n \n')
        writethat.write('recat \n')
        writethat.write("clrmsg \n")
        writethat.write("default gethead\n")
        writethat.write("num=x+1+nfield\n")
        writethat.write("getn num\n")
        writethat.write("keyword 'bmin'\n")
        writethat.write("go gethead\n")
        writethat.write("cell = keyvalue(1)*3600/4\n")
    
        writethat.write('num=x+1\n')
        writethat.write('dist = x+2*nfield\n')
        writethat.write('for i =num to dist; getn i;clrstat; zap; end\n\n')
    
        writethat.write("task 'setfc'\n")
        writethat.write('getn x\n')
        writethat.write('imsize 0\n')
    
        writethat.write('bparm '+str(pb)+' 2 0\n')# has to ndividualize for diff freq
        writethat.write("BOXFILE 'BOX:hope3_1."+userid+'.'+str(lm)+"\n")
        writethat.write('go setfc; wait setfc; end\n')
        writethat.write('go setfc; wait setfc; end\n')


        writethat.write("task 'sabox'\n")
        writethat.write("inclass 'ICL001'  \n")
        writethat.write('inname  ')
        writethat.write("'"+field_names[y]+"'")
        writethat.write("\n")
        writethat.write("INSEQ          2 \n")
        
    
        writethat.write('aparm 5 7 0\n')# has to ndividualize for diff freq
        writethat.write("BOXFILE 'BOX:hope3_1."+userid+"."+str(lm)+"\n")
        writethat.write("OBOXFILE 'BOX:hope3."+userid+"."+str(lm)+"\n")
        writethat.write('aparm(7) 10\n')
        writethat.write('aparm(6) 1\n')
    else:
        writethat.write("task 'sabox'\n")
        writethat.write("inclass 'ICL001'  \n")
        writethat.write('inname  ')
        writethat.write("'"+field_names[y]+"'")
        writethat.write("\n")
        writethat.write("INSEQ          2 \n")
        
    
        writethat.write('aparm 5 7 0\n')# has to ndividualize for diff freq
        writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
        writethat.write("OBOXFILE 'BOX:hope3."+userid+"."+str(lm)+"\n")
        writethat.write('aparm(7) 10\n')
        writethat.write('aparm(6) 1\n')
        

    writethat.write('go sabox\n')
    writethat.write('dowait true \n')
    writethat.write('wait sabox; end\n\n')

    writethat.write("task 'imagr'\n")
    writethat.write("im2parm 10 3 5 0.01 0 0 0 1 1 0 \n")

    writethat.write('getn x\n')
    writethat.write("in2nam ''\n")
    writethat.write("in2clas ''\n")
    writethat.write("in2s 0 \n")
    writethat.write('channel 0\n')
    #writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize
    if fracband>0.12:
        writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
        writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
        writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
    else:
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      

    writethat.write('flux = kk\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    #writethat.write('uvrange '+uvlow+' 0   \n') 
    writethat.write('robust 0       \n')    
    if weighting=='natural': 
        writethat.write('robust 5       \n')         
        
    writethat.write('niter 50000\n')                     
    writethat.write("BOXFILE 'BOX:hope3."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    #writethat.write('uvrange '+uvlow+' 0\n')
    writethat.write('dowait true \n')
    writethat.write("stokes 'I'\n")
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrstat \n")
    writethat.write("clrmsg \n")
    writethat.write("recat \n")
    #for flim in range(2*field_lim):
    	#writethat.write('num = x+1+'+str(flim)+' \n')	
    	#writethat.write("getn num; geto num; outse 3; rename ;end\n")  

    writethat.write('num = 2*nfield+x-1 \n')
    writethat.write('dist= num \n')
    writethat.write('tget imean \n default \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write(' kk = 2.2*kk/6 \n\n')

    writethat.write('num = nfield+x+1 \n')

    writethat.write("clrmsg \n")
    writethat.write("clrmsg \n")
    writethat.write("tget calib \n")
    writethat.write('default \n')
    writethat.write('getn j \n')
    writethat.write("inext 'sn' \n")
    writethat.write('extd \n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('x = nfield+x+1 \n')
    writethat.write('get2n x \n')
    writethat.write('ncomp = -1000000\n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    if fracband>0.12:
        writethat.write('ICHANSEL '+str(chav1[i-1]/2-chav1[i-1]/freq_cl)+' '+str(chav1[i-1]/2+chav1[i-1]/freq_cl)+' 1 0\n')#adjust with no of freq
    else:
        writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 0.5\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'P' \n")
    #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write("clrmsg \n")
    writethat.write('x = x-nfield-1 \n')
    
    writethat.write('x = 2*nfield+x+1 \n')
        
    writethat.write("task 'sabox'\n")
    writethat.write("inclass 'ICL001'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          3 \n")
    

    writethat.write('aparm 3.5 7.5 0\n')# has to ndividualize for diff freq
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write("OBOXFILE 'BOX:hope4."+userid+"."+str(lm)+"\n")
    writethat.write('aparm(7) 10\n')
    writethat.write('aparm(6) 1\n')


    writethat.write('go sabox\n')
    writethat.write('dowait true \n')
    writethat.write('wait sabox; end\n\n')
    
    writethat.write("task 'imagr'\n")
    writethat.write("im2parm 30 2.5 4.5 0.01 0 0 0 1 1 0 \n")
    writethat.write('getn x\n')
    writethat.write("in2nam ''\n")
    writethat.write("in2clas ''\n")
    writethat.write("in2s 0 \n")
    writethat.write('channel 0\n')

    if fracband>0.12:
        writethat.write('nchav '+str(chav1[i-1]/freq_cl+1)+'\n')#individualize3.
        writethat.write("BCHAN          "+str(chav1[i-1]/2-chav1[i-1]/freq_cl/2)+"                      \n")
        writethat.write("ECHAN          "+str(chav1[i-1]/2+chav1[i-1]/freq_cl/2)+"                      \n")
    else:
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize3.      


    writethat.write('flux =kk\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    writethat.write('uvrange 0  \n')        
    writethat.write('robust 0       \n')        
    writethat.write('niter 500000\n')                    
    writethat.write("BOXFILE 'BOX:hope4."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    if weighting=='natural': 
        writethat.write('robust 5       \n')  
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    #writethat.write('uvrange '+uvlow+' 0\n')
    writethat.write('dowait true \n')
    writethat.write("stokes 'I'\n")
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrstat \n")
    writethat.write("recat \n")
    #for flim in range(2*field_lim):
    	#writethat.write('num = x+1+'+str(flim)+' \n')	
    	#writethat.write("getn num; geto num; outse 4; rename ;end\n")    f
    writethat.write("clrmsg \n")
    writethat.write('num = 2*nfield+x-1 \n')
    writethat.write('dist= num \n')
    writethat.write("task 'imean' \n")
    writethat.write('default \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean \n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write("keyword 'ACTNOISE' \n \n")
    writethat.write("gethead \n \n")

    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write('getn dist \n')

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write(' kk = 2*kk/6 \n\n')

    writethat.write("task 'uvsub'\n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('x = nfield+x+1 \n')
    writethat.write('get2n x \n')
    writethat.write('nmaps nfield \n')
    writethat.write('ncomp -1000000 \n')
    writethat.write('dowait true \n')
    writethat.write('go uvsub; wait uvsub; end\n\n')

    writethat.write('x = nfield+x \n')


    writethat.write("task 'rflag' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('outfgver 1 \n')
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20  \n")
    writethat.write("NOISE "+str(mf*sens)+" \n")
    writethat.write("SCUTOFF "+str(10*mf*sens)+" \n")
    writethat.write("STOKE 'RR' \n")
    writethat.write('dowait true \n')
    #writethat.write('go rflag; wait rflag; end\n \n')

    writethat.write("task 'rflag' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('outfgver 1 \n')
    writethat.write('uvrange '+uvlow+' 0     \n')       
    writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20 \n")
    writethat.write("NOISE "+str(mf*sens)+" \n")
    writethat.write("SCUTOFF "+str(10*mf*sens)+" \n")
    writethat.write("STOKE 'LL' \n")
    writethat.write('dowait true \n')


    writethat.write("task 'rflag' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('outfgver 1 \n')
    writethat.write('uvrange 0 '+uvlow+'    \n')       
    writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20  \n")
    writethat.write("NOISE "+str(1.5*mf*sens)+" \n")
    writethat.write("SCUTOFF "+str(15*mf*sens)+" \n")
    writethat.write("STOKE 'RR' \n")
    writethat.write('dowait true \n')
    #writethat.write('go rflag; wait rflag; end\n \n')

    writethat.write("task 'rflag' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('outfgver 1 \n')
    writethat.write('uvrange 0 '+uvlow+'      \n')       
    writethat.write("FPARM   5,"+str(median_integration_time)+",-1,-1,0.001,1,0.85,2,7,7,0.75,0.75,50,20 \n")
    writethat.write("NOISE "+str(1.5*mf*sens)+" \n")
    writethat.write("SCUTOFF "+str(15*mf*sens)+" \n")
    writethat.write("STOKE 'LL' \n")
    writethat.write('dowait true \n')
    #writethat.write('go rflag; wait rflag; end\n \n')


    writethat.write("task 'flagr' \n")
    writethat.write('default \n')

    #writethat.write('cparm 1e-8 100 1e-9 '+str(clip)+' '+str(mf*sens)+' 0 7.5 30 10 50\n')
    #writethat.write('bparm 0.75 0.5 0  \n')
    writethat.write('getn x \n')
    writethat.write("source ''\n")
    writethat.write('outfgver 1 \n')
    writethat.write('dowait true \n')
    #writethat.write('go flagr; wait flagr; end\n \n')


    writethat.write("task 'flgit' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('aparm '+str(10*mf*sens)+' '+str(mf*sens)+' '+str(mf*sens)+' 0 \n')
    writethat.write("outfgver 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go flgit; wait flgit; end\n \n')
    
    writethat.write("task 'tacop' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write('x =x-2*nfield-1 \n')
    writethat.write('geto x \n')    
    writethat.write("inext 'fg' \n")
    writethat.write('dowait true \n')
    writethat.write('go tacop; wait tacop; end\n \n')
    writethat.write("task 'tacop' \n")
    writethat.write('default \n')
    writethat.write('getn x \n')
    writethat.write("outclass 'SPLIT'  \n")
    writethat.write('outname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("OUTSEQ          1 \n")
    writethat.write("inext 'fg' \n")
    writethat.write('dowait true \n')
    writethat.write('go tacop; wait tacop; end\n ')
    writethat.write('x =x+2*nfield+1 \n')   
    writethat.write('getn x \n')
    writethat.write('clrstat;zap \n')   
    
       
    
    writethat.write('x =x-2*nfield-1 \n')
    writethat.write("tget uvcop \n")
    writethat.write('default \n')
    if fracband>0.12:
        writethat.write('getn j \n')
        writethat.write('flagver 2 \n')
        writethat.write('dowait true \n')
        writethat.write('go uvcop; wait uvcop; end\n\n')
        writethat.write('getn j; zap; \n\n')
        writethat.write('getn x; slot j; renumber \n\n')
        writethat.write("getn j; outclass 'SPLIT'; rename \n\n")

    writethat.write("tget calib \n")
    writethat.write('default \n')
    if fracband>0.12:
        writethat.write('getn j \n')
        writethat.write('ICHANSEL '+str(chav1[i-1]/2-chav1[i-1]/freq_cl)+' '+str(chav1[i-1]/2+chav1[i-1]/freq_cl)+' 1 0\n')
        writethat.write('solint 0.5\n')#adjust with no of freq
        writethat.write("SOLMODE     'P' \n")
    else:
        writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
        writethat.write("SOLMODE     'A&P' \n")
        writethat.write('getn x \n')    
        writethat.write('solint 4\n')

    writethat.write('x = nfield+x+1 \n')
    writethat.write('get2n x \n')
    writethat.write('ncomp = -1000000\n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")

    writethat.write("normaliz 1 \n")
    #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write('x = x-nfield-1 \n')
    
    writethat.write('x = 2*nfield+x+1 \n')
    if fracband<0.12:  
        writethat.write("y = x+nfield+1 \n")
        writethat.write("task 'sabox'\n")
        writethat.write("inclass 'ICL001'  \n")
        writethat.write('inname  ')
        writethat.write("'"+field_names[y]+"'")
        writethat.write("\n")
        writethat.write("INSEQ          4 \n")
        
    
        writethat.write('aparm 4 6 0\n')# has to ndividualize for diff freq
        writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
        writethat.write("OBOXFILE 'BOX:hope5."+userid+"."+str(lm)+"\n")
        writethat.write('aparm(7) 10\n')
        writethat.write('aparm(6) 1\n')
    
    
        writethat.write('go sabox\n')
        writethat.write('dowait true \n')
        writethat.write('wait sabox; end\n\n')
    
        writethat.write("task 'imagr'\n")
        writethat.write('getn x\n')
        writethat.write("in2nam ''\n")
        writethat.write("in2clas ''\n")
        writethat.write("in2s 0 \n")
        writethat.write('channel 0\n')
        writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize
        writethat.write('flux =kk\n')# calculate on the basis of noise
        writethat.write('docal -1       \n')    
        writethat.write('do3dima 1      \n')    
        writethat.write('overlap 2      \n')    
        writethat.write('uvrange 0  \n')        
        writethat.write('robust 0       \n')        
        writethat.write('niter 500000\n')                    
        writethat.write("BOXFILE 'BOX:box."+userid+'.'+str(lm)+"\n")
        writethat.write('im2parm 0\n')
        writethat.write('dotv -1\n')
        #writethat.write('wgauss 0, 30, 90, 270\n')
        #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
        #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
        if weighting=='natural': 
           writethat.write('robust 5       \n')  
        writethat.write('dowait true \n')
        writethat.write("stokes 'I'\n")
        writethat.write('go imagr; wait imagr; end\n \n')
        writethat.write("clrstat \n")
        writethat.write("clrmsg \n")
        writethat.write("recat \n")
        #for flim in range(2*field_lim):
            #writethat.write('num = x+1+'+str(flim)+' \n')   
            #writethat.write("getn num; geto num; outse 5; rename ;end\n")  
        
    
    
        writethat.write("num =imsize(1)*(nfield)**0.5 \n")
        for i in range(0,5):
            writethat.write("task 'flatn' \n")
            writethat.write("aparm 0 \n")
            writethat.write("getn y \n")
            writethat.write("imsize num\n")
            writethat.write("nmaps 1 \n")
            writethat.write('dowait true \n')
            writethat.write("go flatn; wait flatn; end \n\n")
            writethat.write("y = y-2*nfield-1 \n")
        
        writethat.write("task 'pbcor'\n")
        writethat.write('default \n')
        writethat.write('x = x+2*nfield+1 \n')
        writethat.write('getn x \n')
        writethat.write("PBPARM(1)=0.1\n")
        writethat.write("PBPARM(2)=1\n")
        writethat.write("PBPARM(3)="+str(pba)+"\n")
        writethat.write("PBPARM(4)="+str(pbb)+"\n")
        writethat.write("PBPARM(5)="+str(pbc)+"\n")
        writethat.write("PBPARM(6)="+str(pbd)+"\n")
        writethat.write("PBPARM(7)=0\n")
        writethat.write('dowait true \n')
        writethat.write('go pbcor \n')
        writethat.write('wait pbcor \n\n')
        writethat.write("clrmsg \n")


        writethat.write('x = x+5 \n')
        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        writethat.write('getn x \n')
        writethat.write("dataout 'OUT:im/"+field_names[y]+"_"+name[-20:]+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')
        writethat.write("i = x\n")
        
        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        writethat.write('getn x \n')
        writethat.write('inse 4 \n')
        writethat.write("inclass 'FLATN' \n'")                
        writethat.write("dataout 'OUT:im/"+field_names[y]+"_"+name[-18:]+"p3.fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')
        writethat.write("i = x\n")
 

        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        writethat.write('y =x-2*nfield-6\n')
        writethat.write('getn y \n')
        writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-20:]+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')

        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        #writethat.write('y =x-2*nfield-6\n')
        writethat.write('getn j \n')
        writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-14:]+"_split"+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')
        writethat.write('x = x+nfield+1 \n')
    
        if npols==4:
        	writethat.write("tget imagr\n")
        	#writethat.write('getn x\n')
        	writethat.write("stokes 'q'\n")
        	writethat.write('flux =0.85*kk\n')# calculate on the basis of noise
        	writethat.write('dowait true \n')
        	writethat.write('go imagr; wait imagr; end\n \n')
        	writethat.write("clrstat \n")
        	writethat.write("clrmsg \n")
        	writethat.write("recat \n")        

        	writethat.write("tget 'imagr'\n")
        	#writethat.write('getn x\n')
        	writethat.write("stokes 'u'\n")
        	writethat.write('flux =0.85*kk\n')# calculate on the basis of noise
        	#writethat.write('wgauss 0, 30, 90, 270\n')
        	#writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
        	#writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
        	if weighting=='natural': 
        	   writethat.write('robust 5       \n')  
        	writethat.write('dowait true \n')
        	writethat.write('go imagr; wait imagr; end\n \n')
        	writethat.write("clrstat \n")
        	writethat.write("clrmsg \n")
        	writethat.write("recat \n")

        	writethat.write("task 'flatn' \n")
        	writethat.write("aparm 0 \n")
        	writethat.write("getn x \n")
        	writethat.write("imsize num\n")
        	writethat.write("nmaps 1 \n")
        	writethat.write('dowait true \n')
        	writethat.write("go flatn; wait flatn; end \n\n")
        	#writethat.write("y = y-2*nfield-1 \n")
        	writethat.write('x = x+2*nfield \n')
	
        	writethat.write("task 'flatn' \n")
        	writethat.write("aparm 0 \n")
        	writethat.write("getn x \n")
        	writethat.write("imsize num\n")
        	writethat.write("nmaps 1 \n")
        	writethat.write('dowait true \n')
        	writethat.write("go flatn; wait flatn; end \n\n")
        	#writethat.write("y = y-2*nfield-1 \n")
        	writethat.write('x = x+2*nfield \n')
        	writethat.write("task 'pbcor'\n")
        	writethat.write('default \n')
        	#writethat.write('x = x+2*nfield+1 \n')
        	writethat.write('getn x \n')
        	writethat.write("PBPARM(1)=0.1\n")
        	writethat.write("PBPARM(2)=1\n")
        	writethat.write("PBPARM(3)="+str(pba)+"\n")
        	writethat.write("PBPARM(4)="+str(pbb)+"\n")
        	writethat.write("PBPARM(5)="+str(pbc)+"\n")
        	writethat.write("PBPARM(6)="+str(pbd)+"\n")
        	writethat.write("PBPARM(7)=0\n")
        	writethat.write('dowait true \n')
        	writethat.write('go pbcor \n')
        	writethat.write('wait pbcor \n\n')
        	writethat.write("clrmsg \n")
	
        	writethat.write("task 'pbcor'\n")
        	writethat.write('default \n')
        	writethat.write('x = x+1 \n')
        	writethat.write('getn x \n')
        	writethat.write("PBPARM(1)=0.1\n")
        	writethat.write("PBPARM(2)=1\n")
        	writethat.write("PBPARM(3)="+str(pba)+"\n")
        	writethat.write("PBPARM(4)="+str(pbb)+"\n")
        	writethat.write("PBPARM(5)="+str(pbc)+"\n")
        	writethat.write("PBPARM(6)="+str(pbd)+"\n")
        	writethat.write("PBPARM(7)=0\n")
        	writethat.write('dowait true \n')
        	writethat.write('go pbcor \n')
        	writethat.write('wait pbcor \n\n')
        	writethat.write("clrmsg \n")
        	writethat.write('i = x \n')

    else:
        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        #writethat.write('y =x-2*nfield-6\n')
        writethat.write('getn x \n')
        writethat.write('i = x \n')
        writethat.write('bw = x \n')
        writethat.write('tt = x \n')
        writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-20:]+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')

        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        writethat.write('y=x-nfield\n')
        writethat.write('getn y \n')
        writethat.write("dataout 'OUT:im/"+field_names[y]+"_"+name[-20:]+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')

        writethat.write("task 'fittp'\n")
        writethat.write('default \n')
        #writethat.write('y =x-2*nfield-6\n')
        writethat.write('getn j \n')
        writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-14:]+"_split"+".fits\n")
        writethat.write('dowait true \n')
        writethat.write('go fittp \n')
        writethat.write('wait fittp \n\n')

    writethat.close()    
    os.system('rm -rf '+outputfolder+'/im')
    os.system('mkdir '+outputfolder+'/im')
    
    os.system('rm -rf '+outputfolder+'/uv')
    os.system('mkdir '+outputfolder+'/uv')
    
    
    
    

if (nophase==0):
    phase_fiel=flux_fiel
writethat = open(home+'/.aips/RUN/SCRPT0.'+userid,"w")
writethat.write('$\n')


for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)
    writethat.write('bw=x \n') # calib file 
    writethat.write("task 'fitld'\n")
    writethat.write('default \n')
    writethat.write("datain 'OUT:im/"+field_names[y]+"_"+name[-6:]+"casa0.fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fitld \n')
    writethat.write('wait fitld \n\n')

    writethat.write("tget calib \n")
    writethat.write('default \n')
    writethat.write("x=bw+1  \n")
    writethat.write('get2n x \n')
        
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")



    writethat.write("inext 'sn' \n")
    writethat.write('extd \n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 1.25\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'P' \n")
    writethat.write("CMODEL  'IMAG' \n")
    #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps 1 \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write("clrmsg \n")

    #writethat.write("inclass 'CALIB'  \n")
    #writethat.write('inname  ')
    #writethat.write("'"+field_names[y]+"'")
    #writethat.write("\n")
    #writethat.write("INSEQ         3 \n")
    writethat.write('x=bw+2 \n') # calib file   

    writethat.write("task 'fittp'\n")
    writethat.write('default \n')
    writethat.write('y =bw+2\n')
    writethat.write('getn y \n')
    writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-12:]+"_calib1.fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fittp \n')
    writethat.write('wait fittp \n\n')

 

writethat.close()

    



if fracband>0.12:
    for i in range(1,notarg+1):
        lm=i
        x=(target_fiel[i-1])
        y=int(x)
        writethat = open(home+'/.aips/RUN/SCRIPT'+str(i)+'.'+userid,"w")
        writethat.write('$\n')
        writethat.write('bw=x \n') # calib file       
    
        for freq_c in range(1,freq_cl+1):
    
    
            writethat.write("task 'split' \n")#rembr to change bak to split
            writethat.write('default \n')
            writethat.write("inclass 'SPLIT'  \n")
            writethat.write('inname  ')
            writethat.write("'"+field_names[y]+"'")
            writethat.write("\n")
            writethat.write("INSEQ          1 \n")
    
    
            writethat.write('bchan '+str(chavgw[i-1]*(freq_c-1)+1)+' \n')
            writethat.write('echan '+str(chavgw[i-1]*(freq_c))+' \n')
    
            writethat.write('ichansel '+str(1+chavgw[i-1]*(freq_c-1))+' '+str(chavgw[i-1]*(freq_c))+' 1 0  \n')
    
            writethat.write('dowait true \n')
            writethat.write('go split; wait split; end\n \n')
    
            writethat.write("task 'split' \n")#rembr to change bak to split
            writethat.write('default \n')
            #writethat.write("y=bw+2 \n")
            writethat.write("inclass 'CALIB'  \n")
            writethat.write('inname  ')
            writethat.write("'"+field_names[y]+"'")
            writethat.write("\n")
            writethat.write("INSEQ          3 \n")
    
            writethat.write("x=x+1 \n")
    
    
            writethat.write('bchan '+str(chavgw[i-1]*(freq_c-1)+1)+' \n')
            writethat.write('echan '+str(chavgw[i-1]*(freq_c))+' \n')
    
            writethat.write('ichansel '+str(1+chavgw[i-1]*(freq_c-1))+' '+str(chavgw[i-1]*(freq_c))+' 1 0  \n')
    
        
            writethat.write('dowait true \n')
            writethat.write('go split; wait split; end\n \n')   
            os.system('rm -rf '+home+'/.boxfiles/hope1.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope2.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope3.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope4.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope5.'+userid+'.'+str(freq_c)+'_'+str(lm))
            syscommand='rm -rf '+home+'/.boxfiles/box.'+userid+'.'+str(freq_c)+'_'+str(lm)
            os.system(syscommand)
            #writethat.write("i=x\n")
            writethat.write("task 'setfc'\n")
            writethat.write('default\n')
            writethat.write('j=1+x \n')
            writethat.write('getn j\n')
            writethat.write('bparm '+str(pb)+' 2 0\n')# has to ndividualize for diff freq
            writethat.write('dowait true \n')
            writethat.write("BOXFILE 'BOX:box."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('go setfc; wait setfc; end\n')
            writethat.write('go setfc; wait setfc; end\n')
            writethat.write('wait setfc; end\n\n')
            os.system('rm -rf '+home+'/.boxfiles/hope1.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope2.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope3.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope4.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/hope5.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/box.'+userid+'.'+str(freq_c)+'_'+str(lm))
            os.system('rm -rf '+home+'/.boxfiles/obox.'+userid+'.'+str(freq_c)+'_'+str(lm))
    
            writethat.write("clrmsg \n")
    
        
            writethat.write("task 'sabox'\n")
            writethat.write("inclass 'ICL001'  \n")
            writethat.write('inname  ')
            writethat.write("'"+field_names[y]+"'")
            writethat.write("\n")
            writethat.write("INSEQ  2 \n")
            
            
            writethat.write('aparm 5 7 0\n')# has to ndividualize for diff freq
            writethat.write("BOXFILE 'BOX:box."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write("OBOXFILE 'BOX:hope2."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('aparm(7) 10\n')
            writethat.write('aparm(6) 1\n')
            writethat.write('dowait true \n')
            
            
            writethat.write('go sabox\n')
            writethat.write('wait sabox; end\n\n')
    
            writethat.write('kk=2.5*kk/3 \n')
    
    
    
    
            writethat.write("task 'imagr'\n")
            writethat.write("INNAME     ' '                   \n")
            writethat.write("INCLASS    ' '                   \n")
            writethat.write("INSEQ         0                  \n")
            writethat.write("INDISK        0                  \n")
            writethat.write("SOURCES     ' '              \n")
            writethat.write("QUAL         -1                  \n")
            writethat.write("CALCODE    ' '                   \n")
            writethat.write("TIMERANG    0                \n")
            writethat.write("SELBAND      -1                  \n")
            writethat.write("SELFREQ      -1                  \n")
            writethat.write("FREQID       -1                  \n")
            writethat.write("SUBARRAY      0                  \n")
            writethat.write("ANTENNAS    0                \n")
            writethat.write("BASELINE    0                \n")
            writethat.write("GAINUSE       0                  \n")
            writethat.write("DOPOL        -1                  \n")
            writethat.write("PDVER         0                  \n")
            writethat.write("BLVER        -1                  \n")
            writethat.write("FLAGVER       0                  \n")
            writethat.write("DOBAND       -1                  \n")
            writethat.write("BPVER        -1                  \n")
            writethat.write("SMOOTH      0                \n")
            writethat.write("STOKES     ' '                   \n")
            writethat.write("BCHAN         1                  \n")
            writethat.write("ECHAN         0                  \n")
            writethat.write("CHINC         1                  \n")
            writethat.write("BIF           0                  \n")
            writethat.write("EIF           0                  \n")
            writethat.write("OUTNAME    ' '                   \n")
            writethat.write("OUTDISK       1                  \n")
            writethat.write("OUTSEQ        0                  \n")
            writethat.write("OUTVER        0                  \n")
            writethat.write("IN2NAME    ' '                   \n")
            writethat.write("IN2CLASS   ' '                   \n")
            writethat.write("IN2SEQ        0                  \n")
            writethat.write("IN2DISK       0                  \n")
            writethat.write("DO3DIMAG     -1                  \n")
            writethat.write("FLDSIZE     0                \n")
            writethat.write("RASHIFT     0                \n")
            writethat.write("DECSHIFT    0                \n")
            writethat.write("UVTAPER       0           0      \n")
            writethat.write("UVRANGE       0           0      \n")
            writethat.write("GUARD         0           0      \n")
            writethat.write("ROTATE        0                  \n")
            writethat.write("ZEROSP      0                \n")
            writethat.write("UVWTFN     ' '                   \n")
            writethat.write("UVSIZE        0           0      \n")
            writethat.write("ROBUST        0                  \n")
            writethat.write("UVBOX         0                  \n")
            writethat.write("UVBXFN        1                  \n")
            writethat.write("XTYPE         5                  \n")
            writethat.write("YTYPE         5                  \n")
            writethat.write("XPARM       0                \n")
            writethat.write("YPARM       0                \n")
            writethat.write("NITER         0                  \n")
            writethat.write("BCOMP       0                \n")
            writethat.write("ALLOKAY       0                  \n")
            writethat.write("NBOXES        0                  \n")
            writethat.write("CLBOX       0                \n")
            writethat.write("BOXFILE     ' '              \n")
            writethat.write("OBOXFILE    ' '              \n")
            writethat.write("GAIN          0.1                \n")
            writethat.write("MINPATCH     51                  \n")
            writethat.write("BMAJ          0                  \n")
            writethat.write("BMIN          0                  \n")
            writethat.write("BPA           0                  \n")
            writethat.write("OVERLAP       0                  \n")
            writethat.write("ONEBEAM       0                  \n")
            writethat.write("OVRSWTCH      0                  \n")
            writethat.write("PHAT          0                  \n")
            writethat.write("FACTOR        0                  \n")
            writethat.write("CMETHOD    ' '                   \n")
            writethat.write("IMAGRPRM    0                \n")
            writethat.write("IMAGRPRM    0                \n")
            writethat.write("IM2PARM     0                \n")
            writethat.write("NGAUSS        0                  \n")
            writethat.write("WGAUSS      0                \n")
            writethat.write("FGAUSS      0                \n")
            writethat.write("MAXPIXEL   20000                 \n")
            writethat.write("IN3NAME    ' '                   \n")
            writethat.write("IN3CLASS   ' '                   \n")
            writethat.write("IN3SEQ        0                  \n")
            writethat.write("IN3DISK       0                  \n")
            writethat.write("IN4NAME    ' '                   \n")
            writethat.write("IN4CLASS   ' '                   \n")
            writethat.write("IN4SEQ        0                  \n")
            writethat.write("IN4DISK       0                  \n")
            writethat.write("FQTOL        -1                  \n")
            writethat.write("DOTV         -1                  \n")
            writethat.write("LTYPE         3                  \n")
            writethat.write("BADDISK     0                \n")
            writethat.write("im2parm 3 4 6 0.05 0 0 0 1 1 0 \n")#dont put default. becoz we have to catch the returned values by setfc...go through all the inputs modified and change them.
            
            writethat.write('bchan '+str(chavgw[i-1]*(freq_c-1)+1)+' \n')
            writethat.write('echan '+str(chavgw[i-1]*(freq_c))+' \n')
            writethat.write('channel 0\n')
            writethat.write('nchav '+str(chavgw[i-1]+1)+'\n')#individualize3.  
            
            writethat.write('getn j\n')
            writethat.write("in2nam ''\n")
            writethat.write("in2clas ''\n")
            writethat.write("in2s 0 \n")
            writethat.write('channel 0\n')
    
            writethat.write('flux = kk\n')# calculate on the basis of noise
            writethat.write('docal -1       \n')    
            writethat.write('do3dima 1      \n')    
            writethat.write('overlap 2      \n')    
            #writethat.write('uvrange '+uvlow+' 0   \n')        
            writethat.write('robust 0       \n')        
            writethat.write('niter 50000\n')                     
            writethat.write("BOXFILE 'BOX:hope2."+userid+'.'+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('dotv -1\n')
            #writethat.write('wgauss 0, 30, 90, 270\n')
            #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
            #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
            #writethat.write('uvrange '+uvlow+' 0\n') 
            if weighting=='natural': 
                writethat.write('robust 5       \n')     
            writethat.write('dowait true \n')
            writethat.write('go imagr; wait imagr; end\n \n')
            writethat.write("clrmsg \n")
            writethat.write("clrstat \n")
            writethat.write('x=j \n')
            writethat.write('x = nfield+x+1 \n')
            ##for randnum in range(field_lim):
                ##writethat.write('x=x+'+str(randnum)+'\n')                
                ##writethat.write('getn x; outse '+str(4+(freq_c-1)*3)+';rename;end\n')

            writethat.write("recat \n")
            writethat.write('x=j \n')
            writethat.write('num = 2*nfield+x-1 \n')
            writethat.write('dist= num \n')
            writethat.write('tget imean \n default \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    
            
            writethat.write('kk=0 \n \n')
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write(' kk = 4*kk/6 \n\n')
            writethat.write('num = nfield+x+1 \n')
    
            writethat.write("clrmsg \n")
            writethat.write("clrmsg \n")
            writethat.write("tget calib \n")
            writethat.write('default \n')
            #writethat.write('j=j-1 \n')
            writethat.write('getn j \n')
            writethat.write("inext 'sn' \n")
            writethat.write('extd \n')
            writethat.write('aparm(7) '+str(calprm7)+'\n')
            writethat.write('aparm(9) '+str(calprm9)+'\n')
            writethat.write('x = nfield+x+1 \n')
            writethat.write('get2n x \n')
            writethat.write('ncomp = -1000000\n')
            writethat.write('aparm(7) '+str(calprm7)+'\n')
            writethat.write('aparm(9) '+str(calprm9)+'\n')
            writethat.write('ICHANSEL 1 '+str(chav1[i-1]/freq_cl-1)+' 1 0\n')#adjust with no of freq
            writethat.write('solint 0.5\n')
            writethat.write('refant '+refAnt+'\n')
            writethat.write("SOLTYPE    'L1R' \n")
            writethat.write("SOLMODE    'P' \n")
            #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
            writethat.write('nmaps nfield \n')
            writethat.write('dowait true \n')
            writethat.write('go calib; wait calib; end\n\n')
            writethat.write("clrmsg \n")
    
            writethat.write("task 'sabox'\n")
    
            writethat.write("getn x \n")
            
            
            writethat.write('aparm 4 6 0\n')# has to ndividualize for diff freq
            writethat.write("BOXFILE 'BOX:box."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write("OBOXFILE 'BOX:hope4."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('aparm(7) 10\n')
            writethat.write('aparm(6) 1\n')
            
            writethat.write('dowait true \n')
            writethat.write('go sabox\n')
            writethat.write('wait sabox; end\n\n')
            writethat.write("x=x+nfield \n")
            
            writethat.write("task 'imagr'\n")
            writethat.write("im2parm 30 2.5 4.5 0.01 0 0 0 1 1 0 \n")
            writethat.write('getn x\n')
            writethat.write("in2nam ''\n")
            writethat.write("in2clas ''\n")
            writethat.write("in2s 0 \n")
            writethat.write('channel 0\n')
    
            writethat.write('nchav '+str(chavgw[i-1]+1)+'\n')#individualize3.  
            writethat.write('flux =kk\n')# calculate on the basis of noise
            writethat.write('docal -1       \n')    
            writethat.write('do3dima 1      \n')    
            writethat.write('overlap 2      \n')    
            writethat.write('uvrange 0  \n')        
            writethat.write('robust 0       \n')        
            writethat.write('niter 500000\n')                    
            writethat.write("BOXFILE 'BOX:hope4."+userid+'.'+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('dotv -1\n')
            writethat.write('dotv -1\n')
            #writethat.write('wgauss 0, 30, 90, 270\n')
            #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
            #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
            if weighting=='natural': 
                writethat.write('robust 5       \n')  
            #writethat.write('uvrange '+uvlow+' 0\n')
            writethat.write('dowait true \n')
            writethat.write('go imagr; wait imagr; end\n \n')
            writethat.write("clrstat \n")
            writethat.write("clrmsg \n")
            writethat.write('dist = nfield+x+1 \n')            
            ##for randnum in range(field_lim):
                #writethat.write('getn dist; outse '+str(5+(freq_c-1)*3)+';rename\n')
                #writethat.write('dist=dist+'+str(randnum)+'\n')

            writethat.write("recat \n")
            writethat.write("clrmsg \n")
            writethat.write('num = 2*nfield+x-1 \n')
            writethat.write('dist= num \n')
            writethat.write("task 'imean' \n")
            writethat.write('default \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean \n  \n")
            #writethat.write('kk = 7*PIXSTD \n \n')
            
            writethat.write('kk=0 \n \n')
            writethat.write("keyword 'ACTNOISE' \n \n")
            writethat.write("gethead \n \n")
            
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write('dist= dist-nfield/10 \n')
            writethat.write('getn dist \n')
            
            writethat.write('dowait true \n')
            writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
            writethat.write('kk=keyval(1)+kk \n')
            writethat.write(' kk = 2*kk/6 \n\n')
            
            writethat.write("task 'uvsub'\n")
            writethat.write('default \n')
            writethat.write('getn x \n')
            writethat.write('x = nfield+x+1 \n')
            writethat.write('get2n x \n')
            writethat.write('nmaps nfield \n')
            writethat.write('ncomp -1000000 \n')
            writethat.write('dowait true \n')
            writethat.write('go uvsub; wait uvsub; end\n\n')
            
            writethat.write('x = nfield+x \n')
            
            writethat.write("task 'flagr' \n")
            writethat.write('default \n')
	    #writethat.write('cparm 1e-8 100 1e-9 '+str(clip)+' '+str(mf*sens)+' 0 7.5 30 10 50\n')
	    #writethat.write('bparm 0.75 0.5 0  \n')

            writethat.write('getn x \n')
            writethat.write("source ''\n")
            writethat.write('outfgver 1 \n')
            writethat.write('dowait true \n')
            #writethat.write('go flagr; wait flagr; end\n \n')

 
            writethat.write("task 'flgit' \n")
            writethat.write('default \n')
            writethat.write('getn x \n')
            writethat.write('aparm '+str(10*mf*sens)+' '+str(mf*sens)+' '+str(mf*sens)+' 0 \n')
            writethat.write("outfgver 1 \n")
            writethat.write('dowait true \n')
            writethat.write('go flgit; wait flgit; end\n \n')
            
            writethat.write("task 'tacop' \n")
            writethat.write('default \n')
            writethat.write('getn x \n')
            writethat.write('x =x-2*nfield-1 \n')
            writethat.write('geto x \n')
            
            writethat.write("inext 'fg' \n")
            writethat.write('dowait true \n')
            writethat.write('go tacop; wait tacop; end\n \n')
            writethat.write('x =x+2*nfield+1 \n')   
            writethat.write('getn x \n')
            writethat.write('clrstat;zap \n')   
            
            
            
            writethat.write('x =x-2*nfield-1 \n')
            
            writethat.write("tget calib \n")
            writethat.write('default \n')
            writethat.write('getn x \n')
            writethat.write('x = nfield+x+1 \n')
            writethat.write('get2n x \n')
            writethat.write('ncomp = -1000000\n')
            writethat.write('aparm(7) '+str(calprm7)+'\n')
            writethat.write('aparm(9) '+str(calprm9)+'\n')
            writethat.write('ICHANSEL 1 '+str(chav1[i-1]/freq_cl-1)+' 1 0\n')#adjust with no of freq
            writethat.write('solint 4\n')
            writethat.write('refant '+refAnt+'\n')
            writethat.write("SOLTYPE    'L1R' \n")
            writethat.write("SOLMODE    'A&P' \n")
            writethat.write("normaliz 1 \n")
            #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
            writethat.write('nmaps nfield \n')
            writethat.write('dowait true \n')
            writethat.write('go calib; wait calib; end\n\n')
    
            writethat.write("task 'sabox'\n")
    
            writethat.write("getn x \n")
            
            
            writethat.write('aparm 4 6 0\n')# has to ndividualize for diff freq
            writethat.write("BOXFILE 'BOX:box."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write("OBOXFILE 'BOX:hope5."+userid+"."+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('aparm(7) 10\n')
            writethat.write('aparm(6) 1\n')
            
            writethat.write('dowait true \n')
            
            writethat.write('go sabox\n')
            writethat.write('wait sabox; end\n\n')
            writethat.write("x=x+nfield \n")
            writethat.write("y=x+1+nfield \n")
            
            writethat.write("task 'imagr'\n")
            writethat.write('getn x\n')
            writethat.write("in2nam ''\n")
            writethat.write("in2clas ''\n")
            writethat.write("in2s 0 \n")
            writethat.write('channel 0\n')
            writethat.write('nchav '+str(chavgw[i-1]+1)+'\n')
            writethat.write('flux =kk\n')# calculate on the basis of noise
            writethat.write('docal -1       \n')    
            writethat.write('do3dima 1      \n')    
            writethat.write('overlap 2      \n')    
            writethat.write('uvrange 0  \n')        
            writethat.write('robust 0       \n')        
            writethat.write('niter 500000\n')                    
            writethat.write("BOXFILE 'BOX:box."+userid+'.'+str(freq_c)+'_'+str(lm)+"\n")
            writethat.write('im2parm 0\n')
            writethat.write('dotv -1\n')
            #writethat.write('wgauss 0, 30, 90, 270\n')
            #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
            #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
            if weighting=='natural': 
                writethat.write('robust 5       \n')         
            #writethat.write('dotv -1\n')
            writethat.write('dowait true \n')
            writethat.write('go imagr; wait imagr; end\n \n')
            writethat.write("clrstat \n")
            writethat.write("clrmsg \n")
            writethat.write('dist = nfield+x+1 \n')            
            ##for randnum in range(field_lim):
                #writethat.write('getn dist; outse '+str(6+(freq_c-1)*3)+';rename\n')
                #writethat.write('dist=dist+'+str(randnum)+'\n')

            writethat.write("recat \n")
            
            
            
            writethat.write("num =imsize(1)*(nfield)**0.5 \n")
            for ff in range(0,2):
                writethat.write("task 'flatn' \n")
                writethat.write("aparm 0 \n")
                writethat.write("getn y \n")
                writethat.write("imsize num\n")
                writethat.write("nmaps 1 \n")
                writethat.write('dowait true \n')
                writethat.write("go flatn; wait flatn; end \n\n")
                writethat.write("y = y-2*nfield-1 \n")
            
            writethat.write("task 'pbcor'\n")
            writethat.write('default \n')
            writethat.write('x = x+2*nfield+1 \n')
            writethat.write('getn x \n')
            writethat.write("PBPARM(1)=0.1\n")
            writethat.write("PBPARM(2)=1\n")
            writethat.write("PBPARM(3)="+str(pba)+"\n")
            writethat.write("PBPARM(4)="+str(pbb)+"\n")
            writethat.write("PBPARM(5)="+str(pbc)+"\n")
            writethat.write("PBPARM(6)="+str(pbd)+"\n")
            writethat.write("PBPARM(7)=0\n")
            writethat.write('dowait true \n')
            writethat.write('go pbcor \n')
            writethat.write('wait pbcor \n\n')
            writethat.write("clrmsg \n")
            
            writethat.write('x = x+2 \n')
            writethat.write("task 'fittp'\n")
            writethat.write('default \n')
            writethat.write('getn x \n')
            writethat.write("dataout 'OUT:im/"+field_names[y]+"_"+name[-15:]+"_"+str(freq_c)+".fits\n")
            writethat.write('dowait true \n')
            writethat.write('go fittp \n')
            writethat.write('wait fittp \n\n')

         
            
            writethat.write("task 'fittp'\n")
            writethat.write('default \n')
            writethat.write('y =x-2*nfield-3\n')
            writethat.write('getn y \n')
            writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-15:]+"_"+str(freq_c)+".fits\n")
            writethat.write('dowait true \n')
            writethat.write('go fittp \n')
            writethat.write('wait fittp \n\n')
         

        writethat.close()

    
writethat = open(home+'/.aips/RUN/KNTR.'+userid,"w")
for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)
    writethat.write("task 'kntr'\n")
    writethat.write('default \n')
    writethat.write("inclass 'PBCOR'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    writethat.write('tvini; tvlo; tvwin;imstat\n')
    writethat.write('kk = 4*PIXSTD  \n')
    writethat.write('clev kk \n ')
    writethat.write("functype 'sq' \n")
    writethat.write('rgblev 0.001\n')
    writethat.write('tvini; tvlo; tvwin;imstat \n')
    writethat.write("dovect -1\n")
    writethat.write("LEVS -2, -1.4, -1, 1 1.4 2 2.8 4 5.6 8 11.2 16 23 32 45 64 90 128 180 256 362 512\n")
    writethat.write("#print pixval/kk \n")   
    writethat.write("pixr kk pixval\n")
    writethat.write("pcut 0.1\n")
    writethat.write('go kntr \n')
    writethat.write('dowait true \n')
    writethat.write('wait kntr \n\n')
 
    writethat.write("task 'lwpla'\n")
    writethat.write('default \n')
    writethat.write("functype 'ne'\n")
    writethat.write("inclass 'PBCOR'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    writethat.write("outfile 'OUT:"+name+"contour."+str(lm)+".ps\n")
    writethat.write('go lwpla \n')
    writethat.write('dowait true \n')
    writethat.write('wait lwpla \n\n')
    writethat.write("tget kntr;ofmfile 'EYEBW '; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'FOTOBW'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY01W'; dotv-1;go;wait kntr;; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY02W'; dotv-1;go; wait kntr;tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY04A'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY04B'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY04C'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY04D'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY04W'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY08A'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY08B'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY08C'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY08W'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY16A'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY16B'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY16W'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY32A'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY32W '; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY64W'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY128W'; dotv-1;go; wait kntr;tget lwpla; go; wait lwpla\n")
    writethat.write("tget kntr;ofmfile 'GREY256'; dotv-1;go;wait kntr; tget lwpla; go; wait lwpla\n")


writethat.close()
writethat = open(home+'/.aips/RUN/LOGS.'+userid,"w")
writethat.write('$ \n')
writethat.write("getn 1 \n")
writethat.write("for i =1 to 200; inext 'pl';inver 0; extd; end\n")
writethat.write("getn 2 \n")
writethat.write("for i =1 to 200; inext 'pl';inver 0; extd; end\n")

for i in range(1,noflux+1):
    writethat.write("task 'uvplt' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write('docal 1 \n')
    writethat.write('doband 3 \n')
    writethat.write('bpver 1 \n')
    writethat.write('bchan '+str(chav1[0]/2)+' \n')
    writethat.write('echan '+str(chav1[0]/2)+' \n')    
    writethat.write("source ")

    x=(flux_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go uvplt; wait uvplt; end \n\n')
    writethat.write("task 'lwpla' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write("")
    writethat.write("outfile 'OUT:"+field_names[y]+"_"+name[-10:]+"_midchan.ps\n")
    writethat.write('dowait true \n')
    writethat.write('go lwpla; wait lwpla; end \n\n')    
    writethat.write("inext 'pl'; extd;\n")    
for i in range(1,nophase+1):
    writethat.write("task 'uvplt' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write('docal 1 \n')
    writethat.write('doband 3 \n')
    writethat.write('bpver 1 \n')
    writethat.write('bchan '+str(chav1[0]/2)+' \n')
    writethat.write('echan '+str(chav1[0]/2)+' \n')    
    writethat.write("source ")

    x=(phase_fiel[i-1])
    y=int(x)
    
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write('dowait true \n')
    writethat.write('go uvplt; wait uvplt; end \n\n')
    writethat.write("task 'lwpla' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write("")
    writethat.write("outfile 'OUT:"+field_names[y]+"_"+name[-10:]+"_midchan.ps\n")
    writethat.write('dowait true \n')
    writethat.write('go lwpla; wait lwpla; end \n\n')    
    writethat.write("inext 'pl'; extd;\n")    


for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)

    writethat.write("task 'snplt'\n")
    writethat.write('default \n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write("nplots 6  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    writethat.write("inext 'sn'\n")
    writethat.write('go snplt \n')
    writethat.write('dowait true \n')
    writethat.write('wait snplt \n\n')

    writethat.write("task 'lwpla' \n")
    writethat.write('default \n')
    writethat.write("plver 1  \n")
    writethat.write("inver 100  \n")      
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    writethat.write("")
    writethat.write("outfile 'OUT:"+field_names[y]+"_"+name[-10:]+"_snplt.ps\n")
    writethat.write('dowait true \n')
    writethat.write('go lwpla; wait lwpla; end \n\n')    
    writethat.write("for i =1 to 20; inext 'pl';inver 0; extd; end\n")    

    writethat.write("task 'uvplt' \n")
    writethat.write('default \n')
    #writethat.write("outfgver 5 \n")
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    
    writethat.write("source ")
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    #writethat.write('docal 1 \n')
    #writethat.write('doband 3 \n')
    writethat.write('bpver 0 \n')
    #writethat.write('imsize 800 \n')  
    writethat.write('dowait true \n')
    writethat.write('go uvplt; wait uvplt; end \n \n')

    writethat.write("task 'lwpla' \n")
    writethat.write('default \n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")

    writethat.write("")
    writethat.write("outfile 'OUT:"+field_names[y]+"_"+name[-10:]+"_final.ps\n")
    writethat.write('dowait true \n')
    writethat.write('go lwpla; wait lwpla; end \n\n')    
    writethat.write("inext 'pl'; extd;\n")    
writethat.write("task 'possm' \n")
writethat.write('default \n')
writethat.write("getn 1  \n")
writethat.write("source '' \n")
writethat.write('bpver 0 \n')
writethat.write('aparm 0 \n')
writethat.write('aparm(8) 2\n')
writethat.write('nplot 6 \n')
writethat.write('solint 0 \n')
writethat.write('dowait true \n')
writethat.write('go possm; wait possm; end \n \n')

writethat.write("task 'lwpla' \n")
writethat.write('default \n')
writethat.write("getn 1 \n")
writethat.write("plver 1  \n")
writethat.write("inver 100  \n")      

writethat.write("")
writethat.write("outfile 'OUT:"+name[-10:]+"_bpassoriginal.ps\n")
writethat.write('dowait true \n')
writethat.write('go lwpla; wait lwpla; end \n\n')    
writethat.write("for i =1 to 20; inext 'pl';inver 0; extd; end\n")

writethat.write("task 'possm' \n")
writethat.write('default \n')
writethat.write("getn 2  \n")
writethat.write("source '' \n")
writethat.write('bpver 0 \n')
writethat.write('aparm 0 \n')
writethat.write('aparm(8) 2\n')
writethat.write('nplot 6 \n')
writethat.write('solint 0 \n')
writethat.write('dowait true \n')
writethat.write('go possm; wait possm; end \n \n')

writethat.write("task 'lwpla' \n")
writethat.write('default \n')
writethat.write("getn 2 \n")
writethat.write("plver 1  \n")
writethat.write("inver 100  \n")      

writethat.write("")
writethat.write("outfile 'OUT:"+name[-10:]+"_bpassaveraged.ps\n")
writethat.write('dowait true \n')
writethat.write('go lwpla; wait lwpla; end \n\n')    
writethat.write("for i =1 to 20; inext 'pl';inver 0; extd; end\n")

writethat.close()

writethat = open(home+'/.aips/RUN/FLAG.'+userid,"w")

for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)
    writethat.write('$ \n')
    
    writethat.write("task 'tvflg' \n")
    writethat.write('default  \n')
    writethat.write('docat -1 \n')
    #writethat.write('docal 1 \n')
    writethat.write("getn 2\n")
    writethat.write("dparm(6) "+str(median_integration_time)+" \n")
    writethat.write("source ")
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    writethat.write("dparm(3) 1 \n")
    writethat.write('dowait true \n')
    writethat.write('go tvflg; wait tvflg; end \n \n')

    writethat.write("task 'tacop' \n")
    writethat.write('default \n')
    writethat.write('getn 2 \n')
    writethat.write("outclass 'SPLIT'  \n")
    writethat.write('outname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("OUTSEQ         2 \n")

    
    writethat.write("inext 'fg' \n")
    writethat.write('dowait true \n')
    writethat.write('go tacop; wait tacop ; end\n \n')
    writethat.write("task 'edita'\n")
    writethat.write('default \n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    writethat.write("inext 'sn'\n")
    writethat.write('go edita \n')
    writethat.write('dowait true \n')
    writethat.write('wait edita \n\n')

    writethat.write("task 'wiper' \n")
    writethat.write('default \n')
    #writethat.write("outfgver 5 \n")
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    
    writethat.write("source ")
    writethat.write("'"+field_names[y]+"'")
    writethat.write("'\n")
    #writethat.write('docal 1 \n')
    #writethat.write('doband 3 \n')
    writethat.write('bpver 0 \n')
    writethat.write('imsize 800 \n')  
    writethat.write('dowait true \n')
    writethat.write('go wiper; wait wiper; end \n \n')

for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)

    writethat.write("task 'split' \n")
    writethat.write('default \n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")
    
    #writethat.write('docal 1 \n')
    writethat.write("source ")
    
    writethat.write("'"+field_names[y]+"'")# wrong way to write

    writethat.write("'\n")
    
    writethat.write('dowait true \n')
    writethat.write('go split; wait split; end\n \n')
    writethat.write("tget 'setfc'\n")
    writethat.write('default \n')
    writethat.write('bparm '+str(pb)+' 2 0\n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          2 \n")
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write('go setfc; wait setfc; end\n')
    
    writethat.write("tget calib \n")
    writethat.write('default \n')
    writethat.write("inclass 'SPLIT'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          2 \n")
    
    writethat.write("inext 'sn' \n")
    writethat.write('extd \n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')

    writethat.write("in2class 'ICL001'  \n")
    writethat.write('in2name  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("IN2SEQ         4 \n")
    
    writethat.write('ncomp = -1000000\n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 0.28\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'P' \n")
    #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write("clrmsg \n")
    writethat.write("tget 'setfc'\n")
    writethat.write('default \n')
    writethat.write('bparm '+str(pb)+' 2 0\n')
    writethat.write("inclass 'CALIB'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          4 \n")
    writethat.write("BOXFILE 'BOX:box."+userid+"."+str(lm)+"\n")
    writethat.write('go setfc; wait setfc; end\n')
    writethat.write("task 'imagr'\n")

    writethat.write("inclass 'CALIB'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          4 \n")
    
    writethat.write("in2nam ''\n")
    writethat.write("in2clas ''\n")
    writethat.write("in2s 0 \n")
    writethat.write('channel 0\n')
    writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize
    writethat.write('flux =kk\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    writethat.write('uvrange 0  \n')        
    writethat.write('robust 0       \n')        
    writethat.write('niter 500000\n')                    
    writethat.write("BOXFILE 'BOX:box."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    writethat.write('dotv -1\n')
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    if weighting=='natural': 
        writethat.write('robust 5       \n')  
    writethat.write('dowait true \n')
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrstat \n")
    writethat.write("recat \n")
    writethat.write("clrmsg \n")
    
    writethat.write('dist= nfield-5 \n')
    writethat.write("task 'imean' \n")
    writethat.write('default \n')

    writethat.write("inclass 'ICL002'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    
    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean \n  \n")
    #writethat.write('kk = 7*PIXSTD \n \n')

    writethat.write('kk=0 \n \n')
    writethat.write("keyword 'ACTNOISE' \n \n")
    writethat.write("gethead \n \n")

    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    
    writethat.write("inclass 'ICL003'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    
    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    
    writethat.write("inclass 'ICL004'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    
    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write("inclass 'ICL005'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    
    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write("inclass 'ICL006'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write('dist= dist-nfield/10 \n')
    writethat.write("inclass 'ICL007'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ dist \n")
    

    writethat.write('dowait true \n')
    writethat.write("go imean; wait imean; keyword 'ACTNOISE';gethead\n  \n")
    writethat.write('kk=keyval(1)+kk \n')
    writethat.write(' kk = 2*kk/6 \n\n')


    writethat.write("tget calib \n")
    writethat.write('default \n')
    writethat.write("inclass 'CALIB'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          4 \n")
    writethat.write("in2class 'ICL001'  \n")
    writethat.write('in2name  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("IN2SEQ         6 \n")

    writethat.write('ncomp = -1000000\n')
    writethat.write('aparm(7) '+str(calprm7)+'\n')
    writethat.write('aparm(9) '+str(calprm9)+'\n')
    writethat.write('ICHANSEL 1 '+str(chav1[i-1]-1)+' 1 0\n')#adjust with no of freq
    writethat.write('solint 4\n')
    writethat.write('refant '+refAnt+'\n')
    writethat.write("SOLTYPE     'L1R' \n")
    writethat.write("SOLMODE     'A&P' \n")
    writethat.write("normaliz 1 \n")
    #writethat.write('uvrange '+uvlow+' 0\n')#adjust with freq
    writethat.write('nmaps nfield \n')
    writethat.write('dowait true \n')
    writethat.write('go calib; wait calib; end\n\n')
    writethat.write('x = x-nfield-1 \n')
    
    writethat.write('x = 2*nfield+x+1 \n')
    writethat.write("y = x+nfield+1 \n")

    writethat.write("task 'imagr'\n")
    writethat.write("inclass 'CALIB'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          6 \n")
    
    writethat.write("in2nam ''\n")
    writethat.write("in2clas ''\n")
    writethat.write("in2s 0 \n")
    writethat.write('channel 0\n')
    writethat.write('nchav '+str(chav1[i-1])+'\n')#individualize
    writethat.write('flux =kk\n')# calculate on the basis of noise
    writethat.write('docal -1       \n')    
    writethat.write('do3dima 1      \n')    
    writethat.write('overlap 2      \n')    
    writethat.write('uvrange 0  \n')        
    writethat.write('robust 0       \n')        
    writethat.write('niter 500000\n')                    
    writethat.write("BOXFILE 'BOX:box."+userid+'.'+str(lm)+"\n")
    writethat.write('dotv -1\n')
    writethat.write('dotv -1\n')
    #writethat.write('wgauss 0, 30, 90, 270\n')
    #writethat.write('FGAUS=0, 0.005, 0.025, 0.120\n')
    #writethat.write('IMAGRP(11)~0.52,0,0.1,0.3,0.1,80\n')
    if weighting=='natural': 
        writethat.write('robust 5       \n')  
    writethat.write('dowait true \n')
    writethat.write('go imagr; wait imagr; end\n \n')
    writethat.write("clrstat \n")
    writethat.write("recat \n")
    writethat.write("clrmsg \n")    


    writethat.write("num =imsize(1)*(nfield)**0.5 \n")
    writethat.write("task 'flatn' \n")
    writethat.write("inclass 'ICL001'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          7 \n")

    writethat.write("imsize num\n")
    writethat.write("nmaps 1 \n")
    writethat.write('dowait true \n')
    writethat.write("go flatn; wait flatn; end \n\n")
    writethat.write("y = y-2*nfield-1 \n")
    
    writethat.write("task 'pbcor'\n")
    writethat.write('default \n')
    writethat.write("inclass 'FLATN'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          6 \n")


    writethat.write("PBPARM(1)=0.1\n")
    writethat.write("PBPARM(2)=1\n")
    writethat.write("PBPARM(3)="+str(pba)+"\n")
    writethat.write("PBPARM(4)="+str(pbb)+"\n")
    writethat.write("PBPARM(5)="+str(pbc)+"\n")
    writethat.write("PBPARM(6)="+str(pbd)+"\n")
    writethat.write("PBPARM(7)=0\n")
    writethat.write('dowait true \n')
    writethat.write('go pbcor \n')
    writethat.write('wait pbcor \n\n')
    writethat.write("clrmsg \n")
    writethat.write("inclass 'PBCOR'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")


    writethat.write("task 'fittp'\n")
    writethat.write('default \n')
    writethat.write("inclass 'PBCOR'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          1 \n")

    writethat.write("dataout 'OUT:im/"+field_names[y]+"_"+name[-20:]+".fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fittp \n')
    writethat.write('wait fittp \n\n')
    writethat.write("i = x\n")
    

    writethat.write("task 'fittp'\n")
    writethat.write('default \n')
    writethat.write("inclass 'CALIB'  \n")
    writethat.write('inname  ')
    writethat.write("'"+field_names[y]+"'")
    writethat.write("\n")
    writethat.write("INSEQ          6 \n")
    
    writethat.write("dataout 'OUT:uv/"+field_names[y]+"_"+name[-20:]+".fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fittp \n')
    writethat.write('wait fittp \n\n')
writethat.close()

writethat = open(home+'/.aips/RUN/ZAP.'+userid,"w")
writethat.write('$ \n')

writethat.write('for i= 1 to x-1; getn i;clrstat; zap;end \n') 

for i in range(1,notarg+1):
    lm=i
    x=(target_fiel[i-1])
    y=int(x)
    writethat.write("task 'fitld'\n")
    writethat.write('default \n')

    writethat.write("datain 'OUT:im/"+field_names[y]+"_"+name[-20:]+".fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fitld \n')

    writethat.write('wait fitld \n\n')
    writethat.write("task 'fitld'\n")
    writethat.write('default \n')

    writethat.write("datain 'OUT:uv/"+field_names[y]+"_"+name[-20:]+".fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fitld \n')
    writethat.write('wait fitld \n\n')

    writethat.write("task 'fitld'\n")
    writethat.write('default \n')
    #writethat.write('y =x-2*nfield-6\n')
    writethat.write("datain 'OUT:uv/"+field_names[y]+"_"+name[-14:]+"_split"+".fits\n")
    writethat.write('dowait true \n')
    writethat.write('go fitld \n')
    writethat.write('wait fitld \n\n')


writethat.write('getn x;clrstat;zap \n')
writethat.close()



if fracband<0.12:
    os.system('rm -rf '+home+'/.aips/RUN/SCRPT1.'+userid)
    os.system('rm -rf '+home+'/.aips/RUN/SCRPT2.'+userid)
