# AUTHOR shen shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu
# AUTHOR Ziteng Xu zxu83@bu.edu

# arrays
import numpy as np

def filtmusic(music,frame_rate,lb,hb):
    "return the ploted filted music sample"
    tau=1/frame_rate
    mf=np.fft.fft(music)            #file music in frequency domain
    n=len(mf)
    t=n*tau
    il=int(lb*t)
    ih=int(hb*t)
    hf=np.zeros(n)
    hf[il:ih]=1
    hf[(n-ih):(n-il)]=1
    filt_fd=hf*mf
    filt_td=np.fft.ifft(filt_fd)
    filt_music=filt_td.real
    return filt_music
    
def loudest_band(music,frame_rate,bw):
    "find the low and high bound for the bandwidth input, return filted ploted sample"
    tau=1/frame_rate
    n=len(music)
    t=n*tau             #the i th item in array is feq*t, also f=i/t 
    freq_dom=np.fft.fft(music)      #file music in frequency domain
    fqd_pos=freq_dom[0:len(freq_dom)//2]      #get the positive frequency
    energy=np.abs(fqd_pos)**2
    i_bw=int(bw*t)
    h=np.ones(i_bw)
    con=np.convolve(h,energy)      #use convole to calculate sum energy
    result=con[i_bw-1:len(con)-i_bw+1]
    i_l=result.argmax()
    lb=i_l/t
    hb=lb+bw
    filted_music=filtmusic(music,frame_rate,lb,hb)
    return lb,hb,filted_music
    
    
def main():
        pass
        
if __name__=="__main__":
    main()    
