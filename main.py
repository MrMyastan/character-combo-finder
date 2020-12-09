import time

bitMask = 0
inputText = input("What would you like to find the combinations of?\n")

for i in range(2 ** len(inputText)):
    inputMasked = ''
    for j in range(len(inputText)):
        if bitMask >> j & 1:
            inputMasked = inputMasked + inputText[j]
    print(inputMasked)
    time.sleep(.5)
    bitMask += 1