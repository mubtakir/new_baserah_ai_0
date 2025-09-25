#!/usr/bin/env python3
"""
مراقب النظام - System Monitor
نظام بصيرة المتكامل

🔍 مراقبة أداء وحالة النظام
📊 إحصائيات مفصلة
⚡ تحليل الأداء

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import os
import sys
import time
import psutil
import threading
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class SystemMetrics:
    """مقاييس النظام"""
    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    disk_usage: float
    active_processes: int
    system_load: float

class BaseraSystemMonitor:
    """
    مراقب نظام بصيرة
    
    🔍 مراقبة شاملة لأداء النظام:
    - استخدام المعالج والذاكرة
    - مراقبة العمليات النشطة
    - تحليل الأداء المستمر
    - تنبيهات الأداء
    """
    
    def __init__(self):
        self.creation_time = datetime.now()
        self.metrics_history: List[SystemMetrics] = []
        self.monitoring_active = False
        self.monitor_thread = None
        
        print(f"🔍⚡ تم إنشاء مراقب نظام بصيرة")
        print(f"   🕐 وقت الإنشاء: {self.creation_time}")
    
    def get_current_metrics(self) -> SystemMetrics:
        """الحصول على مقاييس النظام الحالية"""
        return SystemMetrics(
            timestamp=datetime.now(),
            cpu_percent=psutil.cpu_percent(interval=1),
            memory_percent=psutil.virtual_memory().percent,
            disk_usage=psutil.disk_usage('/').percent,
            active_processes=len(psutil.pids()),
            system_load=os.getloadavg()[0] if hasattr(os, 'getloadavg') else 0.0
        )
    
    def start_monitoring(self, interval: int = 5):
        """بدء المراقبة المستمرة"""
        if self.monitoring_active:
            print("⚠️ المراقبة نشطة بالفعل")
            return
        
        self.monitoring_active = True
        self.monitor_thread = threading.Thread(
            target=self._monitor_loop,
            args=(interval,),
            daemon=True
        )
        self.monitor_thread.start()
        
        print(f"🔍 بدء المراقبة المستمرة (كل {interval} ثواني)")
    
    def stop_monitoring(self):
        """إيقاف المراقبة"""
        self.monitoring_active = False
        if self.monitor_thread:
            self.monitor_thread.join(timeout=2)
        
        print(f"⏹️ تم إيقاف المراقبة")
    
    def _monitor_loop(self, interval: int):
        """حلقة المراقبة الرئيسية"""
        while self.monitoring_active:
            try:
                metrics = self.get_current_metrics()
                self.metrics_history.append(metrics)
                
                # الاحتفاظ بآخر 100 قياس فقط
                if len(self.metrics_history) > 100:
                    self.metrics_history = self.metrics_history[-100:]
                
                # فحص التنبيهات
                self._check_alerts(metrics)
                
                time.sleep(interval)
                
            except Exception as e:
                print(f"❌ خطأ في المراقبة: {e}")
                time.sleep(interval)
    
    def _check_alerts(self, metrics: SystemMetrics):
        """فحص التنبيهات"""
        alerts = []
        
        if metrics.cpu_percent > 80:
            alerts.append(f"⚠️ استخدام المعالج عالي: {metrics.cpu_percent:.1f}%")
        
        if metrics.memory_percent > 85:
            alerts.append(f"⚠️ استخدام الذاكرة عالي: {metrics.memory_percent:.1f}%")
        
        if metrics.disk_usage > 90:
            alerts.append(f"⚠️ مساحة القرص منخفضة: {metrics.disk_usage:.1f}%")
        
        for alert in alerts:
            print(alert)
    
    def get_performance_report(self) -> Dict[str, Any]:
        """تقرير الأداء"""
        if not self.metrics_history:
            return {"error": "لا توجد بيانات مراقبة"}
        
        recent_metrics = self.metrics_history[-10:] if len(self.metrics_history) >= 10 else self.metrics_history
        
        avg_cpu = sum(m.cpu_percent for m in recent_metrics) / len(recent_metrics)
        avg_memory = sum(m.memory_percent for m in recent_metrics) / len(recent_metrics)
        avg_disk = sum(m.disk_usage for m in recent_metrics) / len(recent_metrics)
        
        return {
            "monitoring_duration": str(datetime.now() - self.creation_time),
            "total_measurements": len(self.metrics_history),
            "average_performance": {
                "cpu_percent": round(avg_cpu, 2),
                "memory_percent": round(avg_memory, 2),
                "disk_usage": round(avg_disk, 2)
            },
            "current_status": "healthy" if avg_cpu < 70 and avg_memory < 80 else "warning",
            "last_measurement": self.metrics_history[-1].timestamp.isoformat()
        }

def main():
    """اختبار مراقب النظام"""
    monitor = BaseraSystemMonitor()
    
    # عرض المقاييس الحالية
    current = monitor.get_current_metrics()
    print(f"\n📊 المقاييس الحالية:")
    print(f"   🖥️ المعالج: {current.cpu_percent:.1f}%")
    print(f"   💾 الذاكرة: {current.memory_percent:.1f}%")
    print(f"   💿 القرص: {current.disk_usage:.1f}%")
    print(f"   🔄 العمليات: {current.active_processes}")
    
    # بدء المراقبة لفترة قصيرة
    monitor.start_monitoring(interval=2)
    time.sleep(10)
    monitor.stop_monitoring()
    
    # عرض تقرير الأداء
    report = monitor.get_performance_report()
    print(f"\n📈 تقرير الأداء:")
    for key, value in report.items():
        print(f"   {key}: {value}")

if __name__ == "__main__":
    main()

