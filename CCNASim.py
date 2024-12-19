import random

# Lista de questões simuladas
questions = [
    {
        "question": "O que é uma máscara de sub-rede e qual sua função em uma rede?",
        "options": {
            "a": "Define o gateway padrão",
            "b": "Separa a rede do host",
            "c": "Configura o DNS",
            "d": "Gerencia a VLAN",
        },
        "correct": "b",
    },
    {
        "question": "Qual protocolo é usado para acessar dispositivos de rede de forma segura?",
        "options": {
            "a": "Telnet",
            "b": "SSH",
            "c": "FTP",
            "d": "HTTP",
        },
        "correct": "b",
    },
    {
        "question": "Qual é a função do protocolo ARP?",
        "options": {
            "a": "Resolver nomes de domínio",
            "b": "Mapear endereços IP para MAC",
            "c": "Fornecer endereços IP automáticos",
            "d": "Configurar rotas estáticas",
        },
        "correct": "b",
    },
    {
        "question": "O que é DHCP e qual é sua principal função?",
        "options": {
            "a": "Gerenciar VLANs",
            "b": "Configurar endereços IP automaticamente",
            "c": "Criptografar dados",
            "d": "Resolver nomes de domínio",
        },
        "correct": "b",
    },
    {
        "question": "Qual tecnologia é usada para criar uma conexão segura em redes públicas?",
        "options": {
            "a": "NAT",
            "b": "VPN",
            "c": "VLAN",
            "d": "ICMP",
        },
        "correct": "b",
    },
    {
        "question": "Qual linguagem é comumente usada para automação de redes?",
        "options": {
            "a": "Python",
            "b": "Java",
            "c": "C++",
            "d": "SQL",
        },
        "correct": "a",
    },
]

# Função principal

def run_quiz():
    print("Bem-vindo ao Simulado CCNA! Responda as questões e veja seu desempenho.")
    random.shuffle(questions)
    score = 0

    for idx, q in enumerate(questions, 1):
        print(f"\nQuestão {idx}: {q['question']}")
        for opt, text in q['options'].items():
            print(f"  {opt}) {text}")

        answer = input("Digite sua resposta (a, b, c, ou d): ").strip().lower()
        while answer not in q['options'].keys():
            answer = input("Resposta inválida. Tente novamente (a, b, c, ou d): ").strip().lower()

        if answer == q['correct']:
            print("Correto!")
            score += 1
        else:
            print(f"Errado! A resposta correta era: {q['correct']}) {q['options'][q['correct']]}")

    print(f"\nSimulado concluído! Você acertou {score} de {len(questions)} questões.")

if __name__ == "__main__":
    run_quiz()
