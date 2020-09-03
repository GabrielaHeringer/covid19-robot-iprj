import re
from django.db.models import Q

class FiltroBuscaGlobal():
	pattern = r"\"([^\"]*)\""
	def __init__(self, string, queryset): #Construtor da classe.
                self.string = string
                self.palavras_especificas = re.findall(self.pattern, string)
                self.queryset = queryset
      
	def filtrar(self):
                if len(self.palavras_especificas) != 0:
                        for el in self.palavras_especificas:
                                self.string = self.string.replace(el, '')
                                self.queryset = self.queryset.filter(Q(resumo__icontains=el) |
                                 Q(titulo__icontains=el) |
                                 Q(idioma__icontains=el) |
                                 Q(autores__icontains=el) |
                                 Q(categoria__icontains=el) |
                                 Q(dataPrimeiroAcesso__icontains=el) |
                                 Q(data_publicacao__icontains=el) |
                                 Q(portal__icontains=el) |
                                 Q(subject__icontains=el) |
                                 Q(link_externo__icontains=el))

                self.string = self.string.replace('"', '')
                self.string = self.string.split()

                if self.string:
                        for el in self.string:
                                self.queryset = self.queryset.filter(Q(resumo__icontains=el) |
                                 Q(titulo__icontains=el) |
                                 Q(idioma__icontains=el) |
                                 Q(autores__icontains=el) |
                                 Q(categoria__icontains=el) |
                                 Q(dataPrimeiroAcesso__icontains=el) |
                                 Q(data_publicacao__icontains=el) |
                                 Q(portal__icontains=el) |
                                 Q(subject__icontains=el) |
                                 Q(link_externo__icontains=el))
        
                return self.queryset


class FiltroTituloResumo():
	pattern = r"\"([^\"]*)\"" 

	def __init__(self, string, queryset, field): #Construtor da classe.
		self.string = string
		self.palavras_especificas = re.findall(self.pattern, string)
		self.queryset = queryset
		self.field = field

	def TodosTermos(self):
		if len(self.palavras_especificas) != 0:
			for el in self.palavras_especificas:
				self.string = self.string.replace(el, '')
				if self.field == "titulo":
					self.queryset = self.queryset.filter(Q(titulo__icontains=el))
				else:
					self.queryset = self.queryset.filter(Q(resumo__icontains=el))

		self.string = self.string.replace('"', '')
		self.string = self.string.split()

		if self.string:
			for el in self.string:
				if self.field == "titulo":
					self.queryset = self.queryset.filter(Q(titulo__icontains=el))
				else:
					self.queryset = self.queryset.filter(Q(resumo__icontains=el))

		return self.queryset

	def QualquerTermo(self, queryset_vazia):
		if len(self.palavras_especificas) != 0:
			for el in self.palavras_especificas:
				self.string = self.string.replace('"' + el + '"', '')

				if self.field == "titulo":
					queryset_vazia = queryset_vazia | self.queryset.filter(Q(titulo__icontains=el))
				else:
					queryset_vazia = queryset_vazia | self.queryset.filter(Q(resumo__icontains=el))

		self.string = self.string.replace('"', "")
		self.string = self.string.split()

		if self.string:
			for el in self.string:

				if self.field == "titulo":
					queryset_vazia = queryset_vazia | self.queryset.filter(Q(titulo__icontains=el))
				else:
					queryset_vazia = queryset_vazia | self.queryset.filter(Q(resumo__icontains=el))
		
		self.queryset = queryset_vazia
		return self.queryset

	def NenhumTermo(self):
		if len(self.palavras_especificas) != 0:
			for el in self.palavras_especificas:
				self.string = self.string.replace('"' + el + '"', '')

				if self.field == "titulo":
					self.queryset = self.queryset.filter(~Q(titulo__icontains=el))
				else:
					self.queryset = self.queryset.filter(~Q(resumo__icontains=el))

		self.string = self.string.replace('"', '')
		self.string = self.string.split()

		if self.string:
			for el in self.string:
				if self.field == "titulo":
					self.queryset = self.queryset.filter(~Q(titulo__icontains=el))
				else:
					self.queryset = self.queryset.filter(~Q(resumo__icontains=el))

		return self.queryset


class FiltroAutores():

	def __init__(self, string, queryset):
		self.string = string.split(",")
		self.queryset = queryset

	def TodosAutores(self):
		for el in self.string:
			self.queryset = self.queryset.filter(Q(autores__icontains=el))
		return self.queryset

	def QualquerAutor(self, queryset_vazia):
		for el in self.string:
			queryset_vazia = queryset_vazia | self.queryset.filter(Q(autores__icontains=el))

		self.queryset = queryset_vazia	
		return self.queryset

	def NenhumAutor(self):
		for el in self.string:
			self.queryset = self.queryset.filter(~Q(autores__icontains=el))
		return self.queryset

class FiltroDatas():

	def __init__(self, dataMin, dataMax, queryset, field):
		self.dataMin = dataMin
		self.dataMax = dataMax
		self.queryset = queryset
		self.field = field

	def FiltrarData(self):
		if self.dataMin and self.dataMax:

			if self.field == "acesso":
				self.dataMin = self.dataMin.replace("/", "-")
				self.dataMax = self.dataMax.replace("/","-")
				self.queryset = self.queryset.filter(Q(dataPrimeiroAcesso__gte=self.dataMin),
                                        Q(dataPrimeiroAcesso__lte=self.dataMax))
			else:
				self.queryset = self.queryset.filter(Q(data_publicacao__gte=self.dataMin),
                                        Q(data_publicacao__lte=self.dataMax))

		elif self.dataMin and not self.dataMax:

			if self.field == "acesso":
				self.dataMin = self.dataMin.replace("/", "-")
				self.queryset = self.queryset.filter(Q(dataPrimeiroAcesso__gte=self.dataMin))
			else:
				self.queryset = self.queryset.filter(Q(data_publicacao__gte=self.dataMin))

		elif self.dataMax and not self.dataMin:

			if self.field == "acesso":
				self.dataMax = self.dataMax.replace("/","-")
				self.queryset = self.queryset.filter(Q(dataPrimeiroAcesso__lte=self.dataMax))
			else:
				self.queryset = self.queryset.filter(Q(data_publicacao__lte=self.dataMax))

		return self.queryset
