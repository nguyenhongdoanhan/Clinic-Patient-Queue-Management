import os
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import SQLAlchemyError


def load_env(path='.env'):
    data = {}
    if not os.path.exists(path):
        return data
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                data[k.strip()] = v.strip().strip('"').strip("'")
    return data


def main():
    env = load_env('.env')
    db_url = env.get('DATABASE_URL') or os.environ.get('DATABASE_URL')
    if not db_url:
        print('No DATABASE_URL found in .env or environment; aborting')
        return

    print('Connecting to', db_url)
    try:
        engine = create_engine(db_url, pool_pre_ping=True)
        inspector = inspect(engine)
    except SQLAlchemyError as e:
        print('Could not create engine:', e)
        return

    if 'patients' not in inspector.get_table_names():
        print('No patients table present; nothing to do.')
        return

    cols = [c['name'] for c in inspector.get_columns('patients')]
    stmts = []
    if 'gender' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN gender VARCHAR(20) NULL")
    if 'birthday' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN birthday DATE NULL")
    if 'phone' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN phone VARCHAR(20) NULL")
    if 'email' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN email VARCHAR(100) NULL")
    if 'address' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN address VARCHAR(255) NULL")
    if 'created_at' not in cols:
        stmts.append("ALTER TABLE patients ADD COLUMN created_at DATETIME NULL")

    if not stmts:
        print('All expected columns already present.')
        return

    try:
        with engine.connect() as conn:
            for s in stmts:
                print('Executing:', s)
                conn.execute(text(s))
            conn.commit()
        print('Schema patch applied.')
    except SQLAlchemyError as e:
        print('Failed to apply schema patch:', e)


if __name__ == '__main__':
    main()
