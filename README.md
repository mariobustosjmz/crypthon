# crypthon
Ejercicio de Criptografia usando el Cifrado Cesar con python

###Screens
![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-09-07.png)


![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-09-27.png)
![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-09-39.png)
![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-09-47.png)


![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-09-58.png)
![alt tag](https://github.com/mariobustosjmz/crypthon/blob/master/screen/Screenshot%20from%202017-02-22%2023-10-08.png)


	
	
	
	
	




> Devuelve una lista con mayusculas, minuscula, numeros y un espacio

```python
    def get_alfabeto():
      alfabeto = []

      # mayusculas:65-90 =25
      for i in range(65,91):
          alfabeto.append(chr(i))

      # minusculas:97-122 =25
      for i in range(97,123):
          alfabeto.append(chr(i))

      # numeros =10
      for i in range(10):
          alfabeto.append(str(i))

      # espacio
      alfabeto.append(" ")

      #print len(alfabeto) = 63 elementos
      return alfabeto
   
