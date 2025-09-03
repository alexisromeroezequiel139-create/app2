# 🚀 Cómo Lanzar la API LS WEB

## 📋 Prerrequisitos
- Python 3.8+ instalado
- Dependencias instaladas: `pip install -r requirements_supabase.txt`

## 🔧 Configuración Obligatoria

### 1. Configurar variables de entorno
Edita el archivo `backend/.env` con tus credenciales reales:

```env
# Supabase - Obtén estas credenciales desde tu dashboard de Supabase
SUPABASE_URL=https://tu-proyecto.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# JWT - Cambia esto en producción
JWT_SECRET=tu-clave-secreta-super-segura-aqui

# Email - Configuración SMTP (Gmail recomendado)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tu-email@gmail.com
SMTP_PASSWORD=tu-contraseña-de-aplicacion
EMAIL_TO=alexisromeroezequiel139@gmail.com
```

### 2. Para Gmail: Crear contraseña de aplicación
1. Ve a https://myaccount.google.com/security
2. Activa la verificación en 2 pasos
3. Genera una "Contraseña de aplicación" para usar con SMTP

## 🚀 Métodos para Lanzar la API

### Opción 1: Usando uvicorn directamente (Recomendado)
```bash
cd backend
uvicorn server_supabase:app --reload --host 0.0.0.0 --port 8000
```

### Opción 2: Ejecutando el archivo Python
```bash
cd backend
python server_supabase.py
```

### Opción 3: Con hot reload para desarrollo
```bash
cd backend
uvicorn server_supabase:app --reload
```

## ✅ Verificación
Si todo funciona correctamente, deberías ver:
- Mensaje: "LS WEB API Starting up with Supabase..."
- API disponible en: http://localhost:8000
- Documentación automática: http://localhost:8000/docs

## 🐛 Solución de Problemas Comunes

### Error: "ModuleNotFoundError"
```bash
# Instalar dependencias faltantes
pip install -r requirements_supabase.txt
```

### Error: Variables de entorno faltantes
- Verifica que el archivo `.env` existe en la carpeta `backend/`
- Confirma que todas las variables están configuradas correctamente

### Error: Conexión a Supabase
- Verifica que SUPABASE_URL y SUPABASE_KEY son correctos
- Confirma que Supabase está activo y las tablas existen

### Error: SMTP/Email
- Usa contraseñas de aplicación, no tu contraseña normal de Gmail
- Verifica que el puerto 587 no esté bloqueado

## 📊 Endpoints Disponibles
- `GET /` - Health check
- `POST /api/contact-request` - Crear solicitud de contacto
- `POST /api/login` - Login de administrador
- `GET /api/contact-requests` - Obtener todas las solicitudes
- `POST /api/init-admin` - Crear usuario admin por defecto

## 🔒 Usuario Admin por Defecto
- Email: `admin@lsweb.com`
- Contraseña: `admin123`
