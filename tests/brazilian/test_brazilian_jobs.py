from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    expected_output = [
        {
            "title": "Maquinista",
            "salary": "2000",
            "type": "trainee"
        },
        {
            "title": "Motorista",
            "salary": "3000",
            "type": "full time"
        },
        {
            "title": "Analista de Software",
            "salary": "4000",
            "type": "full time"
        },
        {
            "title": "Assistente administrativo",
            "salary": "1700",
            "type": "full time"
        },
        {
            "title": "Auxiliar administrativo",
            "salary": "1400",
            "type": "full time"
        },
        {
            "title": "Auxiliar usinagem",
            "salary": "1400",
            "type": "full time"
        },
        {
            "title": "Auxiliar de padaria",
            "salary": "1400",
            "type": "full time"
        },
        {
            "title": "Analista Contábil",
            "salary": "1400",
            "type": "full time"
        },
        {
            "title": "Gerente comercial",
            "salary": "5000",
            "type": "full time"
        },
        {
            "title": "Analista de Departamento Pessoal",
            "salary": "4000",
            "type": "full time"
        },
        {
            "title": "Esportista de Futebol profissional",
            "salary": "50000",
            "type": "full time"
        },
        {
            "title": "Analista de crédito",
            "salary": "4000",
            "type": "full time"
        },
        {
            "title": "Pessoa Programadora",
            "salary": "3000",
            "type": "full time"
        },
        {
            "title": "Ux Designer",
            "salary": "3000",
            "type": "full time"
        },
        {
            "title": "Auxiliar de manutenção",
            "salary": "1400",
            "type": "full time"
        }
    ]
    result = read_brazilian_file(path)
    for item in result:
        item['type'] = item.get('type', '').strip()
        item['salary'] = item.get('salary', '').strip()
    assert result == expected_output
