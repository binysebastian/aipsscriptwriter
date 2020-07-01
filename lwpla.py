
qalog.write("task 'lwpla'\n")
qalog.write('default \n')
qalog.write('y = x-nfield-1 \n')
qalog.write('getn y \n')

for j in range(nplo):
   i=j+1
   qalog.write('plver '+str(i)+' \n')
   qalog.write("outfile '"+name+"/snplt_pl"+str(plver)+"_"+str(i)+".ps \n")
   qalog.write('go lwpla \n')
   qalog.write('wait lwpla \n\n')
qalog.write("for i =1 to 10; inext 'pl'; inver 0 ;extd; end \n")
qalog.write("task 'lwpla'\n")
qalog.write('default \n')
qalog.write('y = x-nfield-1 \n')
qalog.write('getn y \n')

for j in range(nplo):
   i=j+1
   qalog.write('plver '+str(i)+' \n')
   qalog.write("outfile '"+name+"/snplt_pl"+str(plver)+"_"+str(i)+".ps \n")
   qalog.write('go lwpla \n')
   qalog.write('wait lwpla \n\n')
qalog.write("for i =1 to 10; inext 'pl' ; inver 0;extd; end \n")


qalog.write("task 'lwpla'\n")
qalog.write('default \n')
qalog.write('y = x-nfield-1 \n')
qalog.write('getn y \n')

for j in range(nplo):
   i=j+1
   qalog.write('plver '+str(i)+' \n')
   qalog.write("outfile '"+name+"/snplt_pl"+str(plver)+"_"+str(i)+".ps \n")
   qalog.write('go lwpla \n')
   qalog.write('wait lwpla \n\n')
qalog.write("for i =1 to 10; inext 'pl' ; inver 0;extd; end \n")
qalog.write("task 'lwpla'\n")
qalog.write('default \n')
qalog.write('y = x-nfield-1 \n')
qalog.write('getn y \n')

for j in range(nplo):
   i=j+1
   
   qalog.write('plver '+str(i)+' \n')
   qalog.write("outfile '"+name+"/snplt_pl"+str(plver)+"_"+str(i)+".ps \n")
   qalog.write('go lwpla \n')
   qalog.write('wait lwpla \n\n')
qalog.write("for i =1 to 10; inext 'pl' ; inver 0;extd; end \n")
