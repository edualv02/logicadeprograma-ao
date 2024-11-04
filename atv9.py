def pedir_pizza():
  """Função para realizar o pedido de pizza."""

  pedidos = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

  while True:
  
    tamanho = input("Escolha o tamanho da pizza (Pequena - R$ 20, Média - R$ 30, Grande - R$ 40): ").upper()
    if tamanho == "PEQUENA":
      preco_pizza = 20
    elif tamanho == "MEDIA":
      preco_pizza = 30
    elif tamanho == "GRANDE":
      preco_pizza = 40
    else:
      print("Tamanho inválido. Por favor, escolha Pequena, Média ou Grande.")
      continue

    
    ingredientes_extras = []
    while True:
      adicionar_ingrediente = input("Deseja adicionar ingredientes extras? (S/N): ").upper()
      if adicionar_ingrediente == "S":
        ingrediente = input("Digite o ingrediente extra (Calabresa, Mussarela, Tomate, Cebola, Bacon): ").upper()
        if ingrediente in ["CALABRESA", "MUSSARELA", "TOMATE", "CEBOLA", "BACON"]:
          ingredientes_extras.append(ingrediente)
          preco_pizza += 5
        else:
          print("Ingrediente inválido. Por favor, escolha entre Calabresa, Mussarela, Tomate, Cebola ou Bacon.")
      elif adicionar_ingrediente == "N":
        break
      else:
        print("Opção inválida. Por favor, digite S ou N.")


    refrigerante = input("Deseja adicionar refrigerante (R$ 3,00)? (S/N): ").upper()
    if refrigerante == "S":
      preco_pizza += 3

    
    pedidos.append(preco_pizza)
    print(f"O valor total do seu pedido é R$ {preco_pizza:.2f}.")

  
    novo_pedido = input("Deseja fazer um novo pedido? (S/N): ").upper()
    if novo_pedido == "N":
      break

  
  print("\nResumo dos pedidos:")
  print(f"Quantidade de pedidos realizados: {len(pedidos)}")
  print(f"Pedido mais caro: R$ {max(pedidos):.2f}")
  print(f"Pedido mais barato: R$ {min(pedidos):.2f}")

pedir_pizza() 

 
 