import numpy as np
import math

def get_prime_numbers(n):
	output = np.full(n, True)	

	for num in range(1, n + 1):
		for i in range(2, math.trunc(np.sqrt(num)) + 1):
			if num % i == 0:
				output[num - 1] = False 
				break
	
	return output

def create_audio(length_sec = 100, sample_rate = 8000, use_kilohertz = True):
    span = length_sec * sample_rate

    if use_kilohertz:
    	span = span * 1000

    primes = get_prime_numbers(span)
    print(primes)

create_audio(length_sec=1, sample_rate=100, use_kilohertz=False)
