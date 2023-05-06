import pip
pip.main(['install','pipreqs'])
pip.main(['install','=r','requirements.txt'])
# pip.main(['install','subprocess'])
# import subprocess
# import sys



# check module and install
# def checker_installer():
#     subprocess.check_call([sys.executable, "-m", "pip", "install", '-r', 'requirements.txt'])

#     for package in packages:
#         print(package)
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])



