import os
import sys
import platform
import socket

#lab 9 : Question 3a.a, 3a.b
print(platform.machine())
print(platform.architecture())

#lab 9 : Question 3a.c, 3a.d
#set and get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

#lab 9 : Question 3a.e
#os name
print(os.name)
print(platform.system())


#lab 9 : Question 3a.f
#Process Id
print(os.getpid())

#lab 9 : Question 3b.a
#file descriptors
#Open or create a file names fdpractise.txt
f_name = "fdpractise.txt"
#with open("fdpractise.txt", "a+") as f:
#   print( f.readline())
#   f.write("hello world")
f = os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fstat(f, "a+")
print(f_obj)
f_obj.close()

print()

#lab 9 : Question 3b.e
# forking
print("before fork:", os.getpid())
p = os.fork()
print("after fork:", os.getpid())

if p == 0:
    print("Child Process ")
    print("Parent Process PID:", os.getpid())
else:
    print("Parent Process ")
    os.wait()
    print("Child Process PID: ", p)

print("Last line")

