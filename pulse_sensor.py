import time
from machine import Pin, ADC

# Initialize variables
prev_r_wave_time = 0
heart_rate = 0

# Set up AD8232 sensor
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)

ecg_data = []
r_peaks = []
rr_intervals = []
heart_rate = []
 
THRESHOLD = 2400

def find_r_peaks(ecg_data):
  # Initialize the list of R waves
  r_peaks = []
  
  # Loop through the ECG data and check for local maxima
  for i in range(1, len(ecg_data) - 1):
    if ecg_data[i] > ecg_data[i-1] and ecg_data[i] > ecg_data[i+1] and ecg_data[i] > THRESHOLD:
      r_peaks.append(i)
  return r_peaks


def calculate_heart_rate(num_large_squares):
    if(num_large_squares!=0):
        rate = 300 / num_large_squares
    
    return rate

# Loop indefinitely
def read():
    # Extract the current window of data
    ecg_data = []
    r_peaks=[]
    rr_intervals = []
    heart_rate = []
    #s = time.ticks_ms()
    
    #arbitarily setting window size to 100
    for i in range(50):
        ecg_data.append(adc.read())
        #st = time.ticks_ms()
        time.sleep(0.2)          #to take samples after 0.2 seconds
        #et = time.ticks_ms()
        #diff = (et-st)/1000      # this is just to check the time difference btw 2 values
        #print(diff)
        
    #find the indices where there is r peak and returns a list
    r_peaks = find_r_peaks(ecg_data)
    
    #find the interval btw two consecutive peaks and store it in a list
    for i in range(1, len(r_peaks)):
        rr_intervals.append(r_peaks[i] - r_peaks[i-1])
        
    #calculate average rr_interval in the window
        #if (len(rr_intervals)!=0):
         #   avg_rr_interval = sum(r_intervals)/len(rr_intervals)
            
            
    #calculate heart rate in beats per minute:
    for i in range(1,len(rr_intervals)):
        rate = calculate_heart_rate(rr_intervals[i])
        heart_rate.append(rate)
        
    if(len(heart_rate)!=0):
        avg_rate = sum(heart_rate)/len(heart_rate)
        return(avg_rate)
    
    time.sleep(0.2)
    #e = time.ticks_ms()
    #d = (e-s)/1000
    #print(d)        #this is just to check the overall time takenn by one iteration 



