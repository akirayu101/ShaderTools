from PyQt5.QtGui import (QGuiApplication, QSurfaceFormat, QOpenGLShader, QVector4D)
from base.shaderwindow import ShaderWindow
from OpenGL import GL
from math import (sin, cos)


class MovingTriangle(ShaderWindow):

    def __init__(self):
        super(MovingTriangle, self).__init__()

    def initialize_data(self):
        self.m_vertices = [(0.25, -0.25, 0, 1.0),
                           (-0.25, -0.25, 0, 1.0),
                           (0.25,  0.25, 0, 1.0)]

        self.m_colors = [(0.0, 0.0, 1.0, 1.0),
                         (1.0, 0.0, 0.0, 1.0),
                         (0.0, 1.0, 0.0, 1.0)]

        self.m_vertex_index = -1
        self.m_color_index = -1
        self.m_frame = 1

        self.shader_files = {}
        self.shader_files[QOpenGLShader.Vertex] = "shaders/moving_triangle/moving_triangle.vs.glsl"
        self.shader_files[QOpenGLShader.Fragment] = "shaders/moving_triangle/moving_triangle.fs.glsl"

    def bind_attribute_localtion(self):
        self.m_vertex_index = self.m_program.attributeLocation("m_vertex")
        self.m_color_index = self.m_program.attributeLocation("m_color")
        self.m_offset_index = self.m_program.attributeLocation("m_offset")

    def enableVAA(self):
        GL.glEnableVertexAttribArray(self.m_vertex_index)
        GL.glEnableVertexAttribArray(self.m_color_index)

    def render(self):
        self.m_frame += 1
        ratio = int(self.devicePixelRatio().real)
        GL.glViewport(0, 0, self.width()*ratio, self.height()*ratio)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.m_program.setAttributeArray(self.m_color_index, self.m_colors)
        self.m_program.setAttributeArray(self.m_vertex_index, self.m_vertices)
        self.m_program.setAttributeValue(self.m_offset_index, QVector4D(sin(self.m_frame/20)*0.5, cos(self.m_frame/20)*0.5, 0.0, 0.0))
        self.m_program.bind()
        GL.glDrawArrays(GL.GL_TRIANGLES, 0, 3)
        self.m_program.release()


if __name__ == '__main__':

    import sys

    app = QGuiApplication(sys.argv)

    surface_format = QSurfaceFormat()
    surface_format.setSamples(4)

    window = MovingTriangle()
    window.setFormat(surface_format)
    window.resize(800, 600)
    window.show()

    window.setAnimating(True)

    sys.exit(app.exec_())
