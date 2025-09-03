-- 🚀 LS WEB - CREACIÓN DE TABLAS EN SUPABASE
-- Ejecuta este código en el SQL Editor de Supabase

-- Tabla para solicitudes de contacto
CREATE TABLE contact_requests (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  company VARCHAR(100),
  project_type VARCHAR(50) NOT NULL,
  budget VARCHAR(50),
  timeline VARCHAR(50),
  description TEXT NOT NULL,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tabla para usuarios
CREATE TABLE users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) DEFAULT 'admin',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Índices para mejor performance
CREATE INDEX idx_contact_requests_created_at ON contact_requests(created_at DESC);
CREATE INDEX idx_users_email ON users(email);

-- Insertar usuario admin por defecto
INSERT INTO users (email, password_hash, role) VALUES (
  'admin@lsweb.com',
  '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewRuIwmH.LhqV1u6', -- password: admin123
  'admin'
);

-- Insertar usuario adicional con la contraseña correcta
INSERT INTO users (email, password_hash, role) VALUES (
  'alexisromeroezequiel139@gmail.com',
  '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewRuIwmH.LhqV1u6', -- password: admin123
  'admin'
);

-- Verificar que las tablas se crearon correctamente
SELECT 'Tables created successfully!' as status;
