#!/usr/bin/env python3
"""
واجهات المستخدم المتعددة - Multi-User Interfaces
نظام بصيرة المتكامل

🖥️ واجهات متعددة للتفاعل مع النظام
📱 CLI, API, Web interfaces
🎯 تجربة مستخدم متكاملة

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import os
import sys
import json
import time
import threading
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import argparse
from datetime import datetime

# إضافة مسار المكونات
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from revolutionary_mother_equation import RevolutionaryMotherEquation
    from complete_multi_layer_thinking_core import CompleteMultiLayerThinkingCore
    from complete_specialized_databases import CompleteSpecializedDatabases
    from adaptive_revolutionary_equations_fixed import AdaptiveRevolutionaryEquations
    from expert_explorer_system import ExpertExplorerSystem
    from revolutionary_intelligent_agent import RevolutionaryIntelligentAgent
    from artistic_publishing_unit import ArtisticPublishingUnit
    from specialized_knowledge_systems import SpecializedKnowledgeSystem
    from advanced_mathematical_components import AdvancedMathematicalComponents
except ImportError as e:
    print(f"⚠️ تحذير: لم يتم العثور على بعض المكونات: {e}")
    print("   سيتم تشغيل الواجهات بدون هذه المكونات")

class InterfaceType(Enum):
    """أنواع الواجهات"""
    CLI = "cli"
    API = "api"
    WEB = "web"
    GRADIO = "gradio"

class UserRole(Enum):
    """أدوار المستخدمين"""
    GUEST = "guest"
    USER = "user"
    DEVELOPER = "developer"
    ADMIN = "admin"
    RESEARCHER = "researcher"

@dataclass
class UserSession:
    """جلسة المستخدم"""
    session_id: str
    user_role: UserRole
    start_time: datetime
    last_activity: datetime
    commands_executed: int = 0
    interface_type: InterfaceType = InterfaceType.CLI
    preferences: Dict[str, Any] = field(default_factory=dict)

class BaseraMultiInterface:
    """
    واجهات المستخدم المتعددة لنظام بصيرة
    
    🖥️ نظام واجهات متكامل يدعم:
    - واجهة سطر الأوامر (CLI)
    - واجهة برمجة التطبيقات (API)
    - واجهة الويب (Web)
    - واجهة Gradio التفاعلية
    """
    
    def __init__(self):
        self.creation_time = datetime.now()
        self.active_sessions: Dict[str, UserSession] = {}
        self.command_history: List[Dict[str, Any]] = []
        
        # تهيئة المكونات الأساسية
        self._initialize_components()
        
        # إعدادات الواجهات
        self.interface_settings = {
            InterfaceType.CLI: {"prompt": "بصيرة> ", "colors": True, "history": True},
            InterfaceType.API: {"port": 8000, "host": "0.0.0.0", "docs": True},
            InterfaceType.WEB: {"port": 8080, "host": "0.0.0.0", "debug": False},
            InterfaceType.GRADIO: {"port": 7860, "share": False, "auth": None}
        }
        
        print(f"🖥️⚡ تم إنشاء واجهات المستخدم المتعددة")
        print(f"   🕐 وقت الإنشاء: {self.creation_time}")
        print(f"   🔧 المكونات المتاحة: {len(self.available_components)}")
    
    def _initialize_components(self):
        """تهيئة المكونات الأساسية"""
        self.available_components = {}
        
        try:
            self.available_components['mother_equation'] = RevolutionaryMotherEquation()
            print("✅ تم تحميل المعادلة الأم الثورية")
        except:
            print("❌ فشل تحميل المعادلة الأم الثورية")
        
        try:
            self.available_components['thinking_core'] = CompleteMultiLayerThinkingCore()
            print("✅ تم تحميل النواة التفكيرية")
        except:
            print("❌ فشل تحميل النواة التفكيرية")
        
        try:
            self.available_components['databases'] = CompleteSpecializedDatabases()
            print("✅ تم تحميل قواعد البيانات المتخصصة")
        except:
            print("❌ فشل تحميل قواعد البيانات المتخصصة")
        
        try:
            self.available_components['adaptive_equations'] = AdaptiveRevolutionaryEquations()
            print("✅ تم تحميل المعادلات المتكيفة")
        except:
            print("❌ فشل تحميل المعادلات المتكيفة")
        
        try:
            self.available_components['expert_explorer'] = ExpertExplorerSystem()
            print("✅ تم تحميل نظام الخبير/المستكشف")
        except:
            print("❌ فشل تحميل نظام الخبير/المستكشف")
        
        try:
            self.available_components['intelligent_agent'] = RevolutionaryIntelligentAgent()
            print("✅ تم تحميل الوكيل الذكي")
        except:
            print("❌ فشل تحميل الوكيل الذكي")
        
        try:
            self.available_components['publishing_unit'] = ArtisticPublishingUnit()
            print("✅ تم تحميل وحدة النشر الفني")
        except:
            print("❌ فشل تحميل وحدة النشر الفني")
        
        try:
            self.available_components['knowledge_system'] = SpecializedKnowledgeSystem()
            print("✅ تم تحميل نظام المعرفة")
        except:
            print("❌ فشل تحميل نظام المعرفة")
        
        try:
            self.available_components['math_components'] = AdvancedMathematicalComponents()
            print("✅ تم تحميل المكونات الرياضية")
        except:
            print("❌ فشل تحميل المكونات الرياضية")
    
    def create_session(self, user_role: UserRole = UserRole.USER, 
                      interface_type: InterfaceType = InterfaceType.CLI) -> str:
        """إنشاء جلسة مستخدم جديدة"""
        session_id = f"session_{int(time.time())}_{len(self.active_sessions)}"
        
        session = UserSession(
            session_id=session_id,
            user_role=user_role,
            start_time=datetime.now(),
            last_activity=datetime.now(),
            interface_type=interface_type
        )
        
        self.active_sessions[session_id] = session
        
        print(f"🆔 تم إنشاء جلسة جديدة: {session_id}")
        print(f"   👤 دور المستخدم: {user_role.value}")
        print(f"   🖥️ نوع الواجهة: {interface_type.value}")
        
        return session_id
    
    def run_cli_interface(self, session_id: str = None):
        """تشغيل واجهة سطر الأوامر"""
        if session_id is None:
            session_id = self.create_session(UserRole.USER, InterfaceType.CLI)
        
        session = self.active_sessions.get(session_id)
        if not session:
            print("❌ جلسة غير صالحة")
            return
        
        print(f"\n🌟 مرحباً بك في نظام بصيرة الثوري!")
        print(f"📋 الجلسة: {session_id}")
        print(f"👤 الدور: {session.user_role.value}")
        print(f"🕐 الوقت: {session.start_time}")
        print(f"\n💡 اكتب 'help' للمساعدة أو 'exit' للخروج")
        
        while True:
            try:
                # تحديث آخر نشاط
                session.last_activity = datetime.now()
                
                # عرض المطالبة
                prompt = self.interface_settings[InterfaceType.CLI]["prompt"]
                command = input(f"\n{prompt}").strip()
                
                if not command:
                    continue
                
                # معالجة الأوامر الخاصة
                if command.lower() in ['exit', 'quit', 'خروج']:
                    print("👋 وداعاً! شكراً لاستخدام نظام بصيرة")
                    break
                elif command.lower() in ['help', 'مساعدة']:
                    self._show_cli_help()
                    continue
                elif command.lower() in ['status', 'حالة']:
                    self._show_system_status(session_id)
                    continue
                elif command.lower() in ['components', 'مكونات']:
                    self._show_available_components()
                    continue
                
                # تنفيذ الأوامر
                result = self._execute_command(command, session_id)
                
                # عرض النتيجة
                if result:
                    print(f"\n📊 النتيجة:")
                    if isinstance(result, dict):
                        for key, value in result.items():
                            print(f"   {key}: {value}")
                    else:
                        print(f"   {result}")
                
                session.commands_executed += 1
                
            except KeyboardInterrupt:
                print("\n\n⚠️ تم إيقاف التشغيل بواسطة المستخدم")
                break
            except Exception as e:
                print(f"\n❌ خطأ: {e}")
    
    def _show_cli_help(self):
        """عرض مساعدة واجهة سطر الأوامر"""
        help_text = """
