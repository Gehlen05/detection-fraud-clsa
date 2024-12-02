# Questão 1
* Este são os campos que a query quer selecionar e de qual tabela as informações serão retiradas.
```
SELECT
co.order_id,
co.customer_name,
co.customer_id,
ad.address,
ad.state,
ad.country,
ad.zip_code
```

O from é a tabela selecionada, nesse caso, o customer_orders chamada/abreviada para co para simplificar o nome para facilitar a expressão de consulta.\
Foi realizada a junção da tabela customer_orders com a tabela address_details chamada/abreviada ad(é possível ver nos campos as suas abreviações). \
O join retornará os registros que são comuns às duas tabelas, utilizando a comparação ON que só vai trazer quando os campos **order_id** das duas tabelas forem iguais.

```
FROM customer_orders co
JOIN address_details ad ON co.order_id = ad.order_id
```
Where trás a condição que só retornará os campos iguais que tenham address maior/igual a 5 caracteres e não contenha nesse mesmo campo -, ou esteja vazio, ou preenchido com SOME ADDRESS
```
WHERE LENGTH(ad.address) >= 5 AND ad.address NOT IN ('-', '', 'SOME ADDRESS')
```

Por últmo à ordenação de forma crescente pelo campo order_id.
```
ORDER BY co.order_id;
```
**A IMPLEMENTAÇÃO EM PYTHON ESTÁ NO ARQUIVO questao_1_SQL2PANDAS.ipynb E questao_1_SQL2PANDAS.PDF**

# Questão 2
Como são 10 pacotes em 20 mil pedidos, parte-se de que não é um problema generalizado e sim algo pontual. 
Inicialmente pediria esses pacotes para investigá-los, executar de forma manual para poder analisá-los melhor.
Também pediria os logs referentes a eles, para ver se tem algum padrão, de horário, de onde vem qual a variação e de infraestrutura para ver se é algum momento em que o
sistema possa estar sobrecaregado. 
Acho que esses seriam meus passos iniciais para investigar e trazer algo para resolução.

