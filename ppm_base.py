import os

def installpackage():
	pack = input(":")
	with open('oth/middle/newpack_ppm.txt') as bf:
		line = bf.readline()
		if (line != ""):
			print("PyOSPackageManager, starting...")
			with open('pack/'+line+'ppm_pack.ppm') as bff:
				print("Test")
