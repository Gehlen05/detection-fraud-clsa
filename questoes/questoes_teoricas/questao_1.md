** Este são os campos que eu quero selecionar e de qual tabela eu quero que ele venha.
SELECT
co.order_id,
co.customer_name,
co.customer_id,
ad.address,
ad.state,
ad.country,
ad.zip_code
*---------------------------------------------------*
O from é a tabela selecionada, nesse caso, o customer_orders chamda/abreviada para co para simplificar o nome para facilitar a expressão de consulta.
essa tabela ela foi realizada a junção com a tabela address_details chamda/abreviada ad(é possível ver nos campos as cuas abreviações). 
O join retornará os registros que são comuns às duas tabelas, utilizando a comparação ON que só vai trazer quando os campos order_id das duas tabelas forem iguais.
ON que 

FROM customer_orders co
JOIN address_details ad ON co.order_id = ad.order_id

Where trás a condição que só retornará os campos iguais que tenham address maior/igual a 5 e não contenha nesse mesmo campo -, ou esteja vazio, ou preenchido com SOME ADDRESS
WHERE LENGTH(ad.address) >= 5 AND ad.address NOT IN ('-', '', 'SOME ADDRESS')


Por últmo ele ordena de forma crescente pelo campo order_id.
ORDER BY co.order_id;