🌟 أوامر نظام بصيرة الثوري:

📋 الأوامر العامة:
   help, مساعدة     - عرض هذه المساعدة
   status, حالة      - عرض حالة النظام
   components, مكونات - عرض المكونات المتاحة
   exit, quit, خروج  - الخروج من النظام

🧮 الأوامر الرياضية:
   sigmoid <x>       - حساب السيجمويد الثوري
   linear <x>        - حساب الدالة الخطية الثورية
   general <x>       - حساب معادلة الشكل العام
   derivative <x>    - حساب المشتقة العددية
   integral <a> <b>  - حساب التكامل العددي

🧠 أوامر التفكير:
   think <text>      - تشغيل النواة التفكيرية
   analyze <text>    - تحليل النص
   learn <text>      - تعلم معلومات جديدة

🎨 أوامر فنية:
   draw <shape>      - رسم شكل هندسي
   publish <text>    - إنشاء منشور فني
   design <type>     - تصميم فني

📚 أوامر المعرفة:
   search <query>    - البحث في المعرفة
   add_knowledge <title> <content> - إضافة معرفة جديدة
   
🤖 أوامر الوكيل الذكي:
   agent <task>      - تكليف الوكيل الذكي
   explore <domain>  - استكشاف مجال معين
        """
        print(help_text)
    
    def _show_system_status(self, session_id: str):
        """عرض حالة النظام"""
        session = self.active_sessions.get(session_id)
        
        print(f"\n📊 حالة نظام بصيرة:")
        print(f"   🆔 الجلسة: {session_id}")
        print(f"   👤 الدور: {session.user_role.value}")
        print(f"   🕐 بداية الجلسة: {session.start_time}")
        print(f"   ⏰ آخر نشاط: {session.last_activity}")
        print(f"   📈 الأوامر المنفذة: {session.commands_executed}")
        print(f"   🔧 المكونات المتاحة: {len(self.available_components)}")
        print(f"   📋 الجلسات النشطة: {len(self.active_sessions)}")
        print(f"   📚 سجل الأوامر: {len(self.command_history)}")
    
    def _show_available_components(self):
        """عرض المكونات المتاحة"""
        print(f"\n🔧 المكونات المتاحة في النظام:")
        
        for name, component in self.available_components.items():
            status = "✅ متاح" if component else "❌ غير متاح"
            component_type = type(component).__name__ if component else "غير محدد"
            print(f"   {status} {name}: {component_type}")
        
        if not self.available_components:
            print("   ⚠️ لا توجد مكونات متاحة حالياً")
    
    def _execute_command(self, command: str, session_id: str) -> Any:
        """تنفيذ الأوامر"""
        parts = command.split()
        if not parts:
            return None
        
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # تسجيل الأمر
        self.command_history.append({
            "session_id": session_id,
            "command": command,
            "timestamp": datetime.now(),
            "args": args
        })
        
        try:
            # الأوامر الرياضية
            if cmd == "sigmoid" and args:
                if 'math_components' in self.available_components:
                    x = float(args[0])
                    result = self.available_components['math_components'].revolutionary_sigmoid(x)
                    return {"sigmoid_value": result.value, "precision": result.precision}
                else:
                    return "❌ المكونات الرياضية غير متاحة"
            
            elif cmd == "linear" and args:
                if 'math_components' in self.available_components:
                    x = float(args[0])
                    result = self.available_components['math_components'].revolutionary_linear(x)
                    return {"linear_value": result.value, "precision": result.precision}
                else:
                    return "❌ المكونات الرياضية غير متاحة"
            
            elif cmd == "general" and args:
                if 'math_components' in self.available_components:
                    x = float(args[0])
                    result = self.available_components['math_components'].revolutionary_general_form(x)
                    return {"general_value": result.value, "precision": result.precision}
                else:
                    return "❌ المكونات الرياضية غير متاحة"
            
            # أوامر التفكير
            elif cmd == "think" and args:
                if 'thinking_core' in self.available_components:
                    text = " ".join(args)
                    result = self.available_components['thinking_core'].process_comprehensive_thinking(text)
                    return {"thinking_result": "تم التفكير بنجاح", "layers_processed": len(result)}
                else:
                    return "❌ النواة التفكيرية غير متاحة"
            
            # أوامر المعرفة
            elif cmd == "search" and args:
                if 'knowledge_system' in self.available_components:
                    query = " ".join(args)
                    results = self.available_components['knowledge_system'].search_knowledge(query)
                    return {"search_results": len(results), "query": query}
                else:
                    return "❌ نظام المعرفة غير متاح"
            
            # أوامر الوكيل الذكي
            elif cmd == "agent" and args:
                if 'intelligent_agent' in self.available_components:
                    task = " ".join(args)
                    result = self.available_components['intelligent_agent'].execute_task(task)
                    return {"agent_result": "تم تنفيذ المهمة", "task": task}
                else:
                    return "❌ الوكيل الذكي غير متاح"
            
            # أوامر فنية
            elif cmd == "draw" and args:
                if 'publishing_unit' in self.available_components:
                    shape = args[0]
                    result = self.available_components['publishing_unit'].create_artistic_shape(shape)
                    return {"drawing_result": "تم الرسم بنجاح", "shape": shape}
                else:
                    return "❌ وحدة النشر الفني غير متاحة"
            
            else:
                return f"❌ أمر غير معروف: {cmd}. اكتب 'help' للمساعدة"
        
        except ValueError as e:
            return f"❌ خطأ في القيم: {e}"
        except Exception as e:
            return f"❌ خطأ في التنفيذ: {e}"
    
    def run_api_interface(self):
        """تشغيل واجهة API"""
        try:
            from fastapi import FastAPI, HTTPException
            from fastapi.responses import JSONResponse
            import uvicorn
            
            app = FastAPI(
                title="Basera AI Revolutionary System API",
                description="واجهة برمجة التطبيقات لنظام بصيرة الثوري",
                version="1.0.0"
            )
            
            @app.get("/")
            async def root():
                return {"message": "مرحباً بك في نظام بصيرة الثوري", "status": "active"}
            
            @app.get("/status")
            async def get_status():
                return {
                    "system": "Basera Revolutionary AI",
                    "components": len(self.available_components),
                    "active_sessions": len(self.active_sessions),
                    "uptime": str(datetime.now() - self.creation_time)
                }
            
            @app.post("/execute")
            async def execute_command(command: str, session_id: str = None):
                if session_id is None:
                    session_id = self.create_session(UserRole.USER, InterfaceType.API)
                
                result = self._execute_command(command, session_id)
                return {"result": result, "session_id": session_id}
            
            settings = self.interface_settings[InterfaceType.API]
            print(f"🚀 تشغيل واجهة API على http://{settings['host']}:{settings['port']}")
            
            uvicorn.run(app, host=settings['host'], port=settings['port'])
            
        except ImportError:
            print("❌ FastAPI غير متاح. يرجى تثبيته: pip install fastapi uvicorn")
    
    def run_gradio_interface(self):
        """تشغيل واجهة Gradio التفاعلية"""
        try:
            import gradio as gr
            
            def process_command(command, session_id=None):
                if session_id is None or session_id not in self.active_sessions:
                    session_id = self.create_session(UserRole.USER, InterfaceType.GRADIO)
                
                result = self._execute_command(command, session_id)
                return str(result), session_id
            
            def get_system_info():
                return f"""
