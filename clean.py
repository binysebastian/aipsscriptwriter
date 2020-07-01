# Estimating the beam and rms
for i in range(1,notarg+1):
	x=(target_fiel[i-1])
	y=int(x)
        os.system('rm -rf '+home+'/.boxfiles/clean0_'+str(num4)+'_'+str(i)+'.py')
        os.system('rm -rf '+home+'/.boxfiles/clean1_'+str(num4)+'_'+str(i)+'.py')
        os.system('rm -rf '+home+'/.boxfiles/clean2_'+str(num4)+'_'+str(i)+'.py')
        os.system('rm -rf '+home+'/.boxfiles/clean3_'+str(num4)+'_'+str(i)+'.py')
	writethat = open(home+'/.boxfiles/clean0_'+str(num4)+'_'+str(i)+'.py',"a")
	writethat.write('\n')
	writethat.write(r"vp.setpbpoly(telescope ='GMRT',  usesymmetricbeam=True, coeff="+str(pbcoeff)+")\n")
	writethat.write(r"os.system('rm -rf pbname')"+"\n")
	writethat.write(r"vp.saveastable('pbname')"+"\n")
	writethat.write(r"default('imhead') "+"\n")
	writethat.write(r"imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+".fits'"+"\n")
	writethat.write(r"mode='summary' "+"\n")
	
	writethat.write(r"cell_s=imhead() "+"\n")
	writethat.write('\n')
	writethat.write(r"cell_si=abs(cell_s['restoringbeam']['minor']['value']/4.5*3600) "+"\n")

	writethat.write("imsi=4.4/round(cell_s['refval'][2]/1e8,2)*3600*2/cell_si"+'\n')
	writethat.write(r"default('imstat') "+"\n")
	writethat.write(r"imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+".fits' "+"\n")
	writethat.write(r"s=imstat() "+"\n")
	writethat.write('\n')
	writethat.write(r"rms=s['medabsdevmed'][0] "+"\n")
	writethat.write(r"default(importuvfits) "+"\n")
	writethat.write(r"fitsfile='"+outputfolder+"/uv/"+field_names[y]+"_"+name[-20:]+".fits'"+"\n")
	writethat.write(r"vis='"+outputfolder+"/uv/"+field_names[y]+"_"+name[-20:]+".ms'"+"\n")
	writethat.write(r"importuvfits() "+"\n")
	writethat.write('\n')
	writethat.write(r" "+"\n")

	writethat.write(r"ideal=3"+"\n")

	# Loop for cleaning + phase selfcal
	
	#writethat.write(r"aaa=[2.5,3,2.5] "+"\n")# threshold factor for clean
	#writethat.write(r"solintt=['1200s','180s','60s']"+"\n")
	writethat.write(r"aaa=[2.5] "+"\n")# threshold factor for clean
	writethat.write(r"solintt=['1200s']"+"\n")
	writethat.write(r"for ii in range(1):"+"\n")
	writethat.write(r"	default(tclean) "+"\n")
	writethat.write(r"	specmode               =  'mfs' "+"\n")
	writethat.write(r"	gridder           =  'wproject' "+"\n")
	writethat.write(r"	wprojplanes        =  -1 "+"\n")
	writethat.write(r"	niter		  	   =   20000*2**ii"+ "\n")
	writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
	writethat.write(r"	scales="+str(scales)+"\n")#change for frequencies
	writethat.write(r"	interactive=False"+"\n")	
	writethat.write(r"	nterms= 2 "+"\n")
	writethat.write(r"	cell=[str(round(cell_si,2))+'arcsec'] "+"\n")
	writethat.write(r"	imsize=[] "+"\n")
	writethat.write("	for i in range(6,14):"+"\n")
	writethat.write("		imsiz=2**i"+"\n")
	writethat.write("		if imsi < imsiz:"+"\n")
	writethat.write("			imsize=[imsiz]"+"\n")
	writethat.write("			break"+"\n")
	writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
	writethat.write(r"	threshold =str(aaa[ii]*rms)+'Jy' "+"\n")
	writethat.write(r"	vis='"+outputfolder+"/uv/"+field_names[y]+"_"+name[-20:]+".ms'"+"\n")
	writethat.write(r"	imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_p'+str(ii)"+"\n")
	writethat.write(r"	stokes='I' "+"\n")
	writethat.write(r"	deconvolver='mtmfs' "+"\n")
	writethat.write(r"	usemask='auto-multithresh' "+"\n")
	writethat.write(r"	sidelobethreshold=1.5"+"\n")
	writethat.write(r"	pblimit=-1.0"+"\n")
	writethat.write(r"	savemodel='modelcolumn'"+"\n")
	writethat.write(r"	tclean() "+"\n")
	writethat.write('\n')

	if npols==4:
		writethat.write(r"	default(tclean) "+"\n")
		writethat.write(r"	specmode               =  'mfs' "+"\n")
		writethat.write(r"	gridder           =  'wproject' "+"\n")
		writethat.write(r"	wprojplanes        =  -1 "+"\n")
		writethat.write(r"	niter		  	   =   5000*2**ii"+ "\n")
		writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
		writethat.write(r"	scales="+str(scales)+"\n")#change for frequencies
		writethat.write(r"	interactive=False"+"\n")	
		writethat.write(r"	nterms= 2 "+"\n")
		writethat.write(r"	cell=[str(round(cell_si,2))+'arcsec'] "+"\n")
		writethat.write(r"	imsize=[] "+"\n")
		writethat.write("	for i in range(6,14):"+"\n")
		writethat.write("		imsiz=2**i"+"\n")
		writethat.write("		if imsi < imsiz:"+"\n")
		writethat.write("			imsize=[imsiz]"+"\n")
		writethat.write("			break"+"\n")
		writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
		writethat.write(r"	threshold =str(aaa[ii]*rms)+'Jy' "+"\n")
		writethat.write(r"	vis='"+outputfolder+"/uv/"+field_names[y]+"_"+name[-20:]+".ms'"+"\n")
		writethat.write(r"	imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_Q_p'+str(ii)"+"\n")
		writethat.write(r"	stokes='Q' "+"\n")
		writethat.write(r"	deconvolver='mtmfs' "+"\n")
		writethat.write(r"	usemask='auto-multithresh' "+"\n")
		writethat.write(r"	sidelobethreshold=1.5"+"\n")
		writethat.write(r"	pblimit=-1.0"+"\n")
		writethat.write(r"	savemodel='modelcolumn'"+"\n")
		writethat.write(r"	tclean() "+"\n")
		writethat.write('\n')

		writethat.write(r"	default(tclean) "+"\n")
		writethat.write(r"	specmode               =  'mfs' "+"\n")
		writethat.write(r"	gridder           =  'wproject' "+"\n")
		writethat.write(r"	wprojplanes        =  -1 "+"\n")
		writethat.write(r"	niter		  	   =   5000*2**ii"+ "\n")
		writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
		writethat.write(r"	scales="+str(scales)+"\n")#change for frequencies
		writethat.write(r"	interactive=False"+"\n")	
		writethat.write(r"	nterms= 2 "+"\n")
		writethat.write(r"	cell=[str(round(cell_si,2))+'arcsec'] "+"\n")
		writethat.write(r"	imsize=[] "+"\n")
		writethat.write("	for i in range(6,14):"+"\n")
		writethat.write("		imsiz=2**i"+"\n")
		writethat.write("		if imsi < imsiz:"+"\n")
		writethat.write("			imsize=[imsiz]"+"\n")
		writethat.write("			break"+"\n")
		writethat.write(r"	weighting         =  '"+weighting+"' "+"\n")
		writethat.write(r"	threshold =str(aaa[ii]*rms)+'Jy' "+"\n")
		writethat.write(r"	vis='"+outputfolder+"/uv/"+field_names[y]+"_"+name[-20:]+".ms'"+"\n")
		writethat.write(r"	imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_U_p'+str(ii)"+"\n")
		writethat.write(r"	stokes='U' "+"\n")
		writethat.write(r"	deconvolver='mtmfs' "+"\n")
		writethat.write(r"	usemask='auto-multithresh' "+"\n")
		writethat.write(r"	sidelobethreshold=1.5"+"\n")
		writethat.write(r"	pblimit=-1.0"+"\n")
		writethat.write(r"	savemodel='modelcolumn'"+"\n")
		writethat.write(r"	tclean() "+"\n")
		writethat.write('\n')

	writethat.write(r"default(exportfits) "+'\n')
	writethat.write(r"imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_p0.image.tt0' "+'\n')
	writethat.write(r"fitsimage='"+outputfolder+"/im/"+field_names[y]+"_"+name[-6:]+"casa0_p0.fits' "+'\n')
	writethat.write(r"exportfits() "+'\n')
	writethat.write('\n')
	if npols==4:
		writethat.write(r"default(exportfits) "+'\n')
		writethat.write(r"imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_Q_p0.image.tt0' "+'\n')
		writethat.write(r"fitsimage='"+outputfolder+"/im/"+field_names[y]+"_"+name[-6:]+"casa0_Q_p0.fits' "+'\n')
		writethat.write(r"exportfits() "+'\n')
		writethat.write('\n')
	
		writethat.write(r"default(exportfits) "+'\n')
		writethat.write(r"imagename='"+outputfolder+"/im/"+field_names[y]+"_"+name[-20:]+"casa0_U_p0.image.tt0' "+'\n')
		writethat.write(r"fitsimage='"+outputfolder+"/im/"+field_names[y]+"_"+name[-6:]+"casa0_U_p0.fits' "+'\n')
		writethat.write(r"exportfits() "+'\n')
		writethat.write('\n')
		writethat.close()

	else:
		writethat.close()
			
