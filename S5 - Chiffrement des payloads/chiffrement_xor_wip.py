
def Xor(inp,key):
    #TODO
    return []

def toCdecl(ch,prefix="char tab"):
    outp=list(ch)
    return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""

if __name__ == '__main__':
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","F")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","5")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","F5")))
    print (toCdecl(Xor("TRAVAUX PRATIQUES ISIMA","ZZ2_F5")))
    print (toCdecl(Xor("ZZ2_F5","F5")))