def suma(x, y):
    """
    Test de suma function
    >>> suma(0, 1)
    1
    >>> suma(-1, 1)
    0
    >>> suma("a", "b")
    'ab'
    >>> suma(1.0, "b")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'float' and 'str'
    """
    return x + y

def palindrome(cadena: str):
    """
    Testing palindrome function
    >>> palindrome("oro")
    True
    >>> palindrome("laptop")
    False
    >>> palindrome("")
    True
    >>> palindrome("e")
    True
    >>> palindrome("Ana")
    True
    >>> palindrome("La ruta natural")
    True

    """
    return cadena.lower().replace(" ", "") == cadena[::-1].lower().strip().replace(" ", "")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)