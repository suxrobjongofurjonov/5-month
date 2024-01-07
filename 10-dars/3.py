
def func( haystack, needle):
        res=[0]*len(needle)
        res1=0
        for i in range(1,len(needle)):
            while (res1>0 and needle[i]!=needle[res1]):
                res1=res[res1-1]
            if needle[res1]==needle[i]:
                res1+=1
                res[i]=res1

        n=0
        for var in range(len(haystack)):
            while (n>0 and needle[n]!=haystack[var]):
                n=res[n-1]
            if needle[n]==haystack[var]:
                n+=1
            if n==len(needle):
                return var-n+1
        return -1
    
print(func(haystack='sadbutsad', needle='sad'))