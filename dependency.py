import subprocess
import sys
import json

file=open("dependency.json")
data=json.load(file)
success=[]
failed=[]

for dependency,version in zip(data["Dependencies"].keys(),data["Dependencies"].values()):

    package=dependency+"=="+version
    try:
        chk=subprocess.check_call(["pip","install",package])
    
        if chk==0:
            success.append(package)
        else:
            failed.append(package)
    except:
            failed.append(package)

        

print("\nPackages successfully installed:")
for package in success:
    print(package)

print("\n\nPackages not installed:")
for package in failed:
    print(package)
