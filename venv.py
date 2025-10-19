import os
import time
os.system("python3 -m venv venv")
time.sleep(2) # This is to avoid memory issues that can cause temporary bricking of the PC
os.system("source venv/bin/activate")
time.sleep(2) # This is to avoid memory issues that can cause temporary bricking of the PC
os.system("pip install audio2vec")
time.sleep(2) # This is to avoid memory issues that can cause temporary bricking of the PC
os.system("pip install quantumaudio")
time.sleep(2) # This is to avoid memory issues that can cause temporary bricking of the PC
os.system("pip install numpy")
time.sleep(2) # This is to avoid memory issues that can cause temporary bricking of the PC
os.system("pip install anyio")
