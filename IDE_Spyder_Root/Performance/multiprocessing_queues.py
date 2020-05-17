#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:44:02 2020

@author: anish
"""


#!/usr/bin/env python      
                
import os              
import subprocess                               
import sys                                        
                                                
from multiprocessing import Process, Queue      
from multiprocessing.queues import _sentinel                
                                                            
                                                            
def run_external_application(application_name, queue):      
    """Runs an Oxygen application"""                                     
    exit_status = 10            
    queue.put(exit_status)                         
    # none of the following help as far as making the pipe go away       
    queue.put(_sentinel)                                 
    queue.close()                                             
                                                              
                                                            
def run(application_name="external_application"):                                                       
    print("Starting '%s'" % application_name)                                                            
                                                                                                              
    queue = Queue()                                                                                   
    application_process = Process(target=run_external_application, args=(application_name, queue))      
                                                                                                      
    application_process.start()         
                                             
    try:                                     
        application_process.join()         
    except KeyboardInterrupt:              
        application_process.terminate()      
                                           
    exit_status = queue.get()                                                                                    
    print("exit status", exit_status)
                                                                                                               
    queue.close()                                                                                         
    # the deletion below has no effect                                                                      
    del queue                                                                                               
    # the only thing that will make the pipe go away is to uncomment the below statement                      
    # queue._writer.close()                                                                                 
                                                                                                            
    print("\nthe '%s' application finished with exit status '%s'...\n" % (application_name, exit_status))
     
    print("Note the file descriptor #4 below")     
    subprocess.call(["ls", "-la", "/proc/%d/fd" % os.getpid()])      
                                        
    return exit_status                  
                                                                                                                       
                                                                                                                       
if __name__ == "__main__":                                                                                             
    print("starting ", os.getpid())                                                                                     
    exit_status = run()                                                                                                
    sys.exit(exit_status)