dct = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5',
      'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
      'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14','fifteen': '15',
      'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
      'twenty':'20', 'thirty':'30', 'forty':'40', 'fifty':'50',
      'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90',
      'hundred':'100', 'thousand':'1000'};

sinput = raw_input('Command:')
ssplitter = raw_input('Splitter:')

sfirst, ssecond = sinput.split(' '+ssplitter+' ')

if len(sfirst.split()) == 1:

    print dct[sfirst]

if len(sfirst.split()) == 2:
    first,second = sfirst.split()
    print (int(dct[first])+int(dct[second]))

if len(ssecond.split()) == 1:

    print dct[ssecond]

if len(ssecond.split()) == 2:
    first,second = ssecond.split()
    print (int(dct[first])+int(dct[second]))




#print 'First:',sfirst,'Second:',ssecond

#print dct[sfirst]
#lol
