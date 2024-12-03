from unittest.mock import patch

def test_invalid_json_format(client):
    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           data="invalid data", content_type='text/plain')
    assert response.status_code == 400
    assert "A requisição não possui um JSON" in response.json['error']


def test_empty_json(client):
    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json={}, content_type='application/json')
    assert response.status_code == 400
    assert "A requisição não possui dados no JSON" in response.json['error']


def test_invalid_schema(client):
    invalid_data = [
        {
            "id_transacao": "string_invalida",
            "amt": "valor_invalido"
        }
    ]
    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=invalid_data, content_type='application/json')
    assert response.status_code == 400
    assert "error" in response.json


def test_valid_json_data(client):
    valid_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]
    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=valid_data, content_type='application/json')
    assert response.status_code == 200


def test_missing_id_transacao_field(client):
    input_data = [
        {
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_amt_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_entertainment_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_gas_transport_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_grocery_pos_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_home_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_kids_pets_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_misc_net_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_shopping_net_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_shopping_pos_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_category_travel_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_1_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_2_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_3_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_4_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_5_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_6_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_7_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_8_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_9_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_10_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_11_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_month_12_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_period_madrugada_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_period_manha_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Noite": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_period_noite_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Tarde": 0
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_missing_transaction_period_tarde_field(client):
    input_data = [
        {
            "id_transacao": 456,
            "amt": 3.933589,
            "category_entertainment": 0,
            "category_gas_transport": 0,
            "category_grocery_pos": 0,
            "category_home": 0,
            "category_kids_pets": 0,
            "category_misc_net": 0,
            "category_shopping_net": 0,
            "category_shopping_pos": 0,
            "category_travel": 0,
            "transaction_month_1": 1,
            "transaction_month_2": 0,
            "transaction_month_3": 0,
            "transaction_month_4": 0,
            "transaction_month_5": 0,
            "transaction_month_6": 0,
            "transaction_month_7": 0,
            "transaction_month_8": 0,
            "transaction_month_9": 0,
            "transaction_month_10": 0,
            "transaction_month_11": 0,
            "transaction_month_12": 0,
            "transaction_period_Madrugada": 1,
            "transaction_period_Manhã": 0,
            "transaction_period_Noite": 0,
        }
    ]

    response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                           json=input_data, content_type='application/json')

    assert response.status_code == 400


def test_internal_error(client):
    with patch('api.v1.routes.montar_dataframe') as mock_montar_dataframe:
        mock_montar_dataframe.side_effect = ValueError(
            "Erro ao montar o DataFrame")
        valid_data = [
            {
                "id_transacao": 456,
                "amt": 3.933589,
                "category_entertainment": 0,
                "category_gas_transport": 0,
                "category_grocery_pos": 0,
                "category_home": 0,
                "category_kids_pets": 0,
                "category_misc_net": 0,
                "category_shopping_net": 0,
                "category_shopping_pos": 0,
                "category_travel": 0,
                "transaction_month_1": 1,
                "transaction_month_2": 0,
                "transaction_month_3": 0,
                "transaction_month_4": 0,
                "transaction_month_5": 0,
                "transaction_month_6": 0,
                "transaction_month_7": 0,
                "transaction_month_8": 0,
                "transaction_month_9": 0,
                "transaction_month_10": 0,
                "transaction_month_11": 0,
                "transaction_month_12": 0,
                "transaction_period_Madrugada": 1,
                "transaction_period_Manhã": 0,
                "transaction_period_Noite": 0,
                "transaction_period_Tarde": 0
            }
        ]

        response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                               json=valid_data, content_type='application/json')

        assert response.status_code == 500
        assert "Erro ao montar o DataFrame" in response.json['error']



def test_internal_error_predicao(client):
    # Mock da função `deteccao_transacao_fraudulenta`
    with patch('api.v1.routes.deteccao_transacao_fraudulenta') as mock_deteccao_transacao_fraudulenta:
        # Simula um erro ao chamar a função
        mock_deteccao_transacao_fraudulenta.side_effect = ValueError("Erro ao realizar predição")

        # Dados de entrada válidos
        valid_data = [
            {
                "id_transacao": 456,
                "amt": 3.933589,
                "category_entertainment": 0,
                "category_gas_transport": 0,
                "category_grocery_pos": 0,
                "category_home": 0,
                "category_kids_pets": 0,
                "category_misc_net": 0,
                "category_shopping_net": 0,
                "category_shopping_pos": 0,
                "category_travel": 0,
                "transaction_month_1": 1,
                "transaction_month_2": 0,
                "transaction_month_3": 0,
                "transaction_month_4": 0,
                "transaction_month_5": 0,
                "transaction_month_6": 0,
                "transaction_month_7": 0,
                "transaction_month_8": 0,
                "transaction_month_9": 0,
                "transaction_month_10": 0,
                "transaction_month_11": 0,
                "transaction_month_12": 0,
                "transaction_period_Madrugada": 1,
                "transaction_period_Manhã": 0,
                "transaction_period_Noite": 0,
                "transaction_period_Tarde": 0
            }
        ]

        # Envia a requisição POST
        response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                               json=valid_data, content_type='application/json')

        # Verifica se o código de status é 500 (erro interno)
        assert response.status_code == 500
        # Confirma se a mensagem de erro é retornada na resposta
        assert "Erro ao realizar predição" in response.json['error']


def test_internal_error_objeto(client):
    # Mock da função `deteccao_transacao_fraudulenta`
    with patch('api.v1.routes.objeto_saida_transacao') as mock_dobjeto_saida_transacao:
        # Simula um erro ao chamar a função
        mock_dobjeto_saida_transacao.side_effect = ValueError("Erro ao realizar objeto")

        # Dados de entrada válidos
        valid_data = [
            {
                "id_transacao": 456,
                "amt": 3.933589,
                "category_entertainment": 0,
                "category_gas_transport": 0,
                "category_grocery_pos": 0,
                "category_home": 0,
                "category_kids_pets": 0,
                "category_misc_net": 0,
                "category_shopping_net": 0,
                "category_shopping_pos": 0,
                "category_travel": 0,
                "transaction_month_1": 1,
                "transaction_month_2": 0,
                "transaction_month_3": 0,
                "transaction_month_4": 0,
                "transaction_month_5": 0,
                "transaction_month_6": 0,
                "transaction_month_7": 0,
                "transaction_month_8": 0,
                "transaction_month_9": 0,
                "transaction_month_10": 0,
                "transaction_month_11": 0,
                "transaction_month_12": 0,
                "transaction_period_Madrugada": 1,
                "transaction_period_Manhã": 0,
                "transaction_period_Noite": 0,
                "transaction_period_Tarde": 0
            }
        ]

        # Envia a requisição POST
        response = client.post('/v1/inteligencia-artificial/deteccao-fraude',
                               json=valid_data, content_type='application/json')

        # Verifica se o código de status é 500 (erro interno)
        assert response.status_code == 500
        # Confirma se a mensagem de erro é retornada na resposta
        assert "Erro ao realizar objeto" in response.json['error']
