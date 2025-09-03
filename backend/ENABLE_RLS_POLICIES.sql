-- 🚀 LS WEB - HABILITAR ACCESO A TABLAS EN SUPABASE
-- Ejecuta este código en el SQL Editor de Supabase DESPUÉS de crear las tablas

-- Habilitar RLS en las tablas
ALTER TABLE contact_requests ENABLE ROW LEVEL SECURITY;
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Políticas para contact_requests (acceso público para lectura, solo autenticados para escritura)
CREATE POLICY "Allow public read access to contact_requests" ON contact_requests
  FOR SELECT TO anon
  USING (true);

CREATE POLICY "Allow authenticated insert to contact_requests" ON contact_requests
  FOR INSERT TO authenticated
  WITH CHECK (true);

-- Para desarrollo: permitir inserción pública en contact_requests
CREATE POLICY "Allow public insert to contact_requests for development" ON contact_requests
  FOR INSERT TO anon
  WITH CHECK (true);

-- Políticas para users (solo admins pueden acceder)
CREATE POLICY "Allow admin read access to users" ON users
  FOR SELECT TO authenticated
  USING (auth.jwt() ->> 'role' = 'admin');

CREATE POLICY "Allow admin insert to users" ON users
  FOR INSERT TO authenticated
  WITH CHECK (auth.jwt() ->> 'role' = 'admin');

-- Para desarrollo: permitir acceso temporal sin autenticación (REMOVER EN PRODUCCIÓN)
CREATE POLICY "Allow public read access to users for development" ON users
  FOR SELECT TO anon
  USING (true);

CREATE POLICY "Allow public insert to users for development" ON users
  FOR INSERT TO anon
  WITH CHECK (true);

-- Verificar políticas
SELECT schemaname, tablename, policyname, permissive, roles, cmd, qual
FROM pg_policies
WHERE tablename IN ('contact_requests', 'users')
ORDER BY tablename, policyname;
