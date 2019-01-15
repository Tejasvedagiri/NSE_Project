import argparse

parser = argparse.ArgumentParser(description='Saving Key to ARGS Parser')
parser.add_argument('--key', dest='key',
                    help='Enter you key here')

args = parser.parse_args()


import quandl
import os
home_path = os.getcwd()
quandl.save_key(args.key, filename=home_path+"/key/userkey")
print(quandl.ApiConfig.api_key)
