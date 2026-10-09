import re
from abc import ABC, abstractmethod

class Produto(ABC):
    """Classe abstrata representando um produto genérico."""
    def __init__(self, nome, preco):
        self._nome = nome
        self.preco = preco # Utiliza o setter com validação

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("O nome do produto não pode ser vazio e deve ser texto.")
        self._nome = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError(f"O preço do produto '{self._nome}' deve ser um número positivo. Valor recebido: {valor}")
        self._preco = float(valor)

    @abstractmethod
    def calcular_preco_final(self):
        """Método abstrato para calcular o preço final com descontos ou impostos."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome} - R$ {self.preco:.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.nome}', {self.preco})"

    # Métodos Dunder de comparação baseados no preço
    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco == outro.preco

    def __lt__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.preco < outro.preco


class Livro(Produto):
    """Classe filha de Produto que representa um Livro."""
    def __init__(self, nome, preco, autor, paginas):
        super().__init__(nome, preco)
        self.autor = autor
        self.paginas = paginas

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        if not valor.strip():
            raise ValueError("O autor não pode ser vazio.")
        self._autor = valor

    @property
    def paginas(self):
        return self._paginas

    @paginas.setter
    def paginas(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("A quantidade de páginas deve ser um número inteiro maior que zero.")
        self._paginas = valor

    def calcular_preco_final(self):
        """Livros possuem isenção de impostos e ganham 10% de desconto."""
        return self.preco * 0.90

    def __str__(self):
        return f"{super().__str__()} (Autor: {self.autor}, {self.paginas} págs)"

    def __repr__(self):
        return f"Livro('{self.nome}', {self.preco}, '{self.autor}', {self.paginas})"


class Eletronico(Produto):
    """Classe filha de Produto que representa um Eletrônico."""
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem

    @property
    def voltagem(self):
        return self._voltagem

    @voltagem.setter
    def voltagem(self, valor):
        if valor not in [110, 220, 'Bivolt']:
            raise ValueError("A voltagem deve ser 110, 220 ou 'Bivolt'.")
        self._voltagem = valor

    def calcular_preco_final(self):
        """Eletrônicos sofrem acréscimo de 15% de imposto."""
        return self.preco * 1.15

    def __str__(self):
        return f"{super().__str__()} (Voltagem: {self.voltagem})"

    def __repr__(self):
        return f"Eletronico('{self.nome}', {self.preco}, '{self.voltagem}')"


class Cliente:
    """Classe independente para validar informações do Cliente."""
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("O nome do cliente não pode ser vazio.")
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        padrao_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(padrao_email, valor):
            raise ValueError(f"E-mail inválido: {valor}")
        self._email = valor

    def __str__(self):
        return f"Cliente: {self.nome} ({self.email})"

    def __repr__(self):
        return f"Cliente('{self.nome}', '{self.email}')"


def executar_testes():
    print("=" * 50)
    print(" INICIANDO TESTES E DEMONSTRAÇÃO ".center(50, "="))
    print("=" * 50)

    # 1. Tratamento de Exceções (Testando validações do @property)
    print("\n--- TESTANDO VALIDAÇÕES DE ERRO ---")
    try:
        # Preço negativo
        produto_invalido = Livro("Livro Ruim", -50, "Autor Desconhecido", 100)
    except ValueError as e:
        print(f"Erro capturado com sucesso: {e}")

    try:
        # Páginas inválidas
        livro_invalido = Livro("Livro Pequeno", 20, "Autor", 0)
    except ValueError as e:
        print(f"Erro capturado com sucesso: {e}")

    try:
        # E-mail inválido
        cliente_invalido = Cliente("José", "email-sem-arroba.com")
    except ValueError as e:
        print(f"Erro capturado com sucesso: {e}")

    # 2. Criação de Instâncias Válidas (10 objetos)
    print("\n--- CRIANDO 10 INSTÂNCIAS VÁLIDAS ---")
    
    clientes = [
        Cliente("Maria Silva", "maria@gmail.com"),
        Cliente("João Souza", "joao@empresa.com.br"),
        Cliente("Ana Costa", "ana@dominio.com")
    ]
    
    produtos = [
        Livro("Dom Quixote", 80.00, "Miguel de Cervantes", 1056),
        Livro("O Senhor dos Anéis", 120.00, "J.R.R. Tolkien", 1200),
        Livro("1984", 45.00, "George Orwell", 328),
        Livro("A Revolução dos Bichos", 30.00, "George Orwell", 152),
        Eletronico("Smartphone Galaxy", 2500.00, "Bivolt"),
        Eletronico("TV LED 50\"", 3200.00, 110),
        Eletronico("Notebook Dell", 4500.00, "Bivolt")
    ]

    for c in clientes:
        print(repr(c)) # Usando __repr__

    # 3. Demonstrando Polimorfismo e __str__
    print("\n--- DEMONSTRANDO POLIMORFISMO (calcular_preco_final) ---")
    total_original = 0
    total_com_descontos_e_impostos = 0

    for prod in produtos:
        # Imprime usando __str__
        print(prod)
        
        # Chama o método polimórfico calcular_preco_final()
        preco_final = prod.calcular_preco_final()
        
        print(f"   -> Preço Original: R$ {prod.preco:.2f} | Preço Final: R$ {preco_final:.2f}\n")
        
        total_original += prod.preco
        total_com_descontos_e_impostos += preco_final

    print("-" * 50)
    print(f"Soma dos preços originais: R$ {total_original:.2f}")
    print(f"Soma dos preços finais: R$ {total_com_descontos_e_impostos:.2f}")

    # 4. Demonstrando Métodos Mágicos de Comparação (__eq__ e __lt__)
    print("\n--- DEMONSTRANDO COMPARAÇÃO (__eq__ e __lt__) ---")
    prod1 = produtos[2] # 1984, R$ 45.00
    prod2 = produtos[3] # A Revolução dos Bichos, R$ 30.00
    prod3 = Livro("Livro com mesmo preço", 45.00, "Autor", 100)

    print(f"{prod1.nome} (R$ {prod1.preco}) < {prod2.nome} (R$ {prod2.preco})? -> {prod1 < prod2}")
    print(f"{prod2.nome} (R$ {prod2.preco}) < {prod1.nome} (R$ {prod1.preco})? -> {prod2 < prod1}")
    print(f"{prod1.nome} (R$ {prod1.preco}) == {prod3.nome} (R$ {prod3.preco})? -> {prod1 == prod3}")

if __name__ == "__main__":
    executar_testes()

