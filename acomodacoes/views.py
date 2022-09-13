from django.shortcuts import render

# Views criadas.

acomodacoes = [
    {
        "id" : 1,
        "tipo" : "Chalé",
        "descrição" : "Chalé com 1 cama de casal. Conta com um frigobar, uma tv e um ar-condicionado"
    },
    {
        "id" : 2,
        "tipo" : "Chalé Quadruplo",
        "descrição" : "Chalé com 2 cama de casal. Conta com um frigobar, uma tv e um ar-condicionado"
    },
    {
        "id" : 3,
        "tipo" : "Apartamento Single",
        "descrição" : "Apartamento com 1 cama de casal. Conta com um frigobar, uma tv e um ar-condicionado"
    },
    {
        "id" : 4,
        "tipo" : "Apartamento Triplo",
        "descrição" : "Apartamento com 1 cama de casal e 1 de cama de solteiro. Conta com um frigobar, uma tv e um ar-condicionado"
    },
]


# Create your views here.
def listar_acomodacoes(request):
    return render(request, 'listar_acomodacoes.html',{'acomodacoes':acomodacoes})

def detalhe(request, acomodacao_id):
    return render(request,'detalhe.html',{'acomodacao': acomodacoes[acomodacao_id]})
