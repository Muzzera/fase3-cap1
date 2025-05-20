# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Construindo uma máquina agrícola

## AgroDev

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/issamahmod/">Mahmod Ahmad Issa</a>
- <a href="https://www.linkedin.com/in/gustavo-zanette-martins">Gustavo Zanetti Martins</a>


## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leoruiz197</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godoy</a>


## 📜 Descrição

*Este documento descreve detalhadamente o circuito desenvolvido utilizando a plataforma Wokwi, para simular um sistema inteligente de irrigação agrícola controlado por um microcontrolador ESP32.*


![Diagrama da Solução](./assets/wokwi.png)

# 🌱 Sistema de Irrigação Inteligente com ESP32

Este projeto simula um sistema de irrigação inteligente utilizando o microcontrolador ESP32 e sensores representados por componentes disponíveis na plataforma Wokwi.

---

## 🔧 Componentes Utilizados

| Componente      | Simulação                       | Pino ESP32 |
|-----------------|----------------------------------|------------|
| Botão           | Sensor de Fósforo (booleano)     | GPIO 13    |
| Botão           | Sensor de Potássio (booleano)    | GPIO 12    |
| LDR             | Sensor de pH (valor analógico)   | GPIO 34    |
| DHT22           | Sensor de Umidade do Solo        | GPIO 27    |
| Módulo Relé     | Controle da Bomba d'Água         | GPIO 14    |
| LED             | Indicador visual (via relé)      | Saída do Relé |

---

## 🔌 Ligações

- **Botões**: Um terminal no pino GPIO (13 ou 12) e outro no GND.
- **LDR**: Um terminal no 3.3V e outro no GPIO 34 com resistor de 10kΩ ao GND (divisor de tensão).
- **DHT22**: VCC no 3.3V, GND no GND, e DATA no GPIO 27.
- **Relé**: IN no GPIO 14, VCC no 3.3V, GND no GND. A saída do relé aciona o LED.

---

## ⚙️ Lógica de Controle

A bomba de irrigação é ativada (`RELAY_PIN = HIGH`) se **qualquer** das seguintes condições for verdadeira:

- Umidade do solo abaixo de 40%;
- Fósforo ausente (botão F solto);
- Potássio ausente (botão K solto);
- pH fora da faixa ideal (menor que 5.5 ou maior que 7.5).

Caso contrário, a bomba permanece desligada (`RELAY_PIN = LOW`).

---

## 💻 Plataforma de Simulação

Este projeto pode ser testado no [Wokwi](https://wokwi.com), utilizando o modo de simulação ESP32. Basta copiar o código `main.ino` e montar o circuito conforme o esquema acima.

---

## 📄 Exemplo de Saída no Monitor Serial

```
P: Sim | K: Não | pH: 6.8 | Umidade: 35.5%
Bomba: Ligada
```

---

Desenvolvido para fins educacionais — Projeto FarmTech Solutions 🌾

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


