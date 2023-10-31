diamantes_por_hora_arthur = int(input())
diamantes_por_hora_luiz = int(input())
diamantes_por_hora_pedro = int(input())
tempo_horas_competicao = int(input())

valor_max_diamantes = max(diamantes_por_hora_pedro, diamantes_por_hora_luiz, diamantes_por_hora_arthur) * tempo_horas_competicao

print(valor_max_diamantes)

