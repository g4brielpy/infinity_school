class Funcionario:
    def __init__(self, nome: str, setor: str, cargo: str, salario_bruto: float) -> None:
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.salario_bruto = salario_bruto

    def dadosFuncionarios(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Setor: {self.setor}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário Bruto: {self.salario_bruto}")
        print(f"{self.calcularSalarioLiquido()}")
        print(f"Valor IR: R$ {self.calcularIR()}\n")

    def calcularSalarioLiquido(self) -> str:
        setor = self.setor.lower()
        desconto_sindical: float = 0.03 * self.salario_bruto
        desconto_ir = self.calcularIR()

        match setor:
            case "ti":
                desconto: float = (
                    0.05 * self.salario_bruto) + desconto_sindical
            case "rh":
                desconto: float = (
                    0.04 * self.salario_bruto) + desconto_sindical
            case _:
                desconto = desconto_sindical

        salario_liquido = (self.salario_bruto - desconto) - desconto_ir
        return f"Salario líquido: R$ {salario_liquido:,.2f}"

    def calcularIR(self) -> float:
        salario = self.salario_bruto

        if (salario < 3_000):
            return 0
        elif (salario >= 3_000 and salario < 5_000):
            desconto_ir: float = 0.08 * salario
        elif (salario >= 5_000 and salario < 8_000):
            desconto_ir: float = 0.08 * salario
        elif (salario >= 8_000 and salario < 10_000):
            desconto_ir: float = 0.12 * salario
        else:
            desconto_ir: float = 0.15 * salario

        return desconto_ir


funcionario = Funcionario(
    nome="Gabriel",
    setor="ti",
    cargo="Desenvolver",
    salario_bruto=4_000.00
)
funcionario.dadosFuncionarios()

funcionario.salario_bruto = 8_500.00
funcionario.dadosFuncionarios()
