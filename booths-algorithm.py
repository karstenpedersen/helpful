def neg(b: str) -> str:
    if b == "0":
        return "1"
    
    return "0"


def add(x: str, y: str) -> (str, bool):
    x = x[::-1]
    y = y[::-1]

    def aux(xx: str, yy:str, c = False) -> (str, bool):
        cc = sum([xx == "1", yy == "1", c])

        if cc == 0:
            return "0", False
        elif cc == 1:
            return "1", False
        elif cc == 2:
            return "0", True
        return "1", True


    result = ""
    carry = False
    for xx, yy in zip(x, y):
        new, carry = aux(xx, yy, carry)
        result += new

    return result[::-1], carry


def negate_twos_complement(x: str) -> str:
    inverse = ""
    found_one = False
    for b in x[::-1]:
        if found_one:
            inverse += neg(b)
        else:
            if b == "1":
                found_one = True
            inverse += b
    return inverse[::-1]


def twos_complement_to_decimal(x: str):
    result = 0
    for i, xx in enumerate(x[::-1]):
        if xx == "0":
            continue
        if i == len(x) - 1:
            result -= 2**i
            break
        result += 2 ** i
    return result



def booths_algorithm(m: str, q: str):
    neg_m = negate_twos_complement(m)
    a = "0" * len(q)
    q_ = "0"

    # Counters
    cycle = 0
    additions = 0
    subtractions = 0
    skips = 0
    
    print("Values")
    print(f"  Q = {q}")
    print(f"Q_1 = {q_}")
    print(f"  M = {m}")
    print(f" -M = {neg_m}")
    print()

    # Calculation
    print("-----------------------------------------")
    print(f"{cycle}   {a}   {q}   {q_}")
    for i in range(len(q)):
        cycle += 1
        qq = q[::-1][0] + q_

        print("-----------------------------------------")
        print(f"{cycle}   {a}   {q}   {q_}")

        if qq == "10":
            # Subtract
            print(f"   +{neg_m}")
            print(f"  -------")
            a, _ = add(a, neg_m)
            print(f"    {a}   {q}   {q_}")
            subtractions += 1
        elif qq == "01":
            #add
            print(f"   +{m}")
            print(f"  -------")
            a, _ = add(a, m)
            print(f"    {a}   {q}   {q_}")
            additions += 1 

        # Shift
        a0 = a[::-1][0]
        a = a[0] + a[:-1]
        q0 = q[::-1][0]
        q = a0 + q[:-1]
        q_ = q0
        print(f"    {a}   {q}   {q_}")

    # Result
    result = a + q


    decimal_result = twos_complement_to_decimal(result)

    print(f"\nResult: {result}\nDecimal value: {decimal_result}")

    decimal_m = twos_complement_to_decimal(m)
    decimal_q = twos_complement_to_decimal(q)
    print(f"q * m = {decimal_q} * {decimal_m} = {decimal_result}")


    skips = cycle - subtractions - additions
    print(f"\nStats:\nCycles: {cycle}\nAdditions: {additions}\nSubtracttions: {subtractions}\nSkips: {skips}")

    return a + q


if __name__ == "__main__":
    booths_algorithm("0111", "1101")
    # print(add("0000", "1001"))
