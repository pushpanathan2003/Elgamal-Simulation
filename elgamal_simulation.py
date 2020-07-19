def egcd(a, b):
    if( a==0):
        return (b, 0, 1)
    else:
        g, y, x =egcd(b%a, a)
        return (g, x-(b//a)*y, y)

def modinv( a, n ):
    g, x, y = egcd(a, n)
    if ( g != 1):
        raise Exception('modular inverse does not exists')
    else:
        return x%n

def addition ( p1, p2, a, p ):
    if( p1[0] == p2[0] ):
        if( p1[1] == p2[1] ):
            l_numerator = (3*p1[0]*p1[0] + a )
            l_denominator = 2*p1[1]
            l = (l_numerator * modinv(l_denominator, p) )%p

    else:
        l_numerator = (p2[1]-p1[1])%p
        l_denominator = (p2[0]-p1[0])%p
        l = (l_numerator * modinv(l_denominator, p) )%p

    result =[]
    result.append ( (l*l - p1[0] - p2[0])%p )
    result.append ( (l*(p1[0] - result[0]) - p1[1])%p )
    
    return result


def multiply ( point, n, a, p ):
    result = point

    for i in range(0, n-1):
        temp = addition( result, point, a, p )
        result = temp

    return result


def encryption( plain_text, e1, e2, a, p ):
    r = int(input("Enter r value : " ))
    c1 = multiply( e1, r, a, p)

    c2 = multiply ( e2, r, a, p )
    temp = addition ( plain_text, c2, a, p )
    
    c2 = temp

    return c1, c2

def decryption( c1, c2, d, a, p ):
    plain_text = multiply ( c1, d, a, p )
    plain_text[1] = -plain_text[1]

    temp = addition( c2, plain_text, a, p )
    plain_text = temp

    return plain_text

if __name__ == "__main__":
    p = int(input("Enter p value : "))
    a = int(input("Enter a value : "))
    b = int(input("Enter b value : "))
    e1 = []
    print ( "Enter e1 : " )
    e1.append( int(input()) )
    e1.append( int(input()) )

    d = int(input("Enter  d : "))

    e2 = multiply ( e1, d, a, p )
    
    plain_text = []
    print ( "Enter plain text : " )
    plain_text.append ( int(input()) )
    plain_text.append ( int(input()) )

    c1, c2 = encryption ( plain_text, e1, e2, a, p )

    print ( "Cipher Text : " )
    print ( c1 )
    print ( c2 )

    P = decryption ( c1, c2, d, a, p )
    print ( "Plain Text : " )
    print ( P )
