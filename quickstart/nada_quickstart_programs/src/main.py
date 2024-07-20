from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))
    
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    r = my_int1 * my_int2
    r3 = my_int1 / my_int2
    r4 = (my_int1 + my_int2) * (my_int1 - my_int2)

    int1 = my_int1 + Integer(1)
    int2 = my_int2 + Integer(1)

    def max(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a < b).if_else(b, a)

    r6 = (my_int1 + my_int2) * ((my_int1 * my_int1) - (my_int1 * my_int2) + (my_int2 * my_int2))
    r1 = max(my_int1, my_int2)
    r5 = Integer(0)
    r7 = (b * b) - (a * c )* Integer(4)
    x = r7 / Integer(2)
    for _ in range(10):
        x = (x + r7 / x) / Integer(2)
    sqrt_discriminant = x

    two_a = a * Integer(2)
    neg_b = b * Integer(-1)

    r8 = (neg_b + sqrt_discriminant) /two_a
    r9 = (neg_b - sqrt_discriminant) / two_a
    

    
    out1 = Output(r1, "Maximum of two Numbers", party1)
    out2 = Output(r, "Multiplication of Two Numbers", party1)
    out3 = Output(r3, "Division of Two Numbers", party1)
    out4 = Output(r4, "(a^2-b^2)=(a+b)(a-b) =", party1)
    out5 = Output(r8, "Root 1 of the quadratic equation 1x^2-4x+4=0", party1)
    out6 = Output(r9, "Root 2 of the quadratic equation 1x^2-4x+4=0", party1)
       
    return [out5, out6, out1,out2,out3,out4]