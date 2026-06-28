# AVA_3_Julio-Ricardo-Jemio_Uso-do-Vision-Transformer-ViT-para-Classifica-o-de-Imagens
# Classificação de Imagens com Vision Transformer (ViT) 🤖👁️

Este repositório contém o código e o relatório técnico da **Prática 3** da disciplina de **Sistemas Evolutivos e Aplicados à Robótica**. O objetivo principal do projeto foi avaliar o desempenho da arquitetura *Vision Transformer* (ViT) na classificação automática de imagens, realizando um estudo comparativo entre os modelos **ViT Base** e **ViT Large**.

## 📌 Visão Geral do Projeto

Diferente das Redes Neurais Convolucionais (CNNs) tradicionais, o **Vision Transformer (ViT)** divide as imagens em pequenos blocos (*patches*) e utiliza mecanismos de auto-atenção para entender o contexto global da imagem. 

Neste experimento, testamos ambos os modelos em um banco de 6 imagens de diferentes espécies animais para analisar dois fatores críticos para a robótica: **Nível de Confiança** e **Tempo de Inferência (Latência)**.

## 📊 Resumo dos Resultados

| Imagem | Classe Real | Vencedor em Velocidade | Vencedor em Confiança |
| :---: | :--- | :---: | :---: |
| 1 | Urso (*Sloth Bear*) | ⚡ ViT Base | 🎯 ViT Large *(Base errou)* |
| 2 | Serpente (*King Snake*) | ⚡ ViT Base | 🎯 ViT Base *(Large oscilou)* |
| 3 | Arara (*Macaw*) | ⚡ ViT Base | 🤝 Empate Técnico |
| 4 | Dugongo (*Dugong*) | ⚡ ViT Base | 🎯 ViT Base |
| 5 | Vombate (*Wombat*) | ⚡ ViT Base | 🎯 ViT Base |
| 6 | Escorpião (*Scorpion*) | ⚡ ViT Base | 🎯 ViT Large |

## 💡 Principais Conclusões

* **Eficiência Temporal:** O **ViT Base** foi o vencedor absoluto em velocidade, sendo entre **2,4x e 5,1x mais rápido** que o ViT Large. Isso o torna a escolha ideal para sistemas embarcados em robótica que exigem decisões em tempo real.
* **Robustez vs. Ambiguidade:** O **ViT Large** justificou sua maior complexidade em cenários difíceis (como na Imagem 1), onde o modelo Base falhou. O Large mostrou-se mais indicado para tarefas de inspeção crítica onde o erro não é tolerável e o processamento pode ser feito em nuvem.
* **O Paradoxo da Confiança:** Contra o senso comum, o modelo menor (Base) entregou maior certeza em suas predições na maioria das imagens claras e bem definidas.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **PyTorch** (Processamento dos tensores)
* **Hugging Face Transformers** (Modelos ViT pré-treinados)
* **Pillow (PIL) & Requests** (Manipulação de imagens via URL)
