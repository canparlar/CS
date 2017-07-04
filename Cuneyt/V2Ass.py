#This Program Gets a command consists of two numbers and a splitting word between them.
#It splits the numbers and prints both of them in their number form.

dct = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5',
      'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
      'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14','fifteen': '15',
      'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
      'twenty':'20', 'thirty':'30', 'forty':'40', 'fifty':'50',
      'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90',
      'hundred':'100', 'thousand':'1000'} #Dict for numbers

def printing (word):

    if len(word.split()) == 1:
        return dct[word]

    if len(word.split()) == 2:
        if word.split()[1] == 'hundred' or word.split()[1] == 'thousand':
            first, second = word.split()
            return (int(dct[first])*int(dct[second]))
        else:
            first,second = word.split()
            return (int(dct[first])+int(dct[second]))

    if len(word.split()) == 3:
        first, second, third = word.split()
        return (int(dct[first])*int(dct[second])+int(dct[third]))

    if len(word.split()) == 4:
        if word.split()[3] == 'hundred' or word.split()[3] == 'thousand':
            first,second,third,fourth = word.split()
            return ((int(dct[first])*int(dct[second]))+(int(dct[third])*int(dct[fourth])))
        else:
            first,second,third,fourth = word.split()
            return (int(dct[first])*int(dct[second])+int(dct[third])+int(dct[fourth]))

    if len(word.split()) == 5:
        first, second, third,fourth, fifth = word.split()
        return (int(dct[first])*int(dct[second])+int(dct[third])*int(dct[fourth])+int(dct[fifth]))

    if len(word.split()) == 6:
        first, second, third,fourth,fifth,sixth = word.split()
        return (int(dct[first])*int(dct[second])+int(dct[third])*int(dct[fourth])+int(dct[fifth])+int(dct[sixth]))

sinput = raw_input('Command:') #asks for the command
ssplitter = raw_input('Splitter:') #asks for the splitter

sfirst, ssecond = sinput.split(' '+ssplitter+' ') #splits the command into two parts

print 'First:' ,printing(sfirst),'\n','Second:' ,printing(ssecond) #TODOnumber ise buna girmemeli