🌟 نظام بصيرة الثوري
📊 المكونات المتاحة: {len(self.available_components)}
📋 الجلسات النشطة: {len(self.active_sessions)}
🕐 وقت التشغيل: {datetime.now() - self.creation_time}
                """
            
            with gr.Blocks(title="نظام بصيرة الثوري") as interface:
                gr.Markdown("# 🌟 نظام بصيرة الثوري - الواجهة التفاعلية")
                
                with gr.Tab("تنفيذ الأوامر"):
                    command_input = gr.Textbox(label="الأمر", placeholder="اكتب أمرك هنا...")
                    session_input = gr.Textbox(label="معرف الجلسة (اختياري)", placeholder="session_id")
                    execute_btn = gr.Button("تنفيذ")
                    
                    result_output = gr.Textbox(label="النتيجة", interactive=False)
                    session_output = gr.Textbox(label="معرف الجلسة", interactive=False)
                    
                    execute_btn.click(
                        process_command,
                        inputs=[command_input, session_input],
                        outputs=[result_output, session_output]
                    )
                
                with gr.Tab("معلومات النظام"):
                    info_btn = gr.Button("تحديث المعلومات")
                    info_output = gr.Textbox(label="معلومات النظام", interactive=False)
                    
                    info_btn.click(get_system_info, outputs=info_output)
                
                with gr.Tab("المساعدة"):
                    gr.Markdown("""
