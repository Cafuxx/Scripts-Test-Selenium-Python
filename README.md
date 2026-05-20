# Selenium Python Tests

![Tests](https://github.com/Cafuxx/selenium-python-tests/actions/workflows/selenium.yml/badge.svg)

Proyecto de automatización QA desarrollado con Selenium, Pytest y Python utilizando buenas prácticas de testing automation y CI/CD.

---

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- ChromeDriver
- WebDriver Manager
- Pytest HTML Reports
- GitHub Actions

---

## Objetivo

Practicar automatización de pruebas E2E (End-to-End) sobre la plataforma:

https://www.saucedemo.com/

Aplicando:

- Page Object Model (POM)
- Fixtures con Pytest
- Parametrize
- Markers (Smoke / Regression)
- Selenium Headless
- Continuous Integration (CI/CD)

---

## Arquitectura del proyecto

```plaintext
.
├── .github/workflows/
│   └── selenium.yml
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── login_test.py
│   ├── checkout_test.py
│   ├── cart_validation_test.py
│   ├── add_and_remove_from_cart_test.py
│   └── order_products_by_price_test.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Tests implementados

- Login validation
- Add product to cart
- Remove product from cart
- Checkout flow
- Cart validation
- Product sorting validation

---

## Features implementadas

- Page Object Model (POM)
- Reusable page classes
- Pytest fixtures
- Headless browser execution
- Parametrized tests
- Smoke & Regression markers
- Explicit waits
- HTML reports
- GitHub Actions CI pipeline
- Automatic test execution on push/pull request

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/Cafuxx/selenium-python-tests.git
```

Entrar al proyecto:

```bash
cd selenium-python-tests
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar tests

Ejecutar toda la suite:

```bash
pytest tests/ -v --tb=short
```

Ejecutar smoke tests:

```bash
pytest -m smoke
```

Ejecutar regression tests:

```bash
pytest -m regression
```

---

## Reportes HTML

Generar reporte HTML:

```bash
pytest tests/ --html=report.html --self-contained-html
```

El reporte incluye:

- Tests pasados/fallados
- Duración de ejecución
- Detalles de errores
- Información de entorno

---

## CI/CD con GitHub Actions

El proyecto utiliza GitHub Actions para ejecutar automáticamente los tests en cada:

- Push
- Pull Request

Workflow ubicado en:

```plaintext
.github/workflows/selenium.yml
```

---

## Aprendizajes

Este proyecto fue realizado para practicar:

- Selenium WebDriver
- Automatización E2E
- Diseño Page Object Model
- Fixtures y parametrización con Pytest
- Explicit waits
- Testing headless
- CI/CD pipelines
- GitHub Actions
- Reportes HTML automatizados
- Organización profesional de frameworks QA

---

## Estado del proyecto

✅ Tests automatizados funcionando  
✅ CI/CD activo con GitHub Actions  
✅ HTML reports generados automáticamente  
✅ Framework estructurado con POM