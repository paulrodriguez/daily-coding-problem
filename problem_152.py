'''
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.
'''
import random

def generate_probabilities(nums,probs):
    nums2 = [0]*100

    i = 0
    j = 0

    while i < len(nums):
        t = int(round(probs[i]*100))
        k = 0
        while k < t:
            nums2[j] = nums[i]
            j += 1
            k += 1
        i +=1
    
    r = random.randint(0,100)

    return nums2[r]


def generate_probabilities_v2(nums,probs):
    probs_prefix = [0]*len(probs)
    probs_prefix[0] = probs[0]
    for i in range(1,len(probs)):
        probs_prefix[i] = probs_prefix[i-1] + probs[i]

    r = random.random()

    for i in range(len(probs_prefix)):
        if r<=probs_prefix[i]:
            return nums[i]
#print(generate_probabilities([1,2,3,4],[0.1,0.5,0.2,0.2]))
print(generate_probabilities_v2([1,2,3,4],[0.1,0.5,0.2,0.2]))
            



