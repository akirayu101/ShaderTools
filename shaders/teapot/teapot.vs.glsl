#version 410 core
in vec4 m_norm;
in vec4 m_vertex;
in vec4 m_color;

uniform mat4 m_mvp;
out vec4 color;

void main()
{
    gl_Position = m_mvp * m_vertex;
    color = m_color;
    m_norm;
}