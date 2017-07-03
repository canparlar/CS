#This Program Gets a command consists of two numbers and a splitting word between them.
#It splits the numbers and prints both of them in their number form.

dct = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5',
      'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
      'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14','fifteen': '15',
      'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
      'twenty':'20', 'thirty':'30', 'forty':'40', 'fifty':'50',
      'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90',
      'hundred':'100', 'thousand':'1000'} #Dict for numbers






sinput = raw_input('Command:') #asks for the command
ssplitter = raw_input('Splitter:') #asks for the splitter

sfirst, ssecond = sinput.split(' '+ssplitter+' ') #splits the command into two part
word = sfirst.split()
list (b[len(word)])

for i in range (0,len(word)):
    try:
        a = int(word[i])
    except ValueError: #not a number
        b[i] = int(dct[word[i]])
    else:
        b[i] = word[i]

        print b
