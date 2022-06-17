import faulthandler as fh

f = open("Error_auto.log", "a+")
fh.enable(file=f, all_threads=True)

exec(type((lambda:0).__code__)(0,1,0,0,0,b'',(),(),(),'','',1,b''))
