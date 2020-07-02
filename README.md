# aipsscriptwriter

This is a set of scripts to carry out the uGMRT continuum data analyis. It runs for Band 3, 4 and 5 uGMRT data.
It uses AIPS to carry out all the calibration and few rounds of imaging and sel-calibration, after which the final imaging is carried out in CASA using MT-MFS algorithm. CASA automatic flagging algorithms, namely 'tfcrop' and 'rflag' are also made use of.

## Requirements

*  AIPS (works in version 12 and 13), other versions have to be tested.
*  CASA (ver>=5.2) are required. 



## Running the scripts
A sample command to run the scripts is given below
```
nohup ~/casa-release-5.5.0-149.el7/bin/casa -c ~/aipsscriptwriter/runme.py foldername 101 > folder.out &
```
### Meaning of the commands

   * nohup ---> is optional, to run the code in the background

   * runme.py ---> is the code to be run from the list of scripts

   * foldername---> folder containing the fits or lta files, make sure there are no files other than the input fits files or flag files (from GMRT) in the folder. Also make sure that this folder is not the current working directory while running the pipeline.

   * 101----> AIPS userid

   * folder.out ---> output file

For more options see and edit inputs.py.
For even more flexibility edit aips_script_write.py

## Outputs

An output folder is created with the name, foldername+'out'. The details about the observation, userid, channels averaged etc can be found here. The final image and uv files can be found in folder named 'im' and 'uv' respectively. 

To access all the files, simply login to aips with the userid you provided in the beginning.



### Possible error

Task 'imagr' may take a long time to stop in which case, edit the bash script 'stop.sh' in the output folder file by putting the corresponding userid and run it.
Currently won't run in parallel.

## Acknowledgements

Parts of the codes are inspired from initial versions of CASA EVLA pipeline. 
The data reduction steps in AIPS are those generally followed by the radio astronomy community at NCRA.
I thank Ishwara Chandra for the many discussions on AIPS data analysis and his help page,
http://www.ncra.tifr.res.in:8081/~ishwar/aips_help.html.
Other documents referred include AIPS.INFO (circulated during radio astronomy schools), http://www.ncra.tifr.res.in/~ruta/gmrt_workshop/aritra_sambit.pdf and http://gmrt.ncra.tifr.res.in/~astrosupp/docs/aips-pol-gmrt-v2.pdf (thanks to Nimisha Kantharia).
Thanks to Preeti Kharb and Silpa Sasikumar for discussions on GMRT polarization.
I also thank Ruchika Seth for her contributions.






