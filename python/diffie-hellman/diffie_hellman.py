"""
Diffie Hellman Key Exchange
"""
import secrets

def private_key(p):
    """
    Generate a private key for use in the Diffie-Hellman key exchange.
    :param p: A prime number.
    :return: A random integer in the range [2, p)
    """
    return secrets.choice(range(2,p))


def public_key(p, g, private):
    """
    Generate a public key corresponding to the given private key.
    :param p: A prime number.
    :param g: A prime number.
    :param private: The private key.
    :return: The public key: g**private mod p
    """
    return (g**private) % p
    


def secret(p, public, private):
    """
    Calculate the shared secret.
    :param p: A prime number.
    :param public: The public key.
    :param private: The private key.
    """
    return (public**private) % p
    