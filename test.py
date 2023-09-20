import unittest
import doctest
import locale

from funcoes import calcula_dif, retorna_arquivo

locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

class TestCalculoFuncoes(unittest.TestCase):
    # Não funciona sem return
    def test_calculo_digita(self):
        resultado = calcula_dif("20 de Agosto de 2023 - 18 de Setembro de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  28")

        resultado = calcula_dif("18 de Setembro de 2023 - 23 de Agosto de 2023")
        self.assertEqual(resultado, "O número de dias entre essas datas é:  25")


    # Funciona corretamente
    def test_calculo_arquivo(self):
        with open("test1.txt", "w") as f:
            f.write("26 de outubro de 2023 - 27 de agosto de 2025\n")
        resultado = calculadif("input.txt")
        self.assertEqual(resultado, 671)


if __name__ == "__main__":
    unittest.main()

