def text(matn):
    character={}
    for var in matn:
        if var in character:
            character[var]=character[var]+1
        else:
            character[var]=1
    res=max(character, key=character.get)
    return res

print(text('Here you can find activities to practise your reading skills. Reading will help you to improve your understanding of the language and build your vocabulary.'))