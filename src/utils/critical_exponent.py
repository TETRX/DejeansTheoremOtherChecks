from fractions import Fraction
import math

def critical_exponent(word, max_exp=math.inf): # very naive but might be enough
    exp=1
    for i in range(len(word)):
        for j in range(i+1,len(word)):
            p=word[i:j]
            excess=0
            len_p=len(p)
            for k in range(j,len(word)):
                if word[k]==p[excess%len_p]:
                    excess+=1
                else:
                    break
            exp=max(exp, Fraction(len(p)+excess,len(p)))
            if exp>=max_exp:
                return exp
    return exp