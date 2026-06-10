# Disaster Vision Monitor

## Integrantes

- Nome Completo — RM XXXXXXX
- Nome Completo — RM XXXXXXX
- Nome Completo — RM XXXXXXX

---

## Descrição do Projeto

O Disaster Vision Monitor é uma aplicação desenvolvida em Python utilizando OpenCV para monitoramento visual em tempo real.

A solução utiliza a câmera do computador para detectar movimentações no ambiente e classificar automaticamente o nível de risco com base na intensidade dos movimentos identificados.

O objetivo é demonstrar conceitos de Visão Computacional aplicados à detecção de atividade e monitoramento inteligente.

---

## Objetivo

Desenvolver um sistema capaz de:

- Capturar imagens da webcam em tempo real.
- Detectar movimentações entre quadros consecutivos.
- Medir a intensidade dos movimentos.
- Classificar automaticamente o risco em:
  - LOW
  - MEDIUM
  - CRITICAL
- Exibir os resultados instantaneamente ao usuário.

---

## Tecnologias Utilizadas

### Linguagem

- Python 3

### Bibliotecas

- OpenCV (cv2)
- Time

---

## Funcionamento

O sistema realiza as seguintes etapas:

1. Captura imagens da webcam.
2. Compara quadros consecutivos.
3. Detecta diferenças entre as imagens.
4. Calcula a intensidade do movimento.
5. Atualiza uma média de movimentação.
6. Classifica o nível de risco.
7. Exibe os resultados em tempo real.

---

## Classificação de Risco

### LOW

Baixa movimentação detectada.

### MEDIUM

Movimentação moderada detectada.

### CRITICAL

Movimentação intensa detectada.

---

## Fluxo da Solução

```text
Webcam
   │
   ▼
Captura de Frames
   │
   ▼
Comparação de Imagens
   │
   ▼
Detecção de Movimento
   │
   ▼
Cálculo de Intensidade
   │
   ▼
Classificação de Risco
   │
   ▼
Exibição em Tempo Real
```

---

## Estrutura do Projeto

```text
DisasterVisionMonitor
│
├── main.py
└── README.md
```

---

## Instalação

### Instalar Dependências

```bash
pip install opencv-python
```

### Executar o Projeto

```bash
python main.py
```

---

## Demonstração em Vídeo

Link do vídeo de demonstração:

```text
https://youtu.be/yUWgJQcLCeg
```

---

## Resultados Obtidos

Durante os testes, o sistema conseguiu detectar movimentações em tempo real e classificar automaticamente diferentes níveis de risco com base na intensidade observada.

A solução demonstra de forma prática a aplicação de Visão Computacional para monitoramento inteligente de ambientes.

---

## Conclusão

O projeto demonstra como técnicas simples de processamento de imagens podem ser utilizadas para criar sistemas de monitoramento capazes de detectar atividade e gerar classificações automáticas de risco em tempo real.