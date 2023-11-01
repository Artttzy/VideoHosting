import os
import dotenv

dotenv.load_dotenv()

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(engine)