def addBinary(a: str, b: str) -> str:
        n = max(len(a),len(b))
        a,b = a.zfill(n), b.zfill(n)

        carrier = 0
        output = ""
  
        for i in range(n-1, -1, -1):

            if a[i] == "0" and b[i] == "0":
                if carrier == 1:
                    output = output + "1"
                    carrier = 0
                else:
                    output = output + "0"
            elif a[i] == "1" and b[i] == "0" or (a[i] == "0" and b[i] == "1"):
                if carrier == 1:
                    output = output + "0"
                else:
                    output = output + "1"
            elif a[i] == "1" and b[i] == "1":
                if carrier == 1:
                    output = output + "1"
                    carrier = 1
                else:
                    output = output + "0"
                    carrier = 1
        if carrier == 1:
            output = output + "1"

        return output[::-1]

def main():
    print(addBinary("11", "1"))
    print(addBinary("1010", "1011"))

main()