import openpyxl as op 
import datetime as dt
import construtor

data_atual = dt.datetime.today().date()
salario = construtor.victtor.salario
conta_atual_mom = construtor.victtor.conta_mae()
conta_atual_cartao1 = construtor.victtor.atual_cartao1
conta_atual_cartao2 = construtor.victtor.atual_cartao2


quest1 = (float(input('Quanto você gastou no cartao mom?: ')))
valor_mom = (conta_atual_mom+quest1)
quest2 = (float(input('Quanto você gastou no roxin?: ')))
valor_cartao1 = (conta_atual_cartao1 + quest2)
valor_cartao2 = conta_atual_cartao2
faculdade = construtor.victtor.faculdade



book = op.Workbook()

book.create_sheet('Financeiro') #Criar páginas

page_financeiro= book['Financeiro'];
page_financeiro.append(['Mês','Rendimento','Cartão 1','Cartão 2','Cartão 3', 'Faculdade']);
page_financeiro.append([data_atual,salario,valor_mom,valor_cartao1,valor_cartao2, faculdade]);


book.save('Planilha Financeira.xlsx')

