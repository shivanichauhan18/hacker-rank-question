def alternatingCharacters(s):
    S=list(s)
    count=0
    for i in range(0,len(S)):
        j=0
        t=0
        while j<len(S)-1:
            if S[j]==S[j+1]:
                t=1
                S.remove(S[j])
                print S
                count=count+1
            j=j+1
        if t==0:
            break
    p="".join(S)
    print p
    return count
print alternatingCharacters("AAABBB")