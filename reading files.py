import numpy as np
import sox
import librosa
import os
import os.path
import glob
import csv
from scipy.io import wavfile
import librosa

def conversion(path):


    z=glob.glob(path)
    print(z)
    tfm = sox.Transformer()
    n=0
    music_pop=[]
    if path=="/home/tatras/Downloads/genres/genres/pop/*.au":
      for i in z:
        music_mp3=[]
        tfm.build(i, 'pop'+str(n)+'.wav')

        music_pop.insert(n,"pop"+str(n)+".wav")
        n=n+1
     # print(music_pop)
        #music_mp3=music_mp3+mp3

      return(music_pop)
        #print(music_mp3)
      #print(music_pop)
    else :
      #path=="/home/tatras/Downloads/genres/genres/classical/*.au":
      music_classical = []
      for i in z:

        tfm.build(i, 'classical'+str(n)+'.wav')

        music_classical.insert(n,"classical"+str(n)+".wav")
        n=n+1
        #print(mp3)
        #music_mp3=music_mp3+mp3

      #print(music_classical)
      return(music_classical)

def features_extraction(pop,classical):
    file = open('data.csv', 'w', newline='')
    with file:
        #a={"mfcc"+str(i) for i in range (20),"satyam"}
        d1={"filename":"satyam"}
        d3 = {}
        for i in range(21):

            d4={"mfcc"+str(i):"satyam"}
            d3.update(d4)
        d1.update(d3)
        d2 = {"genres": "gupta"}
        d1.update(d2)
        sortedDict = dict(sorted(d1.items()))
        writer = csv.DictWriter(file,fieldnames=sortedDict)
        writer.writeheader()
    genres=["pop","classical"]
    for g in genres:
        for filename in os.listdir('/home/tatras/PycharmProjects/'+g):
             y,sr=librosa.load('/home/tatras/PycharmProjects/'+g+"/"+filename)
             mfcc=librosa.feature.mfcc(y,sr)
             z=np.mean(mfcc,axis=1)
             a={'filename':filename}
             b={'genres':g}
             mfcc_dict={}
             i=1
             for e in z:
                 c={"mfcc"+str(i):e}
                 mfcc_dict.update(c)
                 i=i+1
             mfcc_dict.update(a)
             mfcc_dict.update(b)
             file=open('data.csv','a',newline='')

             with file :
                writer=csv.DictWriter(file,fieldnames=d1 )

                writer.writerow(mfcc_dict)


if __name__=="__main__":
    path="/home/tatras/Downloads/genres/genres/classical/*.au"
    pop=conversion(path)
    path = "/home/tatras/Downloads/genres/genres/pop/*.au"
    classical=conversion(path)
    features_extraction(pop,classical)
    print(pop)
    print(classical)



