class A():
    def f(self):
        print("foo")

def main():
    obj_A = A() # O objeto sendo instanciado a partir da classe A
    obj_A.f() # Chamando o método f do objeto obj_A

if __name__ == "__main__":
    main()