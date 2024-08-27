import os
import xml.etree.ElementTree as ET

def main():
    option = 0
    disciplina_name = ""
    professor_name = ""
    suporte_ou_asa = 0

    while(not option or not 0 < option <= 3):
        try:
            option = int(input(f"""Olá!

    1. Pesquisa de Satisfação de Disciplina
    2. Pesquisa de Satisfação de Professores
    3. Pesquisa de Satisfação de ASA/Tutores

    Digite a opção desejada: """))
        except ValueError:
            print("\nDigite um valor válido\n", ValueError)

    match option:
        case 1:
            disciplina_name = input("Digite o nome da disciplina: ")
        case 2:
            disciplina_name = input("Digite o nome da disciplina: ")
            professor_name = input("Digite o nome do(a) professor(a): ")
        case 3:
            disciplina_name = input("Digite o nome da disciplina: ")
            while(not suporte_ou_asa or not 0 < suporte_ou_asa <= 2):
                try:
                    suporte_ou_asa = int(input(f"""
    1. Suporte de Orientação
    2. ASA
                               
    Escolha a opção: """))
                except:
                    print("\nDigite um valor válido\n")

    modelos = (
        'ModeloDisciplina',
        'ModeloProfessor',
        'ModeloASA_SuporteDeOrientação',
    )

    modelo = modelos[option - 1]

    tree = ET.parse(modelo + '.xml')
    root = tree.getroot()

    for elem in root.iter():
        if elem.text:
            if professor_name and 'NOME_PROFESSOR' in elem.text:
                elem.text = elem.text.replace('NOME_PROFESSOR', professor_name)
            if disciplina_name and 'NOME_DISCIPLINA' in elem.text:
                elem.text = elem.text.replace('NOME_DISCIPLINA', disciplina_name)
            if suporte_ou_asa and 'ASA_OU_SUPORTE' in elem.text:
                replacement = 'SUPORTE DE ORIENTAÇÃO' if suporte_ou_asa == 1 else 'ASA'
                elem.text = elem.text.replace('ASA_OU_SUPORTE', replacement)

    output_file_names = (
        'disciplina_output',
        'professor_output',
        'ASA_SuporteDeOrientacao_output'
    )

    output_file_name = output_file_names[option - 1]

    output_path = os.path.join('output', output_file_name + '.xml')

    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    
    input(f'Arquivo criado em {output_path}')

if __name__ == "__main__":
    main()