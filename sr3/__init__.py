#-*- coding: utf-8 -*-

import numpy

#############################################
def binomial(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) / i
    return result
#############################################

def p(diff):
    prob = 1.0 / pow(6, int(diff/6) )
    if diff % 6 > 0:
        prob = prob * float (7 - diff%6)/6
    return prob

def sumP(dice,success,diff):
    prob = p(diff)
    return numpy.sum( [ binomial(dice,i)*pow(prob,i)*pow(1-prob,dice-i) for i in range(success,dice+1) ] )
    
def sr3(dices,success,difficulty):
    """
    Computes the change to pass a Shadowrun 3 (P&P-RPG) test

    sr3(dices, success, difficulty)

    dices: number of dices for a test
    success: number of min. successes
    difficulty: difficulty of a test
    
    returns the change to pass a certain test
    """
    return sumP(dices,success,difficulty)
