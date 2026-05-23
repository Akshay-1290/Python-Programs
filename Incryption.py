import random
import string
st= string.punctuation + string.ascii_letters +" " + string.digits 
print(st)
st = list(st) 
print(st)
stt = st.copy()
print(stt)
random.shuffle(stt)
print(stt)
