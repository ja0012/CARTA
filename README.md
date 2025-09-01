# CARTA4 – Gerador Automático de Cartas de Apresentação para Workana

O CARTA4 é um script em Python que automatiza a criação de cartas de apresentação personalizadas para propostas no **Workana**.  
Ele extrai automaticamente os dados de um projeto (nome do cliente e descrição da demanda) e gera uma carta profissional usando **modelos de linguagem via Ollama**.


Funcionalidades

- **Web Scraping no Workana**  
  Extrai nome do cliente e a descrição do projeto com Selenium.

- **Prompt Personalizado**  
  Gera um prompt estruturado para criação de cartas persuasivas e profissionais.

- **Integração com Ollama**  
  Envia o prompt para um modelo de linguagem (`CA2`, `gemma3`, etc.) via API.

- **Gestão de Sessões**  
  Possibilidade de salvar e carregar sessões para manter consistência no estilo de escrita.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/)  
- [Requests](https://docs.python-requests.org/)  
- [Ollama](https://ollama.ai/) (para processamento de linguagem natural)  
- [ChromeDriver](https://chromedriver.chromium.org/)

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/ja0012/SEO_Analysis.git
   cd SEO_Analysis
