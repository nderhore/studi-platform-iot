import bcrypt

config_bcrypt = bcrypt.gensalt()


def encode_password(password: str) -> bytes:
    return bcrypt.hashpw(bytes(password, encoding='utf-8')
                         , config_bcrypt)
