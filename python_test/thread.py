import thread
import subprocess

nfs_path = "nfs_path_location"
cmd = 'find {} -mindepth 2 -maxdepth 2 -type d -mtime +180'.format(nfs_path)
cmd1 = 'find {} -mindepth 2 -maxdepth 2 -type d -mtime +180'.format(nfs_path)
log_details = subprocess.check_output(cmd,shell=True)
log_details1 = subprocess.check_output(cmd,shell=True)
def older():
    for vals in log_details.split('\n'):
        return vals

def younger():
    for vals in log_details1.split('\n'):
        return vals
    
t1=threading.Thread(target=older)
t2=threading.Thread(target=younger)

t1.start()
t2.start()

t1.join()
t2.join()
