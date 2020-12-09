bitMask = 0
inputText = input("What would you like to find the combinations of?\n")

for i in range(2 ** len(inputText)):
    inputMasked = ''
    for j in range(len(inputText)):
        if bitMask >> j & 1:
            inputMasked += inputText[j]
    print(inputMasked)
    bitMask += 1

""" 
cProfile output with input as "with thunderous applause"
         33554438 function calls in 2556.078 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1  144.157  144.157 2556.078 2556.078 main.py:1(<module>)
        1    0.000    0.000 2556.078 2556.078 {built-in method builtins.exec}
        2   36.727   18.364   36.727   18.364 {built-in method builtins.input}
 16777217    2.615    0.000    2.615    0.000 {built-in method builtins.len}
 16777216 2372.579    0.000 2372.579    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile output with input as "with thunderous applause" and printing of the generated strings (i also removed an extra call to input() i was using to see where it stopped taking input of the bee movie script)
         16777221 function calls in 113.941 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1  102.824  102.824  113.941  113.941 main.py:1(<module>)
        1    0.000    0.000  113.941  113.941 {built-in method builtins.exec}
        1    9.974    9.974    9.974    9.974 {built-in method builtins.input}
 16777217    1.143    0.000    1.143    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

it looks like it would save me around a second to not keep the calculated length in a variable
I'm  guessing that the rest of the unaccounted for time is string concatenation so thats probably somewhere to look for optimization
 """