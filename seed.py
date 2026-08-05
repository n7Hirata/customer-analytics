import requests


BASE_URL = "http://localhost:8000"

def seed_clients():
    clients = [{"name":"Joao Santos", "email":"joao@gmail.com"},
              {"name":"Maria Eduarda", "email":"maria@gmail.com"}, 
              {"name":"Lucas Silva", "email":"lucas@gmail.com"}, 
              {"name":"Bruna da Silva", "email":"bruna@gmail.com"}]
    
    for client in clients:
        response = requests.post(f"{BASE_URL}/clients", json=client)
        if response.status_code == 200:
            data = response.json()
            print(f"  OK: {data['name']} (ID: {data['id']})")
        else:
            print(f"  NOT:  {client['name']}: {response.json()['detail']}")
            
def seed_tickets():
    tickets = [{
                    "ticket_id":164, 
                    "client_id": 2, 
                    "subject": "Pc não liga", 
                    "status": "closed", 
                    "priority": "low", 
                    "tags":"pc, bug"
                },
               {
                   "ticket_id":623, 
                    "client_id": 4, 
                    "subject": "Servidor travou", 
                    "status": "resolved", 
                    "priority": "high", 
                    "tags":"servidor, bug"
                },
               {
                   "ticket_id":273,
                    "client_id": 5,
                    "subject": "Impressora acabou a tinta",
                    "status": "pendente", 
                    "priority": "normal", 
                    "tags":"impressora, toner"
                },
               {
                    "ticket_id": 165,
                    "client_id": 3,
                    "subject": "Erro ao emitir nota fiscal eletrônica",
                    "status": "pending",
                    "priority": "high",
                    "tags": "fiscal, sistema"
                },
               {
                    "ticket_id": 166,
                    "client_id": 4,
                    "subject": "Impressora não responde na rede",
                    "status": "resolved",
                    "priority": "normal",
                    "tags": "impressora, rede"
                },
                {
                    "ticket_id": 167,
                    "client_id": 2,
                    "subject": "Lentidão ao carregar relatórios mensais",
                    "status": "pending",
                    "priority": "low",
                    "tags": "desempenho, relatorios"
                },
                {
                    "ticket_id": 168,
                    "client_id": 5,
                    "subject": "Solicitação de redefinição de senha",
                    "status": "closed",
                    "priority": "low",
                    "tags": "acesso, usuario"
                },
                {
                    "ticket_id": 169,
                    "client_id": 6,
                    "subject": "Queda constante da conexão Wi-Fi",
                    "status": "pending",
                    "priority": "high",
                    "tags": "wifi, rede"
                },
                {
                    "ticket_id": 170,
                    "client_id": 3,
                    "subject": "Monitor piscando durante o uso",
                    "status": "resolved",
                    "priority": "normal",
                    "tags": "hardware, monitor"
                },
                {
                    "ticket_id": 171,
                    "client_id": 2,
                    "subject": "Falha no backup automático diário",
                    "status": "pending",
                    "priority": "high",
                    "tags": "backup, servidor"
                },
                {
                    "ticket_id": 172,
                    "client_id": 4,
                    "subject": "Teclado e mouse USB pararam de funcionar",
                    "status": "closed",
                    "priority": "low",
                    "tags": "perifericos, hardware"
                },
                {
                    "ticket_id": 173,
                    "client_id": 6,
                    "subject": "Email corporativo não recebe anexos",
                    "status": "resolved",
                    "priority": "normal",
                    "tags": "email, comunicacao"
                },
                {
                    "ticket_id": 174,
                    "client_id": 3,
                    "subject": "Tela azul de erro no Windows",
                    "status": "pending",
                    "priority": "high",
                    "tags": "so, crash"
                },
                {
                    "ticket_id": 175,
                    "client_id": 5,
                    "subject": "Dúvida sobre alteração de cadastro de cliente",
                    "status": "closed",
                    "priority": "low",
                    "tags": "suporte, sistema"
                },
                {
                    "ticket_id": 176,
                    "client_id": 2,
                    "subject": "Sem acesso à pasta compartilhada na rede",
                    "status": "pending",
                    "priority": "normal",
                    "tags": "permissao, rede"
                },
                {
                    "ticket_id": 177,
                    "client_id": 6,
                    "subject": "Troca de toner da impressora do RH",
                    "status": "resolved",
                    "priority": "low",
                    "tags": "impressora, suprimentos"
                },
                {
                    "ticket_id": 178,
                    "client_id": 4,
                    "subject": "Nobreak apitando continuamente",
                    "status": "pending",
                    "priority": "high",
                    "tags": "energia, hardware"
                }
               ]
    
    for ticket in tickets:
        response = requests.post(f"{BASE_URL}/tickets", json=ticket)
        if response.status_code == 200:
            data = response.json()
            print(f"  OK: {data['subject']} (TICKET ID: {data['ticket_id']})")  
        else:
            try:
                detail = response.json().get("detail", "Erro desconhecido")
            except Exception:
                detail = f"Erro {response.status_code}: {response.text[:100]}"
            print(f"  Ticket {ticket['ticket_id']}: {detail}")
            
def test_metrics():
    for client_id in range(2, 6):
        response = requests.get(f"{BASE_URL}/metrics/{client_id}")
        if response.status_code == 200:
            metric = response.json()
            print(f"\n{metric['client_name']} ({metric['client_email']})")
            print(f"  Tickets: {metric['total_tickets']} total | {metric['open_tickets']} abertos | {metric['resolved_tickets']} resolvidos")
            print(f"  Taxa de resolução: {metric['resolution_rate']}%")
            print(f"  Frequência média: {metric['avg_days_tickets']} dias entre tickets")
            print(f"  Top tags: {', '.join(metric['top_tags'])}")
            print(f"  Top assuntos: {', '.join(metric['top_subjects'])}")
            

if __name__ == "__main__":
    seed_clients()
    seed_tickets()
    test_metrics()