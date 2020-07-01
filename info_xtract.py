phase_fiel=[]
flux_fiel=[]
target_fiel=[]

listname=outputfolder+"/"+name+'.listobs'
syscommand='rm -rf '+listname
os.system(syscommand)

default('listobs')
vis=ms_active
selectdata=False
verbose=True
listfile=listname
listobs()
syscommand='gedit '+listname
refants=['15','9','5']
refANts=['E02', 'C09', 'C04']
j=0
antenna=['E02:15', 'C09:09', 'C04:05']
for ant in antenna:
         if ant in open(listname).read():
            refANt=refANts[j]
            refAnt=refants[j]
	    break
	 j=j+1




tb.open(ms_active+'/SPECTRAL_WINDOW')
channels = tb.getcol('NUM_CHAN')

spw_bandwidths=tb.getcol('TOTAL_BANDWIDTH')
reference_frequencies = tb.getcol('REF_FREQUENCY')
center_frequencies = []

for ii in range(len(reference_frequencies)):
    center_frequencies.append(reference_frequencies[ii]+spw_bandwidths[ii]/2)
tb.close()
if (channels[0]>300):
	center_frequencies = []
	for ii in range(len(reference_frequencies)):
    		center_frequencies.append(reference_frequencies[ii]-spw_bandwidths[ii]/2)
	tb.close()

bands = []



tb.open(ms_active+'/FIELD')
numFields = tb.nrows()
field_positions = tb.getcol('PHASE_DIR')
field_ids=range(numFields)
field_names=tb.getcol('NAME')
tb.close()

tb.open(ms_active+'/FEED')
Ants = tb.getcol('ANTENNA_ID')
numAnts=len(Ants)
##print numAnts
tb.close()


field_spws = []


tb.open(ms_active)
scanNums = sorted(np.unique(tb.getcol('SCAN_NUMBER')))
field_scans = []
for ii in range(0,numFields):
    subtable = tb.query('FIELD_ID==%s'%ii)
    field_scans.append(list(np.unique(subtable.getcol('SCAN_NUMBER'))))
    subtable.close()
tb.close()
##print field_scans


tb.open(ms_active+'/STATE')
intents=tb.getcol('OBS_MODE')
tb.close()
##print intents

ms.open(ms_active)
scan_summary = ms.getscansummary()
ms_summary = ms.summary()
ms.close()
startdate=float(ms_summary['BeginTime'])
integ_scan_list = []
for scan in scan_summary:
    integ_scan_list.append(int(scan))
sorted_scan_list = sorted(integ_scan_list)
standard_source_names = [ '3C48', '3C147', '3C286']
dcal_sources=['J0319+4130','B0316+413','3C84','J0542+4951','B0538+498','3C147','J0713+4349','B0710+439','J1407+2827','B1404+286','OQ208','J2355+4950','B2352+495']
pacal_sources=['J0521+1638','B0518+165','3C138','J1331+3030','B1328+307','3C286']

cali_int=[]
flux_field=''
for k in standard_source_names:
      j=0
      for l in field_names:
         if (l.find(k)>-1):
            flux_field=flux_field+str(j)+','
            flux_fiel.append(j)
	    cali_int.append(j)
         j=j+1

j=0   
flagg=1

for l in field_names:
	if (l.find('_')==-1):
		flagg=flagg*0.0  # to make sure 'the underscore is not genuiely in the name'
		
	j=j+1	


j=0     
for l in field_names:
	if (l.find('_')>-1) and flagg==1:
		field_names[j]=field_names[j][:-field_names[j][::-1].find('_')].rstrip('_')
		#field_names[j]=field_names[j].rstrip('_')
	j=j+1	


phase_field=''
j=0

for l in field_names:
         if l in open(pipepath+'example.txt').read():
            phase_field=phase_field+str(j)+','
            phase_fiel.append(j)
            cali_int.append(j)
         j=j+1

dcal_field=''
dcal_fiel=[]
j=0

for l in field_names:
         if l in dcal_sources:
            dcal_field=dcal_field+str(j)+','
            dcal_fiel.append(j)
	    #cali_int.append(j)
         j=j+1


pacal_field=''
pacal_fiel=[]
j=0

for l in field_names:
         if l in pacal_sources:
            pacal_field=pacal_field+str(j)+','
            pacal_fiel.append(j)

	    #cali_int.append(j)
         j=j+1



target_field=''
j=0

for l in field_names:
         if j not in cali_int:
            target_field=target_field+str(j)+','	   
            target_fiel.append(j)
         j=j+1


target_field=target_field.rstrip(',')
flux_field=flux_field.rstrip(',')
phase_field=phase_field.rstrip(',')

##print flux_field
##print phase_field
nophase=(len(phase_fiel))
noflux=(len(flux_fiel))
notarg=(len(target_fiel))
nodcal=(len(dcal_fiel))
nopacal=(len(pacal_fiel))
	    

	    
if (nophase<1):
	phase_fiel=flux_fiel
	phase_field=flux_field

nophase=(len(phase_fiel))

tb.open(ms_active+'/FIELD',nomodify=False)
tb.putcol('NAME',field_names)
tb.close()

##print noflux

integration_times = []
for ii in sorted_scan_list:
    integration_times.append(scan_summary[str(ii)]['0']['IntegrationTime'])

maximum_integration_time = max(integration_times)
median_integration_time = np.median(integration_times)


firstchan=int(channels[0]/2-25) 
lastchan=int(channels[0]/2+25)
center_frequencies=[]
synth_beam=[]
maj_beam=[]
rms_tot=[]
for i in range(1,notarg+1):
	x=str(target_fiel[i-1])
	os.system('rm -rf trial.im*')
	default('clean')
	vis=ms_active
	spw='0:'+str(firstchan)+'~'+str(lastchan)
	imagename='trial.im'
	weighting= 'briggs'
	field=x
	niter=0
	clean()

	default('imhead')
	imagename='trial.im.image'
	mode='get'
	hdkey= 'beamminor'
	bmin=imhead()

	default('imhead')
	imagename='trial.im.image'
	mode='get'
	hdkey= 'beammajor'
	bmaj=imhead()
	default('imhead')
	imagename='trial.im.image'
	mode='get'
	hdkey= 'crval4'
	cent_freq=imhead()
	center_frequencies.append(cent_freq['value'])
	maj_beam.append(bmaj['value'])
	synth_beam.append(bmin['value'])
	##print synth_beam

	default('imstat')
	imagename='trial.im.image'
	s=imstat()
	rms=s['rms'][0] 
	rms_tot.append(rms/((channels[0])**0.5)*50**0.5)
	os.system('rm -rf trial.im*')

freq = center_frequencies[0]/1e08
fracband=spw_bandwidths[0]/center_frequencies[0]

if (freq<1.9):
    freq_cl=11
elif (2.5<freq<5):
    freq_cl=6
elif (5<freq<9.5):
    if spw_bandwidths[0]>2.50e8:
       freq_cl=5
    else:
	freq_cl=3
elif (9.5<freq<15):
    freq_cl=4








fin=open(listname)

flag=0
for j in fin:
    if len(pacal_fiel)>0:
       if field_names[pacal_fiel[0]] in j:
          timerpacal='0 '+j[14:16]+' '+j[17:19]+' '+j[20:24]+', 0'+' '+j[27:29]+' '+j[30:32]+' '+j[33:37]
          ##print j[14:38]
          break

fin.close()
