# AUTHOR Shen Shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu

# WAV file support
import scipy.io.wavfile as wavfile

# arrays
import numpy as np

def dialer(file_name,frame_rate,phone,tone_time):
    data=np.array([])
    for num in phone:
        data=np.append(data,turn_data(frame_rate,num,tone_time))
    wavfile.write(file_name,frame_rate,data)

def turn_data(sample_rate,number,time):
    pn=sample_rate*time
    t=np.linspace(0,time,pn)
    f1,f2=frequency_find(number)
    data_out=np.cos(2*np.pi*f2*t)+np.cos(2*np.pi*f1*t)
    return data_out
    
def frequency_find(number):
    num=int(number)
    if num==0:
        f1=1336
        f2=941
    elif num in range(1,10):
        a=(num-1)%3
        b=(num-1)//3
        creat_f1={0:1209,1:1336,2:1477}   #dictionary for case
        creat_f2={0:697,1:770,2:852}
        f1=creat_f1[a]
        f2=creat_f2[b]
    return f1,f2
        
def main():
    dialer('myphone',44100,"6178387330",0.5)

if __name__=="__main__":
    main()
