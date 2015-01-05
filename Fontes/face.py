__author__ = 'Jeferson de Souza'

from calculos import *
#import random

HNO3 = 58.3
CACO3 = 99.9
NO3 = 65.8

# Fator de corre????????????????o
SODA = 1.0751
EDTA = 0.8
HCL = 0.9756

# Volumes dos tanques
Acido = 2900
Coagulante = 3900
Composto = 0
Talco = 2000
file_name = 'Calculos.txt'


def calculo_solucao(parametro_up=1, parametro_dow=1):

    placa1_a = sort_num(66.001, 101.992)
    placa1_b = sort_num(66.001, 101.992)

    amostra_a = sort_num(1.500, 1.999)
    amostra_b = sort_num(1.500, 1.999)

    resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
    resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

    placa3a = find_c(resultado_a, amostra_a, placa1_a)
    placa3b = find_c(resultado_b, amostra_b, placa1_b)

    media = (resultado_a + resultado_b) / 2

    resultado_texto = '''
    %.3f    %.3f
    %.3f     %.3f
    %.3f    %.3f
    %.1f       %.1f
        (%.1f)
    -------------
    ''' % (placa1_a, placa1_b, amostra_a, amostra_b, placa3a, placa3b, resultado_a, resultado_b, media)
    return resultado_texto

def calc_nitrato(parametro_no3_down=1, parametro_no3_up=1):

    resultado_no3 = sort_num(parametro_no3_down, parametro_no3_up)  # trocar pelo parametro
    volume_edta = resultado_no3 / EDTA

    restulado_texto = '''
    %.1f
    %.1f
    ---
    ''' % (volume_edta, resultado_no3)
    return restulado_texto

def calculo_acido(parametro_up=1, parametro_down=1):

        peso = sort_num(3501, 3999)
        volume = reverse_ac(sort_num(parametro_down, parametro_up), sort_num(3500, 4100), SODA)
        resultado_texto = '''
        %d
        %.1f
        %.1f
        ---
        ''' % (peso, volume, analise_ac(volume, peso, SODA))
        return resultado_texto



def calculo_carbonato(parametro_up=1, parametro_dow=1):

    placa1_a = sort_num(0.799, 1.990)
    placa1_b = sort_num(0.799, 1.990)

    amostra_a = sort_num(11.500, 11.999)
    amostra_b = sort_num(11.500, 11.999)

    resultado_a = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro
    resultado_b = sort_num(parametro_dow, parametro_up)  # trocar pelo parametro

    placa3a = find_c(resultado_a, amostra_a, placa1_a)
    placa3b = find_c(resultado_b, amostra_b, placa1_b)

    media = (resultado_a + resultado_b) / 2
    texto_result ='''
    %.3f     %.3f
    %.3f   %.3f
    %.3f     %.3f
    %.1f       %.1f
         %.2f
    --------------
    ''' % (placa1_a, placa1_b, amostra_a, amostra_b, placa3a, placa3b, resultado_a, resultado_b, media)

    return texto_result


#print(calculo_acido(1.5, 2.0))