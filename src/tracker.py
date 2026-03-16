import os

# 1. 패키지가 있는지 확인하고, 없으면 조용히 넘어갑니다.
try:
    import requests
    from supabase import create_client, Client
    TRACKING_ENABLED = True
except ImportError:
    TRACKING_ENABLED = False

_supabase_client = None

def get_supabase_client():
    global _supabase_client
    if _supabase_client is None and TRACKING_ENABLED:
        supabase_url = "https://gkzbiacodysnrzbpvavm.supabase.co"
        supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdremJpYWNvZHlzbnJ6YnB2YXZtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzM1NzE2MTgsImV4cCI6MjA4OTE0NzYxOH0.Lv5uVeNZOyo21tgyl2jjGcESoLl_iQTJYp4jdCwuYDU"
        _supabase_client = create_client(supabase_url, supabase_key)
    return _supabase_client

def get_location_data():
    if not TRACKING_ENABLED:
        return None
    try:
        response = requests.get('http://ip-api.com/json/?fields=status,country,regionName,city,lat,lon', timeout=3)
        data = response.json()
        if data['status'] == 'success':
            return {
                'country': data['country'],
                'region': data['regionName'],
                'city': data['city'],
                'lat': data['lat'],
                'lon': data['lon']
            }
    except Exception:
        pass
    return None

def log_app_usage(app_name: str, action: str, details: dict = None):
    # 2. 패키지가 설치되지 않은 유저라면 여기서 함수를 즉시 종료합니다.
    if not TRACKING_ENABLED:
        return

    try:
        supabase = get_supabase_client()
        location = get_location_data()
        
        log_data = {
            'app_name': app_name,
            'action': action,
            'details': details or {},
        }
        
        if location:
            log_data.update({
                'country': location['country'],
                'region': location['region'],
                'city': location['city'],
                'lat': location['lat'],
                'lon': location['lon']
            })
            
        supabase.table('usage_logs').insert(log_data).execute()
    except Exception:
        pass