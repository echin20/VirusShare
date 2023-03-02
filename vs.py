import argparse
import os
import json

from virusshare import VirusShare

def download(args, v):
    if args.path is None:
        print ("File path not specified. Please specify file path with -p")
    elif os.path.isdir(args.path) is True:
        result = v.download(args.download, args.path)
        if result is None:
            print("success")
    else:
        os.makedirs(args.path)
        result = v.download(args.download, args.path)
        if result is None:
            print("success")

def source(args, v):
    result = v.source(args.source) 

    print(json.dumps(result['data'], indent=4))

def quick(args, v):
    result = v.quick(args.quick)

    print(result['data'])

def info(args, v):
    result = v.info(args.info)

    print(json.dumps(result['data'], indent=4))

def init_parser():
    parser = argparse.ArgumentParser(description="Quries VirusShare database. Api key needs to be saved into a file called \"vsshare.key\". File format {\"api_key\":\"<key>\"}")
    
    parser.add_argument("-i", "--info", help="Information on the sample")
    parser.add_argument("-d", "--download", help="Download sample")
    parser.add_argument("-p", "--path", help="Path to download sample")
    parser.add_argument("-q", "--quick", help="The response  value of 0, 1, or 2 to indicate unknown, malware, and benign")
    parser.add_argument("-s", "--source", help="Source information of the sample. (Requires sha256)")

    return parser

def main():
    parser = init_parser()
    args = parser.parse_args()

    if os.path.exists('vsshare.key'):
        key_file = json.load(open('vsshare.key'))
        key = key_file['api_key']
    else:
        print ("Failed to find vsshare.key file.")

    v = VirusShare(key)

    if args.info:
        info(args, v)
    if args.quick:
        quick(args, v)
    if args.source:
        source(args, v)
    if args.download:
        download(args, v)


if __name__ == "__main__":
    main()
