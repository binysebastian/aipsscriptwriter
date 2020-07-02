# aipsscriptwriter

To run these scripts both AIPS and CASA (ver>=5.2) are required. 
Runs for Band 3, 4 and 5 uGMRT data.

Uses AIPS to carry out all the calibration and few rounds of imaging and sel-calibration, after which the final imaging is carried out in CASA using MT-MFS algorithm. CASA automatic flagging algorithms, namely 'tfcrop' and 'rflag' are also made use of.

## Running the scripts
A sample command to run the scripts is given below

nohup ~/casa-release-5.5.0-149.el7/bin/casa -c ~/aipsscrptwriter_pol_trial_ver/runme.py foldername 935 > folder.out &


runme.py ---> is the code to be run from the list of scripts

foldername---> folder containing the fits or lta files, make sure there are no files other than the input fits files or flag files (from GMRT) in the folder. Also make sure that this folder is not the current working directory while running the pipeline.

935----> AIPS userid

folder.out ---> output file

For more options see and edit inputs.py.
For even more flexibility edit aips_script_write.py

## Outputs

An output folder is created with the name, foldername+'out'. The details about the observation, userid, channels averaged etc can be found here. The final image and uv files can be found in folder named 'im' and 'uv' respectively. 

To access all the files, simply login to aips with the userid you provided in the beginning.



### Possible error

Task 'imagr' may take a long time to stop in which case, edit the stop.sh file by putting the corresponding userid and run it.
Currently won't run parallel.
