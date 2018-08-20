from src.Home import caesar_cipher


def test_proposed():
    assert caesar_cipher.to_encrypt("a b c", 3) == "d e f"
    assert caesar_cipher.to_encrypt("a b c", -3) == "x y z"
    assert caesar_cipher.to_encrypt("simple text", 16) == "iycfbu junj"
    assert caesar_cipher.to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert caesar_cipher.to_encrypt("state secret", -13) == "fgngr frperg"

def test_delta_0():
    assert caesar_cipher.to_encrypt("a b c", 0) == "a b c"