## 🌟 أوامر نظام بصيرة الثوري:

### 📋 الأوامر العامة:
- `status` - عرض حالة النظام
- `components` - عرض المكونات المتاحة

### 🧮 الأوامر الرياضية:
- `sigmoid <x>` - حساب السيجمويد الثوري
- `linear <x>` - حساب الدالة الخطية الثورية
- `general <x>` - حساب معادلة الشكل العام

### 🧠 أوامر التفكير:
- `think <text>` - تشغيل النواة التفكيرية
- `analyze <text>` - تحليل النص

### 📚 أوامر المعرفة:
- `search <query>` - البحث في المعرفة

### 🤖 أوامر الوكيل الذكي:
- `agent <task>` - تكليف الوكيل الذكي

### 🎨 أوامر فنية:
- `draw <shape>` - رسم شكل هندسي
                    """)
            
            settings = self.interface_settings[InterfaceType.GRADIO]
            print(f"🎨 تشغيل واجهة Gradio على المنفذ {settings['port']}")
            
            interface.launch(
                server_port=settings['port'],
                share=settings['share'],
                auth=settings['auth']
            )
            
        except ImportError:
            print("❌ Gradio غير متاح. يرجى تثبيته: pip install gradio")
    
    def get_interface_statistics(self) -> Dict[str, Any]:
        """الحصول على إحصائيات الواجهات"""
        return {
            "creation_time": self.creation_time.isoformat(),
            "active_sessions": len(self.active_sessions),
            "total_commands": len(self.command_history),
            "available_components": len(self.available_components),
            "interface_settings": {k.value: v for k, v in self.interface_settings.items()},
            "session_details": {
                sid: {
                    "user_role": session.user_role.value,
                    "interface_type": session.interface_type.value,
                    "commands_executed": session.commands_executed,
                    "duration": str(datetime.now() - session.start_time)
                }
                for sid, session in self.active_sessions.items()
            }
        }

# ==================== اختبار الواجهات ====================

def test_multi_interfaces():
    """اختبار واجهات المستخدم المتعددة"""
    print("🖥️ اختبار واجهات المستخدم المتعددة")
    print("="*60)
    
    # إنشاء نظام الواجهات
    interface_system = BaseraMultiInterface()
    
    # إنشاء جلسة اختبار
    session_id = interface_system.create_session(UserRole.DEVELOPER, InterfaceType.CLI)
    
    # اختبار تنفيذ الأوامر
    test_commands = [
        "status",
        "components", 
        "sigmoid 1.0",
        "linear 2.0",
        "help"
    ]
    
    print(f"\n🧪 اختبار تنفيذ الأوامر:")
    for cmd in test_commands:
        print(f"\n📝 تنفيذ: {cmd}")
        result = interface_system._execute_command(cmd, session_id)
        print(f"   📊 النتيجة: {result}")
    
    # عرض الإحصائيات
    print(f"\n📊 إحصائيات الواجهات:")
    stats = interface_system.get_interface_statistics()
    print(f"   📈 الجلسات النشطة: {stats['active_sessions']}")
    print(f"   📋 إجمالي الأوامر: {stats['total_commands']}")
    print(f"   🔧 المكونات المتاحة: {stats['available_components']}")
    
    print(f"\n✅ انتهى اختبار واجهات المستخدم المتعددة!")
    return interface_system

def main():
    """الدالة الرئيسية"""
    parser = argparse.ArgumentParser(description="نظام بصيرة الثوري - واجهات المستخدم المتعددة")
    parser.add_argument("--interface", "-i", choices=["cli", "api", "web", "gradio"], 
                       default="cli", help="نوع الواجهة")
    parser.add_argument("--test", "-t", action="store_true", help="تشغيل الاختبارات")
    
    args = parser.parse_args()
    
    if args.test:
        test_multi_interfaces()
        return
    
    # إنشاء نظام الواجهات
    interface_system = BaseraMultiInterface()
    
    # تشغيل الواجهة المطلوبة
    if args.interface == "cli":
        interface_system.run_cli_interface()
    elif args.interface == "api":
        interface_system.run_api_interface()
    elif args.interface == "gradio":
        interface_system.run_gradio_interface()
    else:
        print(f"❌ واجهة غير مدعومة: {args.interface}")

if __name__ == "__main__":
    main()

