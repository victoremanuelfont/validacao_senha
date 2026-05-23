import os
import re
import pytest
import requests

# O hostname 'app' será resolvido pelo DNS interno do Docker Compose
BASE_URL = os.getenv("APP_URL", "http://app:5000")

def test_password_generation_is_secure():
    """Garante que o gerador entrega senhas que cumprem todos os requisitos."""
    response = requests.get(f"{BASE_URL}/generate?length=16")
    assert response.status_code == 200
    
    password = response.json().get("password")
    assert len(password) == 16
    assert re.search(r"[A-Z]", password)
    assert re.search(r"[a-z]", password)
    assert re.search(r"\d", password)
    assert re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

def test_validation_logic():
    """Valida se o endpoint /validate identifica corretamente senhas fracas e fortes."""
    # Teste de senhas inválidas
    invalid_passwords = [
        "Short1!",          # Muito curta
        "nouppercase12!",    # Sem maiúscula
        "NOLOWERCASE12!",    # Sem minúscula
        "NoSpecialChar12",   # Sem caractere especial
        "NoNumbersOnlyChar!" # Sem números
    ]
    
    for pwd in invalid_passwords:
        res = requests.post(f"{BASE_URL}/validate", json={"password": pwd})
        assert res.status_code == 200
        assert res.json().get("secure") is False

    # Teste de senha válida
    valid_res = requests.post(f"{BASE_URL}/validate", json={"password": "StrongPassword2026!"})
    assert valid_res.status_code == 200
    assert valid_res.json().get("secure") is True