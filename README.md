<body>
  <h1>Documentação do Código: Calculadora</h1>
  <p>
    Este código em Python implementa uma calculadora simples que permite ao usuário realizar operações básicas de adição, subtração, multiplicação e divisão com números reais.
  </p>

  <h2>Entrada</h2>
  <p>
    O código utiliza a função <code>input()</code> para solicitar ao usuário que forneça o primeiro número, o segundo número e o operador desejado.
  </p>

  <h2>Processamento</h2>
  <p>
    O código utiliza um laço <code>while</code> para continuar a execução até que o usuário decida sair da calculadora.
  </p>
  <p>
    Dentro do laço, o código realiza as seguintes etapas:
  </p>
  <ol>
    <li>
      <code>numero_1 = float(input('Digite o primeiro número: '))</code>: Solicita ao usuário que digite o primeiro número e converte a entrada para o tipo <code>float</code>.
    </li>
    <li>
      <code>numero_2 = float(input('Digite o segundo número: '))</code>: Solicita ao usuário que digite o segundo número e converte a entrada para o tipo <code>float</code>.
    </li>
    <li>
      <code>operador = input('Digite o operador (+, -, * ou /): ')</code>: Solicita ao usuário que digite o operador desejado. A entrada é armazenada na variável <code>operador</code>.
    </li>
    <li>
      <code>if operador not in operadores:</code>: Verifica se o operador fornecido pelo usuário está na lista de operadores válidos. Caso não esteja, exibe uma mensagem de erro e continua para a próxima iteração do laço utilizando a instrução <code>continue</code>.
    </li>
    <li>
      O próximo bloco de código seleciona a operação a ser realizada com base no operador fornecido:
      <ul>
        <li><code>if operador == '+': resultado = numero_1 + numero_2</code>: Realiza a adição dos dois números e armazena o resultado na variável <code>resultado</code>.</li>
        <li><code>elif operador == '-': resultado = numero_1 - numero_2</code>: Realiza a subtração dos dois números e armazena o resultado na variável <code>resultado</code>.</li>
        <li><code>elif operador == '*': resultado = numero_1 * numero_2</code>: Realiza a multiplicação dos dois números e armazena o resultado na variável <code>resultado</code>.</li>
        <li><code>elif operador == '/':</code>: Verifica se o operador é uma divisão.
          <ul>
            <li><code>if numero_2 == 0:</code>: Verifica se o segundo número é zero.</li>
            <li><code>print(f'Não é possível dividir por {numero_2}')</code>: Exibe uma mensagem de erro informando que a divisão por zero não é possível.</li>
            <li><code>continue</code>: Continua para a próxima iteração do laço.</li>
          </ul>
          <li><code>resultado = numero_1 / numero_2</code>: Realiza a divisão dos dois números e armazena o resultado na variável <code>resultado</code>.</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <code>print(f'O resultado foi {resultado}')</code>: Exibe o resultado da operação realizada.
  </li>
  <li>
    <code>sair = input('Deseja continuar utilizando a calculadora? (S/N)? ')</code>: Solicita ao usuário que indique se deseja continuar utilizando a calculadora. A resposta é armazenada na variável <code>sair</code>.
  </li>
  <li>
    <code>if sair.lower() == 'n': break</code>: Verifica se a resposta do usuário indica que ele deseja sair da calculadora (resposta igual a 'n'). Se for o caso, o código encerra o laço utilizando a instrução <code>break</code>.
  </li>
</ol>

<h2>Saída</h2>
<p>
  O código exibe mensagens ao usuário para fornecer os resultados das operações e solicitar a continuidade da utilização da calculadora. As mensagens são formatadas com os valores dos números e o resultado da operação, utilizando a função <code>print()</code>.
</p>

</body>
</html>
