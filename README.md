# README.md - Desafio Qipu

## Instruções para Execução dos Exercícios

### 1. Clonar o Repositório

```bash
git clone git@github.com:alsox42/desafio-qipu.git
```

### Exercício 1

```bash
cd desafio-qipu/exercicio_1
python lista_ligada.py
```

**Observação**: O resultado final deverá ser o valor 100% exibido no console.

### Exercício 2

```bash
cd desafio-qipu/exercicio_2
sudo docker build -t scraping_aiesweb .
sudo docker run -it scraping_aiesweb /bin/sh
ls
python scraping_aiesweb.py
```

**Instruções**:

1. Informe o código ICAO e pressione [ENTER].
   a) As informações solicitadas no requisito da questão são exibidas no console.
   b) São gerados os arquivos PDFs referentes ao total de cartas disponíveis para cada código ICAO.