def shark(pD, sD, yS, sS, d):
    return 'Shark Bait!' if sD/(sS/2 if d else sS)<= pD/yS else 'Alive!'
