def gen():
    for i in range(5):
       yield(i)
       # yield is used to stop execution of full loop and to run it as per over requirements.

gen1 = gen()
print(next(gen1)) #by next() you can run loop as per your own requirements.
print(next(gen1))
print("hello1")
print(next(gen1))
print(next(gen1))
print("hello2")
print(next(gen1))
