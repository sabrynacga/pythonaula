import sys

# Definindo o módulo exigido pelo problema
MOD = 10**9 + 7

def solve():
    # Lê toda a entrada e quebra em uma lista de inteiros
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    L1, R1, L2, R2, L3, R3 = map(int, input_data)
    
    # DP por Dígitos: Conta X <= A, Y <= B tal que X ^ Y <= C
    def f(A, B, C):
        if A < 0 or B < 0 or C < 0:
            return 0
        
        memo = {}
        
        def dp(bit, tA, tB, tC):
            # Condição de parada: se passamos pelo bit 0, encontramos 1 combinação válida
            if bit == -1:
                return 1
            
            state = (bit, tA, tB, tC)
            if state in memo:
                return memo[state]
            
            ans = 0
            bitA = (A >> bit) & 1
            bitB = (B >> bit) & 1
            bitC = (C >> bit) & 1
            
            # Testa as possibilidades para o bit i-ésimo de X e Y (0 ou 1)
            for x in range(2):
                if tA and x > bitA:
                    continue
                for y in range(2):
                    if tB and y > bitB:
                        continue
                        
                    z = x ^ y
                    if tC and z > bitC:
                        continue
                    
                    # Atualiza as restrições para a próxima chamada
                    ntA = tA and (x == bitA)
                    ntB = tB and (y == bitB)
                    ntC = tC and (z == bitC)
                    
                    ans += dp(bit - 1, ntA, ntB, ntC)
                    
            memo[state] = ans
            return ans
        
        # Inicia do 30º bit (pois 2^30 > 10^9), assumindo que estão no limite ("tight") no começo
        return dp(30, True, True, True)

    # Princípio da Inclusão-Exclusão para cruzar todos os limites L_i e R_i
    W = (f(R1, R2, R3) 
       - f(L1 - 1, R2, R3) - f(R1, L2 - 1, R3) + f(L1 - 1, L2 - 1, R3)
       - f(R1, R2, L3 - 1) 
       + f(L1 - 1, R2, L3 - 1) + f(R1, L2 - 1, L3 - 1) - f(L1 - 1, L2 - 1, L3 - 1))
       
    # Total de combinações T (Cálculos de combinações brutas)
    T = (R1 - L1 + 1) * (R2 - L2 + 1) * (R3 - L3 + 1)
    
    # O total de vezes que a Alice VENCE é Total - Derrotas (W)
    win_ways = (T - W) % MOD
    T_mod = T % MOD
    
    # Probabilidade final no modelo modular (P * Q^-1 mod 10^9+7)
    ans = (win_ways * pow(T_mod, MOD - 2, MOD)) % MOD
    print(ans)

if __name__ == '__main__':
    solve()