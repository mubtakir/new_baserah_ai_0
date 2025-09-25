#!/usr/bin/env python3
"""
مُشغل نظام بصيرة الثوري المكتمل النهائي
Basera Revolutionary AI System - Complete Final Launcher

🌟 نظام متكامل لتشغيل جميع مكونات بصيرة
🚀 واجهة موحدة لجميع الوظائف
🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

المطور: باسل يحيى عبدالله
"""

import os
import sys
import time
import subprocess
from datetime import datetime
from typing import Dict, List, Optional

class BaseraSystemLauncher:
    """مُشغل نظام بصيرة المتكامل"""
    
    def __init__(self):
        self.creation_time = datetime.now()
        self.available_components = self._check_components()
        
        print(f"🌟 مرحباً بك في نظام بصيرة الثوري المكتمل!")
        print(f"🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
        print(f"📅 تاريخ التشغيل: {self.creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🔧 المكونات المتاحة: {len(self.available_components)}/13")
    
    def _check_components(self) -> Dict[str, bool]:
        """فحص المكونات المتاحة"""
        components = {
            "المعادلة الأم الثورية": "revolutionary_mother_equation.py",
            "النواة التفكيرية": "complete_multi_layer_thinking_core.py",
            "قواعد البيانات المتخصصة": "complete_specialized_databases.py",
            "المعادلات المتكيفة": "adaptive_revolutionary_equations_fixed.py",
            "نظام الخبير/المستكشف": "expert_explorer_system.py",
            "الوكيل الذكي": "revolutionary_intelligent_agent.py",
            "الوحدة الفنية للنشر": "artistic_publishing_unit.py",
            "أنظمة المعرفة": "specialized_knowledge_systems.py",
            "المكونات الرياضية": "advanced_mathematical_components.py",
            "واجهات المستخدم": "multi_user_interfaces.py",
            "نظام الاختبار": "comprehensive_testing_system.py",
            "الوحدة الفنية المحسنة": "enhanced_artistic_unit_fixed.py",
            "واجهة الاستنباط": "artistic_inference_interface.py"
        }
        
        available = {}
        for name, filename in components.items():
            available[name] = os.path.exists(filename)
        
        return available
    
    def show_main_menu(self):
        """عرض القائمة الرئيسية"""
        while True:
            print(f"\n" + "="*60)
            print(f"🌟 نظام بصيرة الثوري - القائمة الرئيسية")
            print(f"="*60)
            
            print(f"\n🚀 خيارات التشغيل:")
            print(f"   1️⃣  تشغيل واجهة سطر الأوامر (CLI)")
            print(f"   2️⃣  تشغيل واجهة Gradio التفاعلية")
            print(f"   3️⃣  تشغيل واجهة API")
            print(f"   4️⃣  تشغيل الواجهة الفنية التفاعلية")
            
            print(f"\n🧪 اختبار المكونات:")
            print(f"   5️⃣  تشغيل الاختبارات الشاملة")
            print(f"   6️⃣  اختبار المعادلة الأم الثورية")
            print(f"   7️⃣  اختبار النواة التفكيرية")
            print(f"   8️⃣  اختبار المكونات الرياضية")
            
            print(f"\n🎨 الوحدات الفنية:")
            print(f"   9️⃣  تشغيل الوحدة الفنية للنشر")
            print(f"   🔟 تشغيل وحدة الاستنباط الفني")
            
            print(f"\n📊 معلومات النظام:")
            print(f"   11 عرض حالة المكونات")
            print(f"   12 عرض معلومات النظام")
            print(f"   13 عرض النظريات الثورية")
            
            print(f"\n❌ خروج:")
            print(f"   0️⃣  الخروج من النظام")
            
            print(f"\n" + "="*60)
            
            try:
                choice = input(f"🎯 اختر رقم الخيار: ").strip()
                
                if choice == "0":
                    print(f"👋 شكراً لاستخدام نظام بصيرة الثوري!")
                    print(f"🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله")
                    break
                elif choice == "1":
                    self._launch_cli_interface()
                elif choice == "2":
                    self._launch_gradio_interface()
                elif choice == "3":
                    self._launch_api_interface()
                elif choice == "4":
                    self._launch_artistic_interface()
                elif choice == "5":
                    self._run_comprehensive_tests()
                elif choice == "6":
                    self._test_component("revolutionary_mother_equation.py")
                elif choice == "7":
                    self._test_component("complete_multi_layer_thinking_core.py")
                elif choice == "8":
                    self._test_component("advanced_mathematical_components.py")
                elif choice == "9":
                    self._test_component("artistic_publishing_unit.py")
                elif choice == "10":
                    self._launch_inference_interface()
                elif choice == "11":
                    self._show_component_status()
                elif choice == "12":
                    self._show_system_info()
                elif choice == "13":
                    self._show_revolutionary_theories()
                else:
                    print(f"❌ خيار غير صحيح. يرجى اختيار رقم من 0 إلى 13")
                    
            except KeyboardInterrupt:
                print(f"\n\n⚠️ تم إيقاف التشغيل بواسطة المستخدم")
                break
            except Exception as e:
                print(f"❌ خطأ: {e}")
    
    def _launch_cli_interface(self):
        """تشغيل واجهة سطر الأوامر"""
        if not self.available_components.get("واجهات المستخدم", False):
            print(f"❌ واجهات المستخدم غير متاحة")
            return
        
        print(f"🖥️ تشغيل واجهة سطر الأوامر...")
        try:
            subprocess.run([sys.executable, "multi_user_interfaces.py", "--interface", "cli"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل واجهة CLI: {e}")
    
    def _launch_gradio_interface(self):
        """تشغيل واجهة Gradio"""
        if not self.available_components.get("واجهات المستخدم", False):
            print(f"❌ واجهات المستخدم غير متاحة")
            return
        
        print(f"🎨 تشغيل واجهة Gradio التفاعلية...")
        try:
            subprocess.run([sys.executable, "multi_user_interfaces.py", "--interface", "gradio"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل واجهة Gradio: {e}")
    
    def _launch_api_interface(self):
        """تشغيل واجهة API"""
        if not self.available_components.get("واجهات المستخدم", False):
            print(f"❌ واجهات المستخدم غير متاحة")
            return
        
        print(f"🚀 تشغيل واجهة API...")
        try:
            subprocess.run([sys.executable, "multi_user_interfaces.py", "--interface", "api"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل واجهة API: {e}")
    
    def _launch_artistic_interface(self):
        """تشغيل الواجهة الفنية"""
        if not self.available_components.get("الوحدة الفنية للنشر", False):
            print(f"❌ الوحدة الفنية غير متاحة")
            return
        
        print(f"🎨 تشغيل الواجهة الفنية التفاعلية...")
        try:
            subprocess.run([sys.executable, "artistic_publishing_unit.py"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل الواجهة الفنية: {e}")
    
    def _launch_inference_interface(self):
        """تشغيل واجهة الاستنباط"""
        if not self.available_components.get("واجهة الاستنباط", False):
            print(f"❌ واجهة الاستنباط غير متاحة")
            return
        
        print(f"👁️ تشغيل واجهة الاستنباط التفاعلية...")
        try:
            subprocess.run([sys.executable, "artistic_inference_interface.py"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل واجهة الاستنباط: {e}")
    
    def _run_comprehensive_tests(self):
        """تشغيل الاختبارات الشاملة"""
        if not self.available_components.get("نظام الاختبار", False):
            print(f"❌ نظام الاختبار غير متاح")
            return
        
        print(f"🧪 تشغيل الاختبارات الشاملة...")
        print(f"⏳ قد يستغرق هذا بضع دقائق...")
        try:
            subprocess.run([sys.executable, "comprehensive_testing_system.py"])
        except Exception as e:
            print(f"❌ خطأ في تشغيل الاختبارات: {e}")
    
    def _test_component(self, filename: str):
        """اختبار مكون محدد"""
        if not os.path.exists(filename):
            print(f"❌ الملف غير موجود: {filename}")
            return
        
        print(f"🧪 اختبار المكون: {filename}")
        try:
            result = subprocess.run([sys.executable, filename], 
                                  capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print(f"✅ نجح الاختبار!")
                if result.stdout:
                    print(f"📊 النتيجة:")
                    print(result.stdout[:500] + "..." if len(result.stdout) > 500 else result.stdout)
            else:
                print(f"❌ فشل الاختبار!")
                if result.stderr:
                    print(f"🔍 الخطأ:")
                    print(result.stderr[:300] + "..." if len(result.stderr) > 300 else result.stderr)
        
        except subprocess.TimeoutExpired:
            print(f"⏰ انتهت مهلة الاختبار (60 ثانية)")
        except Exception as e:
            print(f"❌ خطأ في الاختبار: {e}")
    
    def _show_component_status(self):
        """عرض حالة المكونات"""
        print(f"\n📊 حالة مكونات النظام:")
        print(f"="*50)
        
        for name, available in self.available_components.items():
            status = "✅ متاح" if available else "❌ غير متاح"
            print(f"   {status} {name}")
        
        available_count = sum(1 for available in self.available_components.values() if available)
        total_count = len(self.available_components)
        
        print(f"\n📈 الملخص:")
        print(f"   📊 المكونات المتاحة: {available_count}/{total_count}")
        print(f"   📊 نسبة الاكتمال: {available_count/total_count*100:.1f}%")
    
    def _show_system_info(self):
        """عرض معلومات النظام"""
        print(f"\n🌟 معلومات نظام بصيرة الثوري:")
        print(f"="*50)
        
        print(f"🧬 المطور: باسل يحيى عبدالله")
        print(f"📅 تاريخ الإنشاء: {self.creation_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🐍 إصدار Python: {sys.version.split()[0]}")
        print(f"💻 نظام التشغيل: {os.name}")
        print(f"📁 المجلد الحالي: {os.getcwd()}")
        
        # حساب حجم الملفات
        total_size = 0
        file_count = 0
        for filename in os.listdir('.'):
            if filename.endswith('.py'):
                try:
                    size = os.path.getsize(filename)
                    total_size += size
                    file_count += 1
                except:
                    pass
        
        print(f"📊 عدد ملفات Python: {file_count}")
        print(f"📊 الحجم الإجمالي: {total_size/1024:.1f} KB")
        
        print(f"\n🎯 الميزات الرئيسية:")
        print(f"   🧮 رياضيات نقية بدون مكتبات AI تقليدية")
        print(f"   🧬 تطبيق 3 نظريات ثورية مبتكرة")
        print(f"   🖥️ 4 واجهات مستخدم متعددة")
        print(f"   🧪 نظام اختبار شامل")
        print(f"   🎨 وحدات فنية متقدمة")
    
    def _show_revolutionary_theories(self):
        """عرض النظريات الثورية"""
        print(f"\n🧬 النظريات الثورية الثلاث:")
        print(f"="*50)
        
        print(f"\n1️⃣ نظرية ثنائية الصفر (Zero Duality Theory)")
        print(f"   🎯 تحقيق التوازن المثالي في الأنظمة الرياضية")
        print(f"   ⚖️ ضمان الاستقرار والدقة في الحسابات المعقدة")
        print(f"   🔄 تطبيق مبدأ الثنائية الصفرية في جميع العمليات")
        
        print(f"\n2️⃣ نظرية تعامد الأضداد (Perpendicular Opposites Theory)")
        print(f"   📐 تطبيق مبدأ التعامد الرياضي على الأضداد")
        print(f"   🌈 تحقيق التنوع والشمولية في التحليل")
        print(f"   🔍 ضمان تغطية جميع الجوانب المختلفة للمشكلة")
        
        print(f"\n3️⃣ نظرية الفتائل (Filament Theory)")
        print(f"   🕸️ وصف الترابط المعقد بين العناصر المختلفة")
        print(f"   💪 تقوية البنية الكلية للنظام من خلال الترابط")
        print(f"   🤝 تحقيق التماسك والتكامل في النظام")
        
        print(f"\n🌟 جميع النظريات من إبداع باسل يحيى عبدالله")

def main():
    """الدالة الرئيسية"""
    try:
        launcher = BaseraSystemLauncher()
        launcher.show_main_menu()
    except KeyboardInterrupt:
        print(f"\n👋 تم إنهاء البرنامج بواسطة المستخدم")
    except Exception as e:
        print(f"❌ خطأ عام: {e}")

if __name__ == "__main__":
    main()

