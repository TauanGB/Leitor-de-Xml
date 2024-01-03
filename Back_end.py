import xml.etree.ElementTree as ET
import os

def Formatacao(Valor_Numerico):## transformar em def unica, e ser utilizada somente no front
	Vlr_Formatado =	str(Valor_Numerico[0:2]+"."+
		Valor_Numerico[2:5]+"."+
		Valor_Numerico[5:8]+"/"+
		Valor_Numerico[8:12]+"-"+
		Valor_Numerico[12:14])
	
	return Vlr_Formatado

def Busca(XML_s=[],Diretorio = ''): # adicionar apos completo
	Parser = ET.XMLParser(encoding='UTF-8')
	Var_de_xmls = {}


	for xml in XML_s:
		print(xml)
		print(Diretorio+"/"+xml)
		Root = ET.parse(Diretorio+"/"+xml).getroot()
		nsCteProc = {"ns":"http://www.portalfiscal.inf.br/cte"}

		for numeros in Root:
			print(numeros.tag, numeros.attrib)
			
		Elemento = Root.find("./ns:CTe/ns:infCte/ns:ide/ns:nCT",nsCteProc).text

		Municip_inicial_Mn = Root.find("./ns:CTe/ns:infCte/ns:ide/ns:xMunIni",nsCteProc).text
		Municip_inicial_UF = Root.find("./ns:CTe/ns:infCte/ns:ide/ns:UFIni",nsCteProc).text
		
		Municip_Final_Mn = Root.find("./ns:CTe/ns:infCte/ns:ide/ns:xMunFim",nsCteProc).text
		Municip_Final_UF = Root.find("./ns:CTe/ns:infCte/ns:ide/ns:UFFim",nsCteProc).text

		Nome_Emitente = Root.find("./ns:CTe/ns:infCte/ns:emit/ns:xNome",nsCteProc).text
		CNPJ_Emitente = Root.find("./ns:CTe/ns:infCte/ns:emit/ns:CNPJ",nsCteProc).text

		Nome_Remetente = Root.find("./ns:CTe/ns:infCte/ns:rem/ns:xNome",nsCteProc).text
		CNPJ_Remetente = Root.find("./ns:CTe/ns:infCte/ns:rem/ns:CNPJ",nsCteProc).text
		CEP_Remetente = Root.find("./ns:CTe/ns:infCte/ns:rem/ns:enderReme/ns:CEP",nsCteProc).text

		Nome_Destinatario = Root.find("./ns:CTe/ns:infCte/ns:dest/ns:xNome",nsCteProc).text
		CNPJ_Destinatario = Root.find("./ns:CTe/ns:infCte/ns:dest/ns:CNPJ",nsCteProc).text
		CEP_Destinatario = Root.find("./ns:CTe/ns:infCte/ns:dest/ns:enderDest/ns:CEP",nsCteProc).text

		Valor_Pestação = Root.find("./ns:CTe/ns:infCte/ns:vPrest/ns:vTPrest",nsCteProc).text.replace('.',',')

		Valor_Carga = Root.find("./ns:CTe/ns:infCte/ns:infCTeNorm/ns:infCarga/ns:vCarga",nsCteProc).text.replace('.',',')
		Carga_descrição = Root.find("./ns:CTe/ns:infCte/ns:infCTeNorm/ns:infCarga/ns:proPred",nsCteProc).text
		Peso_Carga = Root.find("./ns:CTe/ns:infCte/ns:infCTeNorm/ns:infCarga/ns:infQ/ns:qCarga",nsCteProc).text.replace('.',',')

		Chave_NFe = Root.find("./ns:CTe/ns:infCte/ns:infCTeNorm/ns:infDoc/ns:infNFe/ns:chave",nsCteProc).text
		Chave_Cte = Root.find("./ns:CTe/ns:infCte",nsCteProc).attrib['Id'].replace("CTe","")

		Obs = Root.find("./ns:CTe/ns:infCte/ns:compl/ns:xObs",nsCteProc).text

		Var_de_xmls[xml] = {
			"Dados CT-e":{"Municip inicial Mn":Municip_inicial_Mn,
					"Municip inicial UF":Municip_inicial_UF,
					"Municip Final Mn":Municip_Final_Mn,
					"Municip Final UF":Municip_Final_UF},
			"Emitente":{"Nome Emitente":Nome_Emitente,
					"CNPJ Emitente":CNPJ_Emitente},

			"Remetente":{"Nome Remetente":Nome_Remetente,
					"CNPJ Remetente":CNPJ_Remetente,
					"CEP Remetente ":CEP_Remetente},

			"Destinatario":{"Nome Destinatario":Nome_Destinatario,
					"CNPJ Destinatario":CNPJ_Destinatario,
					"CEP Destinatario":CEP_Destinatario},

			"Serviçoes e impostos":{"Valor Pestação":Valor_Pestação},

			"Info Carga":{"Valor Carga":Valor_Carga,
					"Carga descrição":Carga_descrição,
					"Peso Carga":Peso_Carga},

			"Info Documentos":{"Chave NFe":Chave_NFe},

			"Doc. de Transporte. Ant":{"Chave Cte":Chave_Cte},

			"Observacao":{"Obs":Obs}
			}
	
	return Var_de_xmls