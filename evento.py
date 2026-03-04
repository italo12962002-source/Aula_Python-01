workshop_1 = {"Victor","Italo","Brenda","Alice","Maria","Victor","Gustavo"}
workshop_2 = {"Thiago","Gabriel","Doglas","Caio","Heitor","Caio","Gustavo"}

participantes_a = set(workshop_1)
participantes_b = set(workshop_2)

print(f"Participantes do primeiro evento: {participantes_a}")
print(f"Participantes do segundo evento: {participantes_b}")

todos_participantes = participantes_a.union(participantes_b)

print(f"\nLista de todos os participantes:{todos_participantes}")

print(f"\nA quantidade de participantes é: {len(todos_participantes)}")

ambos_workshop = participantes_a.intersection(participantes_b)
print(f"Participantes nos dois Workshops: {ambos_workshop}")

so_a = participantes_a.difference(participantes_b)

print(f"Apenas participantes do primeiro evento: {so_a}")