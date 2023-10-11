# README.md - Desafio Qipu

## Instruções para Execução dos Exercícios

### 1. Clonar o Repositório

```bash
git clone git@github.com:alsox42/desafio-qipu.git
```

### Exercício 1

```bash
cd desafio-qipu/exercicio_1
python -m venv venv
. venv/bin/activate
python lista_ligada.py
```

**Observação**: O resultado final deverá ser o valor 100% exibido no console.
                Como não há dependencia de importação para essa tarefa, a  criação do ambiente virtual é apenas para cumprir o requisito da tarefa. 
            

### Exercício 2

```bash
cd desafio-qipu/exercicio_2
sudo docker build -t scraping_aiesweb .
sudo docker run -it scraping_aiesweb /bin/sh
ls
python scraping_aiesweb.py
```


**Instruções**:

Informe o código ICAO e pressione [ENTER].
a) As informações solicitadas no requisito da questão são exibidas no console.
b) São gerados os arquivos PDFs referentes ao total de cartas disponíveis para cada código ICAO.

### Observação final: 
Você pode optar por não executar o exercicio 2 via container, nesse caso é necessario criar a virtualenv e executar o arquivo requirements.txt. Nesse caso dependendo da configuração do seu S.O. O script python ira exibir o resultado das linhas 49, 50 e 51, o mapa das cartas será exibido na tela do console. 