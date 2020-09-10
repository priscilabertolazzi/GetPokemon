'''
Este script realiza requisições na API RestFULL do Pokémon sobre o pokémon Ditto, e verifica seu nome, número e tipo.

Dependências:
$ pip install requests
$ pip install jsonpath
'''

#importando os pacotes requests, jsonpath e json
import requests
import jsonpath
import json

class Teste_GetPokemon(): #criando uma classe de testes

    URL = "https://pokeapi.co/api/v2/pokemon/ditto" #criando a variável "URL" para guardar o endereço da PokéAPI passando o pokémon Ditto

    def test_valida_nome(self): #implementando um cenário de teste para validar o nome do pokémon
        self.response = requests.get(self.URL) #criando a variável "response" e baixando o conteúdo retornado ao executar o endereço da variável "URL"
        self.json_response = json.loads(self.response.text) #criando a variável "json_response" e lendo o conteúdo retornado da váriavel "response"
        self.nome = jsonpath.jsonpath(self.json_response, "name") #criando a váriavel "nome" e atribuindo à ela o elemento "name" do response do json
        assert self.nome[0] == "ditto", "O nome do pokémon não é ditto." #valida se a variável "nome" é igual à "ditto", se não for exibe a mensagem de que o nome do pokémon não é ditto

    def test_valida_numero(self): #implementando um cenário de teste para validar o número do pokémon
        self.response = requests.get(self.URL) #criando a variável "response" e baixando o conteúdo retornado ao executar o endereço da variável "URL"
        self.json_response = json.loads(self.response.text) #criando a variável "json_response" e lendo o conteúdo retornado da váriavel "response"
        self.numero = jsonpath.jsonpath(self.json_response, "id") #criando a váriavel "numero" e atribuindo à ela o elemento "id" do response do json
        assert self.numero[0] == 132, "O número do pokémon não é 132." #valida se a variável "numero" é igual à "132", se não for exibe a mensagem de que o número do pokémon não é 132

    def test_valida_tipo_nome(self): #implementando um cenário de teste para validar o tipo do pokémon
        self.response = requests.get(self.URL) #criando a variável "response" e baixando o conteúdo retornado ao executar o endereço da variável "URL"
        self.json_response = json.loads(self.response.text) #criando a variável "json_response" e lendo o conteúdo retornado da váriavel "response"
        self.tipo = self.json_response['types'][0]['type']['name'] #criando a váriavel "tipo" e atribuindo à ela o elemento "name" da propriedade "type" do primeiro objeto dentro da matriz da propriedade "types"
        assert self.tipo == 'normal', "O tipo do pokémon não é normal." #valida se a variável "tipo" é igual à "normal", se não for exibe a mensagem de que o tipo do pokémon não é normal

if __name__ == "__main__": #condição do python para executar diretamente esse script
    teste = Teste_GetPokemon() #instaciando a classe "Teste_GetPokemon()"
    teste.test_valida_nome() #chamando o método que valida o nome do pokémon da classe "Test_GetPokemon"
    teste.test_valida_numero() #chamando o método que valida o numero do pokémon da classe "Test_GetPokemon"
    teste.test_valida_tipo_nome() #chamando o método que valida o tipo do pokémon da classe "Test_GetPokemon"

    print("O pokémon Ditto foi validado com sucesso.")
