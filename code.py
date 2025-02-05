
import requests
import pandas as pd
from datetime import datetime

#(exemplo com uma API hipotética)
def consultar_antecedentes(nome, data_nascimento):
    # URL da API (exemplo fictício)
    url = "https://api.antecedentes.gov.br/consultar"
    
    params = {
        "nome": nome,
        "data_nascimento": data_nascimento
    }
    # Requisição para a API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        dados = response.json()
        
        if dados.get("status") == "sucesso":
            return dados["resultados"]
        else:
            return {"erro": "Nenhum resultado encontrado ou erro na consulta"}
    else:
        return {"erro": f"Erro na consulta: {response.status_code}"}

def gerar_relatorio(nome, data_nascimento, antecedentes):
    df = pd.DataFrame(antecedentes)
    
    df['Nome'] = nome
    df['Data de Nascimento'] = data_nascimento
    
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    arquivo_relatorio = f"relatorio_antecedentes_{nome.replace(' ', '_')}_{agora}.csv"
    
    df.to_csv(arquivo_relatorio, index=False)
    
    print(f"Relatório gerado: {arquivo_relatorio}")
    print(df)

# Exemplo de uso
nome = "João Silva"
data_nascimento = "1985-05-15"  # Exemplo de data no formato YYYY-MM-DD

antecedentes = consultar_antecedentes(nome, data_nascimento)

if "erro" not in antecedentes:
    gerar_relatorio(nome, data_nascimento, antecedentes)
else:
    print(antecedentes["erro"])

