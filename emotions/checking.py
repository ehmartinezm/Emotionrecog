
import os
path = '/Users/edwin/emotions/downloads/saddy/'
files = os.listdir(path)


def create_pos_n_neg():
    for file_type in ['/Users/edwin/emotions/negatives/']:
        print(path)

        for img in os.listdir(file_type):
            print(img)

            if file_type == '/Users/edwin/emotions/downloads/saddy/':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
                    print(line)
            elif file_type == '/Users/edwin/emotions/negatives/':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)


create_pos_n_neg()

"""
def create_pos_n_neg():

    for file_type in files :
        print("working")


        for img in os.listdir(file_type):
            print("trying")
            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
                    print(line)
            elif file_type == '/Users/edwin/emotions/downloads/saddy/':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)"""
