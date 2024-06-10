class Veiculo:
	
	def __init__(self, marca, velocidade_max, quilometros_litro): 
		self.marca = marca
		self.velocidade_max = velocidade_max
		self.quilometros_litro = quilometros_litro
			
	def quantidade_assentos(self, quantidade):
		print(f"A capacidade de assentos é {quantidade}")
				
	def mostrar(self):
		print(f"Marca = {self.marca}")
		print(f"Velocidade Máxima = {self.velocidade_max}")
		print(f"Quilômetros por Litro = {self.quilometros_litro}")
	
modelo_carro = Veiculo("Gol", 80, 5)
modelo_carro.mostrar()

print(40 * "=")

class Onibus(Veiculo):
	def quantidade_assentos(self, quantidade=40):
		return super().quantidade_assentos(quantidade)

onibus = Onibus("Escola", 100, 10)
onibus.mostrar()
onibus.quantidade_assentos()  # Correção: chamar o método sem passar argumentos
