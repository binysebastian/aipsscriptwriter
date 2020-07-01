# aipsscriptwriter

To run these scripts both AIPS and CASA (ver>=5.2) are required. 
Runs for Band 3, 4 and 5 uGMRT data.

A sample command to run the scripts is given below

nohup ~/casa-release-5.5.0-149.el7/bin/casa -c ~/aipsscrptwriter_pol_trial_ver/runme.py foldername 935 > folder.out &


runme.py ---> is the code to be run from the list of scripts

foldername---> folder containing the fits or lta files, make sure there are no files other than the input fits files or flag files (from GMRT) in the folder. Also make sure that this folder is not the current working directory while running the pipeline.

935----> AIPS userid

folder.out ---> output file

For more options see and edit inputs.py.
For even more flexibility edit aips_script_write.py

