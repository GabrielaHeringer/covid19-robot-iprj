Para contornar o problema de de timed out do domínio https://covid-search.doctorevidence.com/
subdividimos a spider em 3 partes, cada uma contendo as querys da página principal do DocEvidence
classificadas pelo seu tamanho limite.

--- CovidSearchDoctorEvidence1
Abrange os resultados de pesquisa com menos de 1000 novos registros
[2, 5, 7, 9, 12, 13, 14, 16, 17, 18, 19, 20, 23, 24, 26, 27, 31, 32, 33, 35, 39, 43]

---CovidSearchDoctorEvidence2
Abrange	os resultados de pesquisa com menos de 10000 novos registros   
[3, 4, 6, 8, 10, 11, 21, 25, 29, 30, 34, 36, 37, 38, 40, 41, 42]

---CovidSearchDoctorEvidence3
Abrange os resultados de pesquisa com menos de 20000 novos registros
3-1:
[0]
3-2:
[1, 15, 22, 28]
3-3:
[44]
