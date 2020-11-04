from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    finaldata = prepare_data(dict(request.POST))
    if finaldata.get('input'):
        res = modify_text(finaldata)
        finaldata['reply'] = res
        return render(request,'index.html',finaldata)
    else:
        return render(request,'index.html')

def prepare_data(rawdata):
    for key,value in rawdata.items():
        rawdata[key] = value[0]
    return rawdata

def modify_text(data):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    res = ""
    string = data.get('input')
    lines = 0
    words = 0
    chars = 0
    if data.get('removeSpace'):
        string = string.strip()
    if data.get('removeTextCheck'):
        string = string.replace(data.get('removeText'),'')

    size = len(string)

    for idx,ch in enumerate(string):

        if (ch == '\r' or ch == '\n') and data.get('removeNewLine'):
            continue
        if idx<size-1 and string[idx] == ' ' and string[idx+1] == ' ' and data.get('removeSpace'):
            continue
        if data.get('removePunc') and ch in punctuations:
            continue
        else:
            if ch.isalpha():
                if data['textcase'] == 'lower' and not ch.islower():
                    res += ch.lower()
                elif data['textcase'] == 'upper' and not ch.isupper():
                    res += ch.upper()
                else:
                    res += ch
            else:
                res += ch
        chars+=1
        if idx>0 and ch == ' ' and string[idx-1] != ' ':
            words+=1
        if ch == '\r':
            words+=1
            lines+=1

    data['charCount'] = chars-lines
    data['wordCount'] = words+1
    data['lineCount'] = lines+1

    return res