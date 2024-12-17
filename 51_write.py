
    # using write mode
f=open('new.txt','w')
data=f.write("Writing a new file using write mode.")
data=f.write("\nWriting a new file using write mode.")
data=f.write("\nWriting a new file using write mode.")
f.close()

    # using append mode
f=open('new.txt','a')
data=f.write("\nI am using append mode to add new line at last.")
data=f.write("\nI am using append mode to add new line at last.")
f.close()