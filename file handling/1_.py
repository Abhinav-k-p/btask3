# Write a Python program to read an entire text file

file=open('sample.txt','w')
file.write('Beinex is a multinational firm exploring the endless possibilities of data for Cloud, Analytics, Artificial Intelligence, Machine Learning, and Automation \n')
file.write('Beinex Holdings is a group of six companies.\n')
file.close()
file=open('sample.txt','r')
print(file.read())
file.close()