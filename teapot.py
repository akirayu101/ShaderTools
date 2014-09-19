__author__ = 'akirayu101'

from PyQt5.QtGui import (
    QGuiApplication, QSurfaceFormat, QOpenGLShader, QVector4D)
from base.shaderwindow import ShaderWindow
from OpenGL import GL
from base.objloader import load_obj


class TeaPot(ShaderWindow):

    def __init__(self):
        super(TeaPot, self).__init__()

    def initialize_data(self):
        self.m_vertices, _ = load_obj("materials/wt_teapot.obj")

        self.m_vertex_index = -1
        self.m_frame = 1

        self.shader_files = {}
        self.shader_files[
            QOpenGLShader.Vertex] = "shaders/teapot/teapot.vs.glsl"
        self.shader_files[
            QOpenGLShader.Fragment] = "shaders/teapot/teapot.fs.glsl"

    def bind_attribute_localtion(self):
        self.m_vertex_index = self.m_program.attributeLocation("m_vertex")
        self.m_color_index = self.m_program.attributeLocation("m_color")

    def enableVAA(self):
        GL.glEnableVertexAttribArray(self.m_vertex_index)
        # GL.glEnableVertexAttribArray(self.m_color_index)

    def render(self):
        self.m_frame += 1
        ratio = int(self.devicePixelRatio().real)
        GL.glViewport(0, 0, self.width() * ratio, self.height() * ratio)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.m_program.setAttributeArray(self.m_vertex_index, self.m_vertices)
        self.m_program.setAttributeValue(
            self.m_color_index, QVector4D(1.0, 0.0, 0.0, 0.0))
        self.m_program.bind()

        GL.glDrawArrays(GL.GL_TRIANGLES, 0, len(self.m_vertices))
        self.m_program.release()


if __name__ == '__main__':

    import sys

    app = QGuiApplication(sys.argv)

    surface_format = QSurfaceFormat()
    surface_format.setSamples(4)

    window = TeaPot()
    window.setFormat(surface_format)
    window.resize(600, 600)
    window.show()

    window.setAnimating(True)

    sys.exit(app.exec_())
