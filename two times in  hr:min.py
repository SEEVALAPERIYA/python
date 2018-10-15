def write_time():  
  NUMBER_OF_MIN=40 #my offset
  obj=time.gmtime()
  print  " D", obj.tm_mday, " M",obj.tm_mon,  "Y",obj.tm_year, 
  " time", obj.tm_hour+TIME_OFFSET,":",   obj.tm_min-NUMBER_OF_MIN, ":",obj.tm_sec
