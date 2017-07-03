#This Program Gets a command consists of two numbers and a splitting word between them.
#It splits the numbers and prints both of them in their number form.

dct = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5',
      'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
      'ten':'10', 'eleven':'11', 'twelve':'12', 'thirteen':'13', 'fourteen':'14','fifteen': '15',
      'sixteen':'16', 'seventeen':'17', 'eighteen':'18', 'nineteen':'19',
      'twenty':'20', 'thirty':'30', 'forty':'40', 'fifty':'50',
      'sixty':'60', 'seventy':'70', 'eighty':'80', 'ninety':'90',
      'hundred':'100', 'thousand':'1000'} #Dict for numbers

def calc (word): #calculates the number by the lists given

    if len(word) == 1: #if there is only two words/numbers
        return word[0] #returns the number

    if len(word) == 2: #if there is only three words/numbers
        if word[1] == 100 or word[1] == 1000: #if there is 100 or 1000 multiples
            return (word[0]*word[1])
        else: #else it adds
            return (word[0]+word[1])

    if len(word) == 3: #if there is only three words/numbers
        return (word[0]*word[1]+word[2])

    if len(word) == 4: #if there is only four words/numbers
        if word[3] == 100 or word[3] == 1000: #if there is 100 or 1000 multiples
            return (word[0]*word[1]+word[2]*word[3])
        else: #else it adds
            return (word[0]*word[1]+word[2]+word[3])

    if len(word) == 5: #if there is only five words/numbers
        return (word[0]*word[1]+word[2]*word[3]+word[4])

    if len(word) == 6: #if there is only six words/numbers
        return (word[0]*word[1]+word[2]*word[3]+word[4]+word[5])

def numberize (word): #this creates a list with all numberized numbers in input
    nums = [] #creates a list
    for i in range (0,len(word)): #translates all the numbers
        try: #trys to make it an int
            val = int(word[i])
        except ValueError: #if its not a number
            nums.append(int(dct[word[i]])) #translates it by dict
        else: #if it is a number
            nums.append(int(word[i])) #makes it int
    return calc(nums) #sends it to be calculated when done sends it to be printed

sinput = raw_input('Command:') #asks for the command
ssplitter = raw_input('Splitter:') #asks for the splitter

sfirst, ssecond = sinput.split(' '+ssplitter+' ') #splits the command into two part
print 'First:' ,numberize(sfirst.split()),'\n','Second:' ,numberize(ssecond.split()) #prints results
