# Guía de Despliegue - LS WEB

## Paso 1: Preparar Repositorio en GitHub
1. Crear repositorio público en GitHub llamado "ls-web-app"
2. Subir todo el código del proyecto al repositorio

## Paso 2: Desplegar Backend (Railway)
1. Ir a https://railway.app
2. Crear cuenta / iniciar sesión
3. Crear nuevo proyecto
4. Conectar con GitHub y seleccionar el repositorio "ls-web-app"
5. Configurar variables de entorno:
   - SUPABASE_URL
   - SUPABASE_KEY
   - JWT_SECRET
   - SMTP_HOST
   - SMTP_PORT
   - SMTP_USER
   - SMTP_PASSWORD
   - EMAIL_TO
6. Railway detectará automáticamente FastAPI y lo desplegará
7. Obtener la URL pública del backend (ej: https://ls-web-backend.up.railway.app)

## Paso 3: Actualizar Frontend
1. En el archivo frontend/.env, cambiar REACT_APP_BACKEND_URL a la URL del backend desplegado
2. Subir los cambios al repositorio GitHub

## Paso 4: Desplegar Frontend (Vercel)
1. Ir a https://vercel.com
2. Crear cuenta / iniciar sesión
3. Importar proyecto desde GitHub
4. Seleccionar el repositorio "ls-web-app"
5. Configurar build settings:
   - Root Directory: frontend
   - Build Command: npm run build
   - Output Directory: build
6. Agregar variable de entorno: REACT_APP_BACKEND_URL con la URL del backend
7. Desplegar

## URLs Finales
- Frontend: https://ls-web-app.vercel.app
- Backend: https://ls-web-backend.up.railway.app

## Testing
1. Probar formulario de contacto en el frontend
2. Probar login con admin@lsweb.com / admin123
3. Verificar que los emails se envíen correctamente
