# -*- coding: utf-8 -*-

import unittest
import psycopg2
from QueTocaBBDD import Horario

class TestQueToca(unittest.TestCase):
    def setUp(self):
        self.horario = Horario()

    def test_objeto_inicializado_correctamente(self):
        self.assertIsInstance(self.horario, Horario, "El objeto se ha creado correctamente.")

    def test_conexion_a_bd_correcto(self):
        self.assertIsInstance(self.horario.ConexionABaseDatos(), psycopg2.extensions.connection, "Se ha conectado a la base de datos")

    def test_crear_horario(self):
        self.assertTrue(self.horario.CrearHorario(), "Se ha creado un nuevo horario.")

    def test_leer_horario(self):
        self.assertIsInstance(self.horario.LeerHorario(4), str, "Se ha leido el horario.")

    def test_modificar_horario(self):
        self.assertTrue(self.horario.ModificarHorario(), "Se ha modificado el horario.")

    def test_borrar_horario(self):
        self.assertTrue(self.horario.BorrarHorario(), "Se ha borrado el horario.")

    def test_profesor_asignatura(self):
        self.assertIsInstance(self.horario.ProfesorAsignatura("Infraestructura virtual"), str, "Se ha leido un profesor.")

    def test_mis_asignaturas(self):
    	self.assertIsInstance(self.horario.MisAsignaturas(), str, "Se ha leido mis asignaturas.")

    def test_mi_dia(self):
    	self.assertIsInstance(self.horario.MiDia("2016-11-06"), str, "Se ha leido mi dia.")


if __name__ == '__main__':
    unittest.main()
