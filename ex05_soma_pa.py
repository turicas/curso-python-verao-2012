def cria_soma_pa(a_1, r):
    def soma_pa(n):
        a_n = a_1 + (n - 1) * r
        return (a_1 + a_n) * n / 2.0
    return soma_pa
