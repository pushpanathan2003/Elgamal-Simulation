def egcd(a, b):
    if ( a == 0 ):
        return (b, 0, 1)
    else:
        g, y, x = egcd( b%a, a)
        return (g, x-(b//a)*y, y)

def modinv(a, n):
    g, x, y = egcd(a, n)
    if ( g != 1 ):
        raise Exception('modular inverse does not exists')
    else:
        return x%n

def encryption ( e1, e2, p, plain_text ):
    r = int(input("Enter r : "))
    c1 = pow(e1, r, p)
    c2 = plain_text * pow(e2, r, p)
    c2 = pow(c2, 1, p)
    return c1, c2

def decryption ( c1, c2, d, p ):
    c1_d = pow(c1, d, p)
    c1_d_inverse = modinv( c1_d, p )
    return (c2 * c1_d_inverse)% p

if __name__ == "__main__":
    p = int(input("Enter p : "))
    d = int(input("Enter d : "))
    e1 = int(input("Enter e1 : "))
    e2 = pow(e1, d, p)
    print ( "e2 value : " + str(e2) )

    plain_text = int(input("Enter plain text : "))
    c1, c2 = encryption ( e1, e2, p, plain_text )
    print ( "c1 : " + str(c1) )
    print ( "c2 : " + str(c2) )
    
    P = decryption ( c1, c2, d, p )
    print ( "Plain_text : " + str(P) )
