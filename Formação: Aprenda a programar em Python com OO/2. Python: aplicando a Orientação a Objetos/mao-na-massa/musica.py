class Musica:
    nome = ''
    artista = ''
    duracao = int

musica_isa = Musica()
musica_isa.nome = 'Mirror'
musica_isa.artista = 'Justin Timberlake'
musica_isa.duracao = (4 * 60) + 38

print(f'A música favorita de Isa 💓 é {musica_isa.nome} do {musica_isa.artista}, que possui duração de {musica_isa.duracao} segundo.')