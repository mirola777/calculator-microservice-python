import unittest

from src.main import app


class TestHttpRequest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def test_saludo_por_defecto(self):
        response = self.client.get("/hola")
        self.assertIn("Hola Mundo!", response.text)

    def test_cuadrado_por_defecto(self):
        response = self.client.get("/cuadrado")
        self.assertRegex(response.text, r"El cuadrado de 0.0 es 0.0")

    def test_cubo_por_defecto(self):
        response = self.client.get("/cubo")
        self.assertRegex(response.text, r"El cubo de 0.0 es 0.0")

    def test_cuadrado_numero(self):
        response = self.client.get("/cuadrado?numero=3")
        self.assertRegex(response.text, r"El cuadrado de 3.0 es 9.0")

    def test_cubo_numero(self):
        response = self.client.get("/cubo?numero=3")
        self.assertRegex(response.text, r"El cubo de 3.0 es 27.0")

if __name__ == "__main__":
    unittest.main()