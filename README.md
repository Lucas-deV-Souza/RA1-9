# Compilador Léxico RPN para ARMv7

Instituição: PUCPR - Pontifícia Universidade Católica do Paraná
Disciplina: Linguagens Formais e Compiladores
Professor: FRANK COELHO DE ALCANTARA
Aluno: Lucas de Souza Vieira
GitHub: Lucas-deV-Souza
Grupo: RA1 9

# Sobre o Projeto
Este projeto é um analisador léxico construído em Python que lê expressões matemáticas em Notação Polonesa Reversa (RPN) e as converte para a linguagem Assembly compatível com a arquitetura ARMv7 (placa DE1-SoC), para execução no emulador CPulator.

# Como Executar
O projeto não possui menus interativos, sendo executado diretamente via linha de comando.
1. Abra o terminal no diretório do projeto.
2. Execute o comando passando o arquivo de teste como argumento:
   `python analisador.py teste1.txt`
3. O programa irá gerar automaticamente um arquivo de saída com o mesmo nome e extensão `.asm` (ex: `teste1.asm`) e registrará os tokens em `tokens.txt`.

# Testes e Validação
Os arquivos de teste contêm todas as operações exigidas aninhadas, além do uso de memória (MEM) e recuperação de histórico (RES). Os resultados visuais podem ser conferidos nos LEDs vermelhos do emulador CPulator.
