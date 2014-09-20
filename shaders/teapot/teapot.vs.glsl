#version 410 core
layout (location = 1) in vec4 m_norm;
layout (location = 2) in vec4 m_vertex;
layout (location = 4) in vec4 m_color;
out vec4 color;

void main()
{
    gl_Position = m_vertex;
    color = m_color;
    m_norm;
}