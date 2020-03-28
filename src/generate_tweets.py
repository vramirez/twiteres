import json
import sys

def generate_model(fail):
    with open(fail) as json_file:
        for line in json_file:
            data = json.loads(line)
            if(data.get('retweeted_status')==None):
                lain=data.get('text')
                print(lain.replace('\n', ' ').replace('\r', ' '))
                
                

if __name__ == "__main__":
    filename = sys.argv[1]        
    generate_model(filename)
    