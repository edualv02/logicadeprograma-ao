def pedir_pizza():
  """
  Função que simula o pedido de pizza, calculando o valor total e armazenando informações sobre os pedidos.
  """

  pedido_mais_caro

  while True:

    valor_total = 0

    
    tamanho = input("Escolha o tamanho da pizza (Pequena - R$20, Média - R$30, Grande - R$40): ").upper()
    if tamanho == "PEQUENA":
      valor_total += 20
    elif tamanho == "MEDIA":
      valor_total += 30
    elif tamanho == "GRANDE":
      valor_total += 40
    else:
      print("Tamanho inválido. Por favor, escolha entre Pequena, Média ou Grande.")
      continue

    
    ingredientes_extras = input("Deseja adicionar ingredientes extras (Calabresa, Mussarela, Tomate, Cebola, Bacon)? (Sim/Não): ").upper()
    if ingredientes_extras == "SIM":
      while True:
        extra = input("Digite o ingrediente extra (ou 'sair' para finalizar): ").upper()
        if extra == "SAIR":
          break
        elif extra in ["CALABRESA", "MUSSARELA", "TOMATE", "CEBOLA", "BACON"]:
          valor_total += 5
        else:
          print("Ingrediente inválido. Por favor, escolha entre Calabresa, Mussarela, Tomate, Cebola ou Bacon.")
    
    
    refrigerante = input("Deseja adicionar um refrigerante (R$ 3,00)? (Sim/Não): ").upper()
    if refrigerante == "SIM":
      valor_total += 3

    
    pedidos.append(valor_total)

    
    novo_pedido = input("Deseja fazer um novo pedido? (Sim/Não): ").upper()
    if novo_pedido != "SIM":
      break

  
  pedido_mais_caro = max(pedidos)
  pedido_mais_barato = min(pedidos)
  quantidade_pedidos = len(pedidos)

  print("\nResumo dos pe