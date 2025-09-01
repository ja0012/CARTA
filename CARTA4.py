#!/usr/bin/python3.13
import requests
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

MODELO = "CA2"          ; url = "http://10.120.120.4:11434/api/generate"  # Endpoint da API do Ollama
#MODELO = "gemma3:12b"   ; url = "http://10.120.120.5:11434/api/generate"  # Endpoint da API do Ollama

def carregar_sessao(nome_sessao=MODELO):
    """Carrega uma sessão salva no Ollama."""
    payload = {
        "model": nome_sessao,
        "prompt": f"/load {nome_sessao}",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao carregar a sessão: {e}")

def salvar_sessao(nome_sessao=MODELO):
    """Salva a sessão atual do Ollama."""
    payload = {
        "model": nome_sessao,
        "prompt": f"/save {nome_sessao}",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao salvar a sessão: {e}")

def gerar_texto_com_ollama(prompt, model=MODELO, max_tokens=1000, temperature=0.7):
    """Envia o prompt para a IA do Ollama e retorna o texto gerado."""
    payload = {
        "model": model,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        generated_text = response.json()["response"]
        return generated_text
    except requests.exceptions.RequestException as e:
        print(f"Erro ao se conectar com o Ollama: {e}")
        return None

def gerar_prompt(nome, demanda):
    """Gera o prompt para a carta de apresentação."""
    return f"""
    Gere uma carta de apresentação personalizada para um cliente, seguindo a estrutura e as instruções abaixo. A carta deve ser persuasiva, profissional e focada em resultados, adaptada às informações específicas do cliente.

---

**INFORMAÇÕES SOBRE O CLIENTE:**
- Nome do cliente: {nome}
- Demanda do cliente: "{demanda}"

---

**SOBRE MIM:**
- Nome: Júlio Costa
- Especialização: Copywriting, Escrita Persuasiva, SEO (Search Engine Optimization)
- Experiência: 5 anos criando textos que aumentam vendas, engajam audiências e melhoram o posicionamento nos motores de busca.
- Personalidade: Criativo, analítico, estratégico e comunicativo. Apaixonado por usar palavras para influenciar comportamentos e gerar resultados.
- Tom de voz: Amigável, profissional e confiável. Adaptável ao público-alvo, seja formal ou descontraído, mas sempre persuasivo e orientado para resultados.

---

**ESTRUTURA DA CARTA:**

1. **Saudação Inicial:**
   - Comece com: "Olá, [nome do cliente]. Como vai?"
   - Em seguida: "Espero que esteja bem!"

2. **Introdução:**
    - Apresente-se brevemente com algo parecido com isso: "Meu nome é Júlio Costa, sou Copywriter Profissional com mais de 5 anos de experiência em criação de textos que aumentam vendas, engajam audiências e melhoram o posicionamento nos motores de busca."
    - Evite frases neutras demais no começo. Troque por algo que já posicione sua autoridade e mostre conexão real com o projeto.
    - Diminua a repetição do seu cargo. Uma vez, bem colocada, é suficiente.

3. **Mencione a Demanda:**
    - Mostre que entendeu a demanda: "Li atentamente sua demanda sobre [breve descrição da demanda] e fiquei entusiasmado com a oportunidade de ajudar."
    - Conecte-se emocionalmente: "Entendo que [mencionar um ponto específico da demanda] é crucial para o sucesso do seu projeto, e estou certo que irei contribuir para o sucesso do seu projeto"

4. **Benefícios do Seu Trabalho:**
   - Liste 3 a 5 benefícios claros e mensuráveis. 
        Por exemplo: 
        --> Aumento de conversões em até 30% com textos otimizados para vendas. 
        --> Melhoria no ranqueamento do seu site nos motores de busca, atraindo mais tráfego orgânico.
        --> Conteúdo personalizado que ressoa com seu público-alvo, aumentando o engajamento e a fidelização. 

5. **Portfólio:**
   - Informe que o portfólio está sendo enviado: "Meu portfólio está sendo enviado em anexo, onde você poderá ver exemplos de projetos anteriores."

6. **Chamada para Ação (CTA):**
   - Ofereça uma próxima etapa clara: "Estou disponível para um bate-papo sem compromisso. Nela, Podemos falar meis sobre o seu projeto e de como posso te ajudar a alcançar os resultados que você deseja. Vamos conversar?"
   - Exemplo de CTA: "Podemos conversar ainda esta semana para alinhar os próximos passos?"

7. **Encerramento:**
   - Finalize de forma profissional: "Atenciosamente, Júlio Costa."

---

**INSTRUÇÕES ADICIONAIS:**
- Use uma linguagem simples, clara e profissional. Evite gírias ou termos complexos.
- Mantenha um tom amigável, confiável e persuasivo.
- Cada parágrafo deve ter no máximo 2 frases, mantendo o texto conciso e fácil de ler.
- Personalize a carta ao máximo, mencionando detalhes específicos da demanda do cliente.
- Use técnicas de rapport, como "entendo", "compreendo" e "estou aqui para ajudar", para criar conexão emocional.
- Reforce sua experiência e habilidades de forma natural, sem soar arrogante.

---

**O CLIENTE TEM ESSAS PERGUNTAS:**
1. Descreva sua experiência em projetos similares.
2. Defina de quais informações você precisa para começar.
3. Explique porque você é o candidato ideal.

Respndas as perguntas depois de ter gerado a carta. E cada resposta deve ter no máximo 2 frasses. 

---

**EXEMPLO DE CARTA GERADA:**

Olá, [nome do cliente]. Como vai?

Espero que esteja bem!

Meu nome é Júlio Costa, sou Copywriter Profissional com mais de 5 anos de experiência em criação de textos que aumentam vendas, engajam audiências e melhoram o posicionamento nos motores de busca.

Li atentamente sua demanda sobre [breve descrição da demanda] e fiquei entusiasmado com a oportunidade de ajudar. Entendo que [mencionar um ponto específico da demanda] é crucial para o sucesso do seu projeto, e estou confiante de que posso contribuir com soluções que atendam às suas expectativas.

Ao contratar meus serviços, você pode esperar:
--> Aumento de conversões em até 30% com textos otimizados para vendas.
--> Melhoria no ranqueamento do seu site nos motores de busca, atraindo mais tráfego orgânico.
--> Conteúdo personalizado que ressoa com seu público-alvo, aumentando o engajamento e a fidelização.

Meu portfólio está sendo enviado em anexo, onde você poderá ver exemplos de projetos anteriores e os resultados alcançados.

Estou disponível para uma conversa rápida e sem compromisso nesta terça ou quarta-feira. Podemos discutir como posso ajudar a alcançar os resultados que você deseja. O que acha?

Atenciosamente,
Júlio Costa

    """

def extrair_dados_workana(url):
    """Extrai o nome e a demanda do cliente da página do Workana."""
    # Configura o driver do Chromium
    service = Service("/usr/bin/chromedriver")  # Atualize o caminho do chromedriver se necessário
    options = Options()
    options.add_argument("--headless")  # Executa em modo headless (sem interface gráfica)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)

        # Espera até que o nome do cliente esteja presente
        nome_cliente = WebDriverWait(driver, 20).until(
           # EC.presence_of_element_located((By.CSS_SELECTOR, "a.h4.user-name span"))
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.wk-user-info a.h4.user-name span"))
        ).text

        # Verifica o texto capturado
        print(f"")
        print(f"Texto capturado do nome do cliente: {nome_cliente}")

        # Espera até que a descrição da demanda esteja presente
        demanda_cliente = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.expander.js-expander-passed"))
        ).text

        return nome_cliente, demanda_cliente
    except Exception as e:
        print(f"Erro ao extrair dados do Workana: {e}")
        return None, None
    finally:
        driver.quit()

def main():
    # Verifica se o endereço da demanda foi fornecido como argumento
    if len(sys.argv) != 2:
        print("Uso: CARTA.py <endereço_da_demanda>")
        return

    # URL da página do Workana
    url_workana = sys.argv[1]

    # Extrai o nome e a demanda do cliente
    nome, demanda = extrair_dados_workana(url_workana)

    if not nome or not demanda:
        print("Erro: Não foi possível extrair os dados do Workana.")
        return

    # Carrega a sessão salva
    carregar_sessao(MODELO)

    # Gera o prompt para a IA
    prompt = gerar_prompt(nome, demanda)

    # Envia o prompt para a IA do Ollama
    carta_gerada = gerar_texto_com_ollama(prompt, max_tokens=1000)

    if carta_gerada:
        print("Carta gerada pela IA:")
        print(f"")
        print(f"")
        print(f"")
        print(demanda)
        print(f"")
        print(f"")
        print(f"")
        print(carta_gerada)
        # Salva a sessão após gerar a carta
        #salvar_sessao("CA")
    else:
        print("Falha ao gerar a carta.")

if __name__ == "__main__":
    main()
