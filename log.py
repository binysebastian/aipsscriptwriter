qalog = open(outputfolder+"/"+name+"."+str(num),"w")

qalog.write("Refant = "+refAnt+"\n")
qalog.write("User id = "+str(num)+","+userid+"\n")
qalog.write("Flux calibrator ")
for i in range(1,noflux+1):
	x=(flux_fiel[i-1])
	y=int(x)
	qalog.write(field_names[y]+" ")
qalog.write("\n Phase calibrator ")
for i in range(1,nophase+1):
	x=(phase_fiel[i-1])
	y=int(x)
	qalog.write(field_names[y]+" ")
qalog.write("\n Target ")
for i in range(1,notarg+1):
	x=(target_fiel[i-1])
	y=int(x)
	qalog.write(field_names[y]+" \n")
	qalog.write("beam "+str(synth_beam[i-1])+"x"+str(maj_beam[i-1])+" \n")
	qalog.write("Channels averaged "+str(chav[i-1])+" \n")
qalog.write("Single visibilty rms "+str(sens)+"\n")

qalog.write("Median integration time = "+str(median_integration_time)+"\n")








qalog.close()
