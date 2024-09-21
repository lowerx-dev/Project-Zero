# Model
from models import Base

# sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# SQLALCHEMY INIT
engine = create_async_engine("sqlite+aiosqlite:///database.db", connect_args={"check_same_thread": False})
SessionLocal = async_sessionmaker(engine, autoflush=True)

async def get_session_db():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as db:
        try:
            yield db
        except Exception as e:
            await db.rollback()
            raise e
        
        finally:
            await db.close()