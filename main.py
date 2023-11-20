import os;path="/home"
while True:
 command = input(f"ethernet_man@ubuntu-linux:~{path}$ ")
 if command.startswith("cd "):
  command=command.split(" ",1)[1].split(";",1)[0]
  if command=="..":
   if"/"in path:path=path.rsplit("/",1)[0]
   else:path=""
  elif os.system(f"cd {path}; cd {command}")==0:
   if path=="~"or command.startswith("/"):path=command
   else:path+="/"+command;command=""
 if path.endswith("/"):path=path[0:-1]
 if command!="":os.system(f"cd {path}; {command}")
