#!/usr/bin/env python3
"""
🚀 LS WEB - SCRIPT DE PRUEBA FINAL DE LA API
Ejecuta este script para verificar que todo funciona correctamente
"""

import requests
import json
import sys

def test_api():
    print("🚀 LS WEB - PRUEBA FINAL DE LA API")
    print("=" * 50)

    base_url = "http://localhost:8000"
    all_tests_passed = True

    # Test 1: Root endpoint
    print("\n1. 🏠 Probando endpoint raíz...")
    try:
        response = requests.get(f"{base_url}/api/")
        if response.status_code == 200:
            print("   ✅ Status: 200 OK")
            print(f"   📝 Response: {response.text}")
        else:
            print(f"   ❌ Status: {response.status_code}")
            all_tests_passed = False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        all_tests_passed = False

    # Test 2: Contact requests (should show data now)
    print("\n2. 📋 Probando obtener solicitudes de contacto...")
    try:
        response = requests.get(f"{base_url}/api/contact-requests")
        if response.status_code == 200:
            data = response.json()
            print("   ✅ Status: 200 OK")
            print(f"   📊 Número de solicitudes: {len(data)}")
            if data:
                print("   📝 Primera solicitud:")
                print(f"      Nombre: {data[0].get('name', 'N/A')}")
                print(f"      Email: {data[0].get('email', 'N/A')}")
                print(f"      Proyecto: {data[0].get('project_type', 'N/A')}")
        else:
            print(f"   ❌ Status: {response.status_code}")
            print(f"   📝 Response: {response.text}")
            all_tests_passed = False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        all_tests_passed = False

    # Test 3: Login con admin
    print("\n3. 🔐 Probando login de admin...")
    try:
        login_data = {
            "email": "admin@lsweb.com",
            "password": "admin123"
        }
        response = requests.post(f"{base_url}/api/login", json=login_data)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print("   ✅ Login exitoso!")
                print(f"   👤 Usuario: {data.get('user', {}).get('email', 'N/A')}")
                print(f"   🎭 Rol: {data.get('user', {}).get('role', 'N/A')}")
                print(f"   🔑 Token generado: {data.get('token')[:20]}...")
            else:
                print("   ❌ Login falló")
                print(f"   📝 Mensaje: {data.get('message', 'Sin mensaje')}")
                all_tests_passed = False
        else:
            print(f"   ❌ Status: {response.status_code}")
            all_tests_passed = False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        all_tests_passed = False

    # Test 4: Crear nueva solicitud de contacto
    print("\n4. 📝 Probando crear nueva solicitud de contacto...")
    try:
        contact_data = {
            "name": "Cliente de Prueba Final",
            "email": "cliente@final.com",
            "phone": "+5491187654321",
            "company": "Empresa Final S.A.",
            "projectType": "crm-personalizado",
            "budget": "$15,000 - $25,000",
            "timeline": "4-6 meses",
            "description": "Esta es una solicitud de prueba final para verificar que la API funciona completamente con Supabase."
        }
        response = requests.post(f"{base_url}/api/contact-request", json=contact_data)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print("   ✅ Solicitud creada exitosamente!")
                print(f"   🆔 ID generado: {data.get('id', 'N/A')}")
                print(f"   📝 Mensaje: {data.get('message', 'N/A')}")
            else:
                print("   ❌ Error al crear solicitud")
                all_tests_passed = False
        else:
            print(f"   ❌ Status: {response.status_code}")
            print(f"   📝 Response: {response.text}")
            all_tests_passed = False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        all_tests_passed = False

    # Test 5: Verificar que la nueva solicitud aparece en la lista
    print("\n5. 📊 Verificando que la nueva solicitud aparece en la lista...")
    try:
        response = requests.get(f"{base_url}/api/contact-requests")
        if response.status_code == 200:
            data = response.json()
            print("   ✅ Status: 200 OK")
            print(f"   📊 Total de solicitudes ahora: {len(data)}")

            # Buscar la solicitud que acabamos de crear
            found = False
            for req in data:
                if req.get('email') == 'cliente@final.com':
                    found = True
                    print("   ✅ ¡Nueva solicitud encontrada en la lista!")
                    print(f"      📝 Descripción: {req.get('description', '')[:50]}...")
                    break

            if not found:
                print("   ⚠️  Nueva solicitud no encontrada en la lista (posible problema de RLS)")
                all_tests_passed = False
        else:
            print(f"   ❌ Status: {response.status_code}")
            all_tests_passed = False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        all_tests_passed = False

    # Resultado final
    print("\n" + "=" * 50)
    if all_tests_passed:
        print("🎉 ¡TODOS LOS TESTS PASARON! La API está funcionando correctamente.")
        print("✅ Conexión con Supabase: OK")
        print("✅ Tablas creadas: OK")
        print("✅ Políticas RLS: OK")
        print("✅ Login de admin: OK")
        print("✅ CRUD de solicitudes: OK")
    else:
        print("⚠️  Algunos tests fallaron. Revisa los pasos anteriores:")
        print("1. Verifica que ejecutaste CREATE_TABLES_SUPABASE.sql")
        print("2. Verifica que ejecutaste ENABLE_RLS_POLICIES.sql")
        print("3. Verifica las credenciales en .env")
        print("4. Reinicia el servidor si es necesario")

    print("\n📋 Endpoints disponibles:")
    print(f"   🌐 API Docs: http://localhost:8001/docs")
    print(f"   🏠 Root: http://localhost:8001/api/")
    print(f"   📧 Contact: http://localhost:8001/api/contact-request")
    print(f"   📋 List: http://localhost:8001/api/contact-requests")
    print(f"   🔐 Login: http://localhost:8001/api/login")
    print(f"   👑 Init Admin: http://localhost:8001/api/init-admin")

    return all_tests_passed

if __name__ == "__main__":
    success = test_api()
    sys.exit(0 if success else 1)
