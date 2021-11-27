# Hybrid Machine Translation

## Explaining the Program

Performance of Neural Machine Translation (NMT) systems on low resource languages is not as good as the performance of language pairs with sufficient amounts of data. For some low resource language pairs, performance of Statistical Machine Translation (SMT) systems are comparable or better than NMT. In this project, we attempt to combine best of SMT and NMT to create a Hybrid Machine Translation system which is able to perform better than SMT and NMT on loe resource languages.

## Approach

We use the phrase tables generated using SMT. While generating translations in NMT, there are some unknown tokens generated, which reduce the performance of the model. We use the attention scores to find the most relevant source word for the generated target word. If the generated target word is an unknown token, then we replace it with the translation of the most relevant source word. The translation of the source word can be looked up in the phrase table.

Since, the phrase tables are very huge, the lookup operation becomes computationally expensive. We prune the phrase tables efficiently to make the proposed approach computationally efficient. 

## Results

We used Hindi-English language pairs for all our experiments. We considered a Bi-LSTM with attention mechanism as our baseline model. We compared the performance of our proposed Hybrird Machine Translation method with the baseline and observed that the proposed method outperforms the baseline by 1 - 1.3 BLEU points.

## Future Work

The proposed approach works during inference. In future, we focus on incorporating the phrase table while training the translation model. 
