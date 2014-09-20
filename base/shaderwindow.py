__author__ = 'akirayu101'

from PyQt5.QtGui import QOpenGLShaderProgram, QMatrix4x4
from PyQt5.QtCore import Qt
from OpenGL import GL
from base.openglwindow import OpenGLWindow


class ShaderWindow(OpenGLWindow):

    def __init__(self):
        super(ShaderWindow, self).__init__()

        self.m_program = 0
        self.m_vao = None

        self.m_model_matrix = QMatrix4x4()
        self.m_view_matrix = QMatrix4x4()
        self.m_projection_matrix = QMatrix4x4()

    @property
    def m_mvp_matrix(self):
        return self.m_projection_matrix * self.m_view_matrix * self.m_model_matrix

    def initialize_data(self):
        pass

    def initialize(self):
        self.initialize_data()
        self.create_shader()
        self.bind_attribute_localtion()
        self.create_vao()
        self.enableVAA()

    def bind_attribute_localtion(self):
        pass

    def create_shader(self):
        self.m_program = QOpenGLShaderProgram(self)

        for k, v in self.shader_files.items():
            self.m_program.addShaderFromSourceFile(k, v)
        self.m_program.link()

    def create_vao(self):

        vertex_array_object = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(vertex_array_object)

        vertex_buffer = GL.glGenBuffers(1)
        GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vertex_buffer)

    def enableVAA(self):
        pass

    def render(self):

        pass

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Up:
            self.m_model_matrix.rotate(2.0, 1.0, 0.0, 0.0)
        elif key == Qt.Key_Down:
            self.m_model_matrix.rotate(-2.0, 1.0, 0.0, 0.0)
        elif key == Qt.Key_Left:
            self.m_model_matrix.rotate(2.0, 0.0, 1.0, 0.0)
        elif key == Qt.Key_Right:
            self.m_model_matrix.rotate(-2.0, 0.0, 1.0, 0.0)
        else:
            pass
