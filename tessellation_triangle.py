from PyQt5.QtGui import (
    QGuiApplication, QSurfaceFormat, QOpenGLShader, QVector4D)
from base.shaderwindow import ShaderWindow
from OpenGL import GL


class TessellationTriangle(ShaderWindow):

    def __init__(self):
        super(TessellationTriangle, self).__init__()

    def initialize_data(self):
        self.m_vertices = [(0.25, -0.25, 0, 1.0),
                           (-0.25, -0.25, 0, 1.0),
                           (0.25,  0.25, 0, 1.0)]

        self.m_vertex_index = -1
        self.m_frame = 1

        self.shader_files = {}
        self.shader_files[
            QOpenGLShader.Vertex] = "shaders/tessellation_triangle/tessellation.vs.glsl"
        self.shader_files[
            QOpenGLShader.Fragment] = "shaders/tessellation_triangle/tessellation.fs.glsl"
        self.shader_files[
            QOpenGLShader.TessellationControl] = "shaders/tessellation_triangle/tessellation.tc.glsl"
        self.shader_files[
            QOpenGLShader.TessellationEvaluation] = "shaders/tessellation_triangle/tessellation.te.glsl"

    def bind_attribute_localtion(self):
        self.m_vertex_index = self.m_program.attributeLocation("m_vertex")
        self.m_offset_index = self.m_program.attributeLocation("m_offset")

    def enableVAA(self):
        GL.glEnableVertexAttribArray(self.m_vertex_index)

    def render(self):
        self.m_frame += 1
        ratio = int(self.devicePixelRatio().real)
        GL.glViewport(0, 0, self.width() * ratio, self.height() * ratio)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)

        self.m_program.setAttributeArray(self.m_vertex_index, self.m_vertices)
        self.m_program.setAttributeValue(
            self.m_offset_index, QVector4D(0.0, 0.0, 0.0, 0.0))
        self.m_program.bind()

        GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)
        GL.glPatchParameteri(GL.GL_PATCH_VERTICES, 3)
        GL.glDrawArrays(GL.GL_PATCHES, 0, 3)
        self.m_program.release()


if __name__ == '__main__':

    import sys

    app = QGuiApplication(sys.argv)

    surface_format = QSurfaceFormat()
    surface_format.setSamples(4)

    window = TessellationTriangle()
    window.setFormat(surface_format)
    window.resize(800, 600)
    window.show()

    window.setAnimating(True)

    sys.exit(app.exec_())
