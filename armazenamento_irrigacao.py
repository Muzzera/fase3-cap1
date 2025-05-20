from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Substitua esta URL conforme o banco desejado (ex: oracle+cx_oracle://usuario:senha@host:porta/service)
DATABASE_URL = 'sqlite:///sensor.db'

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phosphorus = Column(Boolean)
    potassium = Column(Boolean)
    ph = Column(Float)
    humidity = Column(Float)
    irrigation_status = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.drop_all(engine)  # Apenas para testes, remove tabela existente
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserção de dados simulados (copiados do monitor serial)
samples = [
    SensorData(phosphorus=True, potassium=False, ph=6.8, humidity=35.5, irrigation_status='Ligada'),
    SensorData(phosphorus=True, potassium=True, ph=6.5, humidity=60.0, irrigation_status='Desligada'),
    SensorData(phosphorus=False, potassium=True, ph=4.9, humidity=45.0, irrigation_status='Ligada'),
]

session.add_all(samples)
session.commit()

# Consulta
print("\n📋 Dados armazenados:")
for s in session.query(SensorData).all():
    print(vars(s))

# Atualização
record = session.query(SensorData).filter_by(id=1).first()
if record:
    record.humidity = 50.0
    session.commit()

# Remoção
record_to_delete = session.query(SensorData).filter_by(id=3).first()
if record_to_delete:
    session.delete(record_to_delete)
    session.commit()

session.close()