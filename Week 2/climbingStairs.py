def climbStairs(n: int) -> int:
        CounterOne = 1
        CounterTwo = 2

        #We start with index 2
        Index = 2

        if n == 1:
                return 1
        if n == 2:
                return 2

        while Index < n:
            aux = CounterTwo
            CounterTwo = CounterOne + CounterTwo
            CounterOne = aux
            Index += 1

        return CounterTwo

def main():
    print(climbStairs(4))

main()