def found(text):
    letter=[c for c in text if c.isalpha()]
    letters=letter[::-1]

    res=''
    f=0

    for var in text:
        if var.isalpha():
            res+=letters[f]
            f+=1
        else:
            res+=var

    return res

matn="He%llo, Wor!ld!"
res1=found(matn)
print(res1)