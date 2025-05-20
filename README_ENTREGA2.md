# 💾 Armazenamento de Dados do Sistema de Irrigação (Entrega 2)

Este módulo simula a persistência dos dados lidos pelo ESP32 em um banco SQL utilizando SQLAlchemy.

---

## 🧱 Estrutura da Tabela (`sensor_data`)

| Campo             | Tipo        | Descrição                              |
|------------------|-------------|----------------------------------------|
| id               | Inteiro     | Identificador único (chave primária)   |
| phosphorus       | Boolean     | Indica presença de fósforo             |
| potassium        | Boolean     | Indica presença de potássio            |
| ph               | Float       | Valor do pH do solo                    |
| humidity         | Float       | Umidade do solo (%)                    |
| irrigation_status| String(10)  | Estado da bomba: 'Ligada' ou 'Desligada' |
| created_at       | Timestamp   | Data/hora da inserção automática       |

---

## 🧩 Justificativa e Relação com o MER (Fase 2)

A estrutura segue o modelo relacional criado na fase anterior, representando a entidade **LeituraSensor** com os atributos principais registrados pelo ESP32.

Essa entidade pode futuramente se relacionar com uma entidade `Sensor`, `ÁreaPlantio` ou `Dispositivo` via chaves estrangeiras.

---

## ⚙️ Operações CRUD

- **Inserção**: Simula leitura vinda do monitor serial.
- **Consulta**: Lista os dados armazenados.
- **Atualização**: Modifica o valor de umidade de um registro.
- **Remoção**: Deleta um registro com base no ID.

---

## 🚀 Execução

Para rodar:

```bash
pip install sqlalchemy
python armazenamento_irrigacao.py
```

Você pode trocar o banco SQLite por Oracle, PostgreSQL, MySQL alterando a `DATABASE_URL`.

---

Desenvolvido para FarmTech Solutions 🌾