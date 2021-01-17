def matrix_texter(M):
    restrung=''
    for a in str(M):
        if a=='[':
            restrung+='{'
        elif a==' ':
            restrung+=','
        elif a==']':
            restrung+='}'            
        elif a=='\n':
            restrung+=','
        else:
            restrung+=a
    restrung='{'+restrung
    restrung=restrung+'}'
    return restrung                        
