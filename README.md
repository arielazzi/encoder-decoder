# encoder-decoder

## Integrantes
Ariel Azzi, Mateus Weber, Mayara Damiani e Rayana Menezes

## Implementações

### Encoder
- Golomb
- Elias-Gamma
- Fibonacci
- Unária
- Delta

### Decoder
- Golomb
- Elias-Gamma
- Fibonacci
- Unária
- Delta

### Tratamento de Erro/Ruído
- Cálculo CRC-8
- Codewords Hamming
- Tratamento de Erro Hamming

## Limitações
- Demora para executar a codificação do tratamento de erro em arquivos muito grandes. (Gerar arquivo .ecc) 

## Como rodar o projeto?
- Instalar última versão do [Python](https://www.python.org/downloads/)
- Acessar a raiz do projeto em um terminal de sua preferência e rodar o seguinte comando para iniciar: `python main.py`.

## Como funciona?
Ao iniciar o projeto, o usuário deve escolher entre as opções do Menu principal. 
- A opção 1 irá gerar o primeiro arquivo .cod para determinado tipo de codificação.
- A opção 2 faz a decodificação do arquivo .cod, gerando outro arquivo decodificado.
- A opção 3 lida com o tratamento de ruídos, fazendo o cálculo do CRC e gerando os codewords Hamming. No fim é gerado o arquivo .ecc.
- A opção 4 faz a decodificação do arquivo .ecc, executando a decodificação do Hamming e a verificação do CRC para tratamento de erros. Os erros encontrados na decodificaçâo Hamming são salvos em log.txt. No fim é gerado o arquivo .cod final.
