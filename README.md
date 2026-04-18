# DIO-Estudo-Whisper-e-gTTS

## Descrição

Este projeto demonstra uma interação por voz com o ChatGPT utilizando:

- Whisper (speech-to-text)
- API da OpenAI (geração de texto)
- gTTS (text-to-speech)

O sistema recebe um arquivo de áudio, transcreve para texto, envia para o ChatGPT e retorna a resposta em formato de áudio.

---

## Funcionamento

1. Carrega um arquivo de áudio (`audio.wav`)
2. Transcreve o áudio utilizando o Whisper
3. Envia o texto transcrito para o ChatGPT
4. Recebe a resposta gerada
5. Converte a resposta em áudio com gTTS
6. Salva o resultado como `resposta.mp3`

---

## Tecnologias utilizadas

- Python
- OpenAI API
- Whisper (`whisper-1`)
- gTTS

---

## Estrutura do projeto

```text
DIO-Estudo-Whisper-e-gTTS/
├── app.py
├── audio.wav
├── resposta.mp3
├── requirements.txt
├── README.md
├── .env.example
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/Vin-A/DIO-Estudo-Whisper-e-gTTS.git
cd DIO-Estudo-Whisper-e-gTTS
```

Crie um ambiente virtual (opcional):

```bash
python -m venv .venv
```

Ative o ambiente:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env.example`:

```env
OPENAI_API_KEY=sua_chave_aqui
```

---

## Como usar

1. Coloque um arquivo de áudio chamado `audio.wav` na pasta do projeto com o audio da pergunta
2. Crie o arquivo `.env` com sua chave da OpenAI
3. Execute o script:

```bash
python app.py
```

4. O arquivo de saída será gerado como:

```text
resposta.mp3
```

---

## Exemplo de saída

- Texto transcrito exibido no terminal
- Resposta do modelo exibida no terminal
- Arquivo de áudio gerado (`resposta.mp3`)

---

## Aviso

Não exponha sua chave da API publicamente. Use o arquivo `.env`.
