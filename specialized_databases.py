"""
نظام قواعد البيانات المتخصصة لطبقات النواة التفكيرية
Specialized Database System for Thinking Core Layers

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله

نظام قواعد بيانات ثوري يدعم التعلم المستمر لكل طبقة تفكير
"""

import sqlite3
import json
import numpy as np
from datetime import datetime
from typing import Dict, List, Any, Optional, Union, Tuple
from abc import ABC, abstractmethod
from enum import Enum
import uuid
import os
from pathlib import Path

from multi_layer_thinking_core import ThinkingLayerType

class DatabaseType(Enum):
    """أنواع قواعد البيانات المتخصصة."""
    MATHEMATICAL_DB = "mathematical_knowledge"
    LOGICAL_DB = "logical_patterns"
    INTERPRETIVE_DB = "interpretive_meanings"
    PHYSICAL_DB = "physical_laws"
    LINGUISTIC_DB = "linguistic_knowledge"
    SYMBOLIC_DB = "symbolic_representations"
    VISUAL_DB = "visual_patterns"
    SEMANTIC_DB = "semantic_networks"

class LearningSource(Enum):
    """مصادر التعلم المختلفة."""
    USER_INTERACTION = "user_interaction"
    INTERNET_RESEARCH = "internet_research"
    SELF_ANALYSIS = "self_analysis"
    PATTERN_DISCOVERY = "pattern_discovery"
    ERROR_CORRECTION = "error_correction"
    CROSS_LAYER_LEARNING = "cross_layer_learning"

class BaseSpecializedDatabase(ABC):
    """
    قاعدة البيانات المتخصصة الأساسية
    كل طبقة تفكير لها قاعدة بيانات متخصصة ترث من هذه الفئة
    """
    
    def __init__(self, db_name: str, layer_type: ThinkingLayerType):
        self.db_name = db_name
        self.layer_type = layer_type
        self.db_path = f"databases/{db_name}.db"
        
        # إنشاء مجلد قواعد البيانات
        os.makedirs("databases", exist_ok=True)
        
        # الاتصال بقاعدة البيانات
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.connection.cursor()
        
        # إحصائيات التعلم
        self.learning_sessions = 0
        self.total_entries = 0
        self.last_update = None
        
        # تهيئة الجداول
        self._initialize_tables()
        
        print(f"🗄️ تم إنشاء قاعدة بيانات متخصصة: {db_name} للطبقة {layer_type.value}")
    
    @abstractmethod
    def _initialize_tables(self):
        """تهيئة الجداول المتخصصة لكل نوع قاعدة بيانات."""
        pass
    
    @abstractmethod
    def store_learning(self, data: Any, source: LearningSource, metadata: Dict[str, Any] = None):
        """حفظ التعلم الجديد."""
        pass
    
    @abstractmethod
    def retrieve_knowledge(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """استرجاع المعرفة."""
        pass
    
    def _create_base_tables(self):
        """إنشاء الجداول الأساسية المشتركة."""
        
        # جدول التعلم العام
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS learning_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE,
                timestamp TEXT,
                source TEXT,
                data_type TEXT,
                success BOOLEAN,
                metadata TEXT
            )
        ''')
        
        # جدول الأنماط المكتشفة
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS discovered_patterns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pattern_id TEXT UNIQUE,
                pattern_type TEXT,
                pattern_data TEXT,
                confidence REAL,
                discovery_date TEXT,
                usage_count INTEGER DEFAULT 0
            )
        ''')
        
        # جدول الأخطاء والتصحيحات
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS error_corrections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                error_id TEXT UNIQUE,
                error_type TEXT,
                error_data TEXT,
                correction_data TEXT,
                correction_date TEXT,
                effectiveness REAL
            )
        ''')
        
        self.connection.commit()
    
    def log_learning_session(self, session_id: str, source: LearningSource, 
                           data_type: str, success: bool, metadata: Dict[str, Any] = None):
        """تسجيل جلسة تعلم."""
        
        self.cursor.execute('''
            INSERT OR REPLACE INTO learning_sessions 
            (session_id, timestamp, source, data_type, success, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            session_id,
            datetime.now().isoformat(),
            source.value,
            data_type,
            success,
            json.dumps(metadata or {})
        ))
        
        self.connection.commit()
        self.learning_sessions += 1
        self.last_update = datetime.now()
    
    def store_pattern(self, pattern_id: str, pattern_type: str, 
                     pattern_data: Any, confidence: float):
        """حفظ نمط مكتشف."""
        
        self.cursor.execute('''
            INSERT OR REPLACE INTO discovered_patterns 
            (pattern_id, pattern_type, pattern_data, confidence, discovery_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            pattern_id,
            pattern_type,
            json.dumps(pattern_data),
            confidence,
            datetime.now().isoformat()
        ))
        
        self.connection.commit()
    
    def get_patterns_by_type(self, pattern_type: str) -> List[Dict[str, Any]]:
        """الحصول على أنماط حسب النوع."""
        
        self.cursor.execute('''
            SELECT * FROM discovered_patterns 
            WHERE pattern_type = ? 
            ORDER BY confidence DESC
        ''', (pattern_type,))
        
        results = []
        for row in self.cursor.fetchall():
            results.append({
                'pattern_id': row[1],
                'pattern_type': row[2],
                'pattern_data': json.loads(row[3]),
                'confidence': row[4],
                'discovery_date': row[5],
                'usage_count': row[6]
            })
        
        return results
    
    def get_database_stats(self) -> Dict[str, Any]:
        """إحصائيات قاعدة البيانات."""
        
        # عدد جلسات التعلم
        self.cursor.execute('SELECT COUNT(*) FROM learning_sessions')
        total_sessions = self.cursor.fetchone()[0]
        
        # عدد الأنماط
        self.cursor.execute('SELECT COUNT(*) FROM discovered_patterns')
        total_patterns = self.cursor.fetchone()[0]
        
        # عدد التصحيحات
        self.cursor.execute('SELECT COUNT(*) FROM error_corrections')
        total_corrections = self.cursor.fetchone()[0]
        
        # معدل النجاح
        self.cursor.execute('SELECT AVG(CAST(success AS REAL)) FROM learning_sessions')
        success_rate = self.cursor.fetchone()[0] or 0.0
        
        return {
            'database_name': self.db_name,
            'layer_type': self.layer_type.value,
            'total_learning_sessions': total_sessions,
            'total_patterns': total_patterns,
            'total_corrections': total_corrections,
            'success_rate': success_rate,
            'last_update': self.last_update.isoformat() if self.last_update else None,
            'database_size_mb': os.path.getsize(self.db_path) / (1024 * 1024)
        }
    
    def close(self):
        """إغلاق الاتصال بقاعدة البيانات."""
        self.connection.close()


class MathematicalDatabase(BaseSpecializedDatabase):
    """قاعدة بيانات متخصصة للطبقة الرياضية."""
    
    def __init__(self):
        super().__init__("mathematical_knowledge", ThinkingLayerType.MATHEMATICAL)
    
    def _initialize_tables(self):
        """تهيئة جداول الطبقة الرياضية."""
        self._create_base_tables()
        
        # جدول المعادلات
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS equations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equation_id TEXT UNIQUE,
                equation_type TEXT,
                equation_formula TEXT,
                parameters TEXT,
                domain TEXT,
                range_info TEXT,
                accuracy REAL,
                usage_count INTEGER DEFAULT 0,
                creation_date TEXT
            )
        ''')
        
        # جدول النماذج الرياضية
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mathematical_models (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model_id TEXT UNIQUE,
                model_name TEXT,
                model_type TEXT,
                input_variables TEXT,
                output_variables TEXT,
                model_data TEXT,
                performance_metrics TEXT,
                creation_date TEXT
            )
        ''')
        
        # جدول الثوابت الرياضية
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mathematical_constants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                constant_name TEXT UNIQUE,
                constant_value REAL,
                constant_description TEXT,
                precision_level INTEGER,
                source TEXT,
                verification_date TEXT
            )
        ''')
        
        # جدول النظريات المطبقة
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS applied_theories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                theory_id TEXT UNIQUE,
                theory_name TEXT,
                theory_type TEXT,
                application_context TEXT,
                results TEXT,
                effectiveness REAL,
                application_date TEXT
            )
        ''')
        
        self.connection.commit()
        
        # إدراج البيانات الأساسية
        self._insert_initial_data()
    
    def _insert_initial_data(self):
        """إدراج البيانات الرياضية الأساسية."""
        
        # الثوابت الرياضية الأساسية
        constants = [
            ("pi", np.pi, "النسبة بين محيط الدائرة وقطرها", 15, "mathematical_definition"),
            ("e", np.e, "أساس اللوغاريتم الطبيعي", 15, "mathematical_definition"),
            ("golden_ratio", 1.618033988749895, "النسبة الذهبية", 15, "mathematical_definition"),
            ("sqrt_2", np.sqrt(2), "الجذر التربيعي للعدد 2", 15, "mathematical_definition")
        ]
        
        for name, value, desc, precision, source in constants:
            self.cursor.execute('''
                INSERT OR IGNORE INTO mathematical_constants 
                (constant_name, constant_value, constant_description, precision_level, source, verification_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, value, desc, precision, source, datetime.now().isoformat()))
        
        # النظريات الثورية الأساسية
        theories = [
            ("zero_duality_theory", "نظرية ثنائية الصفر", "revolutionary", 
             "تطبيق رياضي", "انبثاق الأضداد من الصفر", 0.95),
            ("perpendicularity_theory", "نظرية التعامد", "revolutionary",
             "تطبيق رياضي", "تعامد الأضداد لمنع الفناء", 0.95),
            ("filament_theory", "نظرية الفتائل", "revolutionary",
             "تطبيق رياضي", "بناء التعقيد من الوحدات الأساسية", 0.95)
        ]
        
        for theory_id, name, theory_type, context, results, effectiveness in theories:
            self.cursor.execute('''
                INSERT OR IGNORE INTO applied_theories 
                (theory_id, theory_name, theory_type, application_context, results, effectiveness, application_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (theory_id, name, theory_type, context, results, effectiveness, datetime.now().isoformat()))
        
        self.connection.commit()
    
    def store_learning(self, data: Any, source: LearningSource, metadata: Dict[str, Any] = None):
        """حفظ التعلم الرياضي."""
        
        session_id = f"math_learning_{uuid.uuid4()}"
        
        try:
            if isinstance(data, dict):
                if 'equation' in data:
                    # حفظ معادلة جديدة
                    self._store_equation(data['equation'], metadata or {})
                elif 'model' in data:
                    # حفظ نموذج رياضي
                    self._store_mathematical_model(data['model'], metadata or {})
                elif 'constant' in data:
                    # حفظ ثابت رياضي
                    self._store_constant(data['constant'], metadata or {})
            
            # تسجيل جلسة التعلم
            self.log_learning_session(session_id, source, "mathematical_data", True, metadata)
            
            print(f"   ✅ تم حفظ التعلم الرياضي: {session_id}")
            
        except Exception as e:
            self.log_learning_session(session_id, source, "mathematical_data", False, 
                                    {**(metadata or {}), 'error': str(e)})
            print(f"   ❌ خطأ في حفظ التعلم الرياضي: {e}")
    
    def _store_equation(self, equation_data: Dict[str, Any], metadata: Dict[str, Any]):
        """حفظ معادلة رياضية."""
        
        equation_id = f"eq_{uuid.uuid4()}"
        
        self.cursor.execute('''
            INSERT INTO equations 
            (equation_id, equation_type, equation_formula, parameters, domain, range_info, accuracy, creation_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            equation_id,
            equation_data.get('type', 'unknown'),
            equation_data.get('formula', ''),
            json.dumps(equation_data.get('parameters', {})),
            equation_data.get('domain', 'real'),
            equation_data.get('range', 'real'),
            equation_data.get('accuracy', 0.0),
            datetime.now().isoformat()
        ))
        
        self.connection.commit()
    
    def _store_mathematical_model(self, model_data: Dict[str, Any], metadata: Dict[str, Any]):
        """حفظ نموذج رياضي."""
        
        model_id = f"model_{uuid.uuid4()}"
        
        self.cursor.execute('''
            INSERT INTO mathematical_models 
            (model_id, model_name, model_type, input_variables, output_variables, model_data, performance_metrics, creation_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            model_id,
            model_data.get('name', 'unnamed_model'),
            model_data.get('type', 'unknown'),
            json.dumps(model_data.get('inputs', [])),
            json.dumps(model_data.get('outputs', [])),
            json.dumps(model_data.get('data', {})),
            json.dumps(model_data.get('metrics', {})),
            datetime.now().isoformat()
        ))
        
        self.connection.commit()
    
    def _store_constant(self, constant_data: Dict[str, Any], metadata: Dict[str, Any]):
        """حفظ ثابت رياضي."""
        
        self.cursor.execute('''
            INSERT OR REPLACE INTO mathematical_constants 
            (constant_name, constant_value, constant_description, precision_level, source, verification_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            constant_data.get('name', 'unnamed_constant'),
            constant_data.get('value', 0.0),
            constant_data.get('description', ''),
            constant_data.get('precision', 10),
            constant_data.get('source', 'user_input'),
            datetime.now().isoformat()
        ))
        
        self.connection.commit()
    
    def retrieve_knowledge(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """استرجاع المعرفة الرياضية."""
        
        results = []
        
        # البحث في المعادلات
        self.cursor.execute('''
            SELECT * FROM equations 
            WHERE equation_type LIKE ? OR equation_formula LIKE ?
            ORDER BY accuracy DESC, usage_count DESC
            LIMIT ?
        ''', (f'%{query}%', f'%{query}%', limit))
        
        for row in self.cursor.fetchall():
            results.append({
                'type': 'equation',
                'equation_id': row[1],
                'equation_type': row[2],
                'formula': row[3],
                'parameters': json.loads(row[4]),
                'accuracy': row[6],
                'usage_count': row[7]
            })
        
        # البحث في الثوابت
        self.cursor.execute('''
            SELECT * FROM mathematical_constants 
            WHERE constant_name LIKE ? OR constant_description LIKE ?
            ORDER BY precision_level DESC
            LIMIT ?
        ''', (f'%{query}%', f'%{query}%', limit))
        
        for row in self.cursor.fetchall():
            results.append({
                'type': 'constant',
                'name': row[1],
                'value': row[2],
                'description': row[3],
                'precision': row[4]
            })
        
        return results[:limit]
    
    def get_best_equations(self, equation_type: str = None, limit: int = 5) -> List[Dict[str, Any]]:
        """الحصول على أفضل المعادلات."""
        
        if equation_type:
            self.cursor.execute('''
                SELECT * FROM equations 
                WHERE equation_type = ?
                ORDER BY accuracy DESC, usage_count DESC
                LIMIT ?
            ''', (equation_type, limit))
        else:
            self.cursor.execute('''
                SELECT * FROM equations 
                ORDER BY accuracy DESC, usage_count DESC
                LIMIT ?
            ''', (limit,))
        
        results = []
        for row in self.cursor.fetchall():
            results.append({
                'equation_id': row[1],
                'equation_type': row[2],
                'formula': row[3],
                'parameters': json.loads(row[4]),
                'accuracy': row[6],
                'usage_count': row[7]
            })
        
        return results


class LinguisticDatabase(BaseSpecializedDatabase):
    """قاعدة بيانات متخصصة للطبقة اللغوية."""
    
    def __init__(self):
        super().__init__("linguistic_knowledge", ThinkingLayerType.LINGUISTIC)
    
    def _initialize_tables(self):
        """تهيئة جداول الطبقة اللغوية."""
        self._create_base_tables()
        
        # جدول الكلمات والجذور
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS words_roots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT,
                root TEXT,
                pattern TEXT,
                word_type TEXT,
                meaning TEXT,
                semantic_weight REAL,
                frequency INTEGER DEFAULT 0,
                last_used TEXT
            )
        ''')
        
        # جدول دلالات الحروف
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS letter_semantics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                letter TEXT UNIQUE,
                semantic_meaning TEXT,
                phonetic_properties TEXT,
                symbolic_value REAL,
                usage_contexts TEXT,
                cultural_significance TEXT
            )
        ''')
        
        # جدول الأنماط اللغوية
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS linguistic_patterns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pattern_id TEXT UNIQUE,
                pattern_type TEXT,
                pattern_structure TEXT,
                examples TEXT,
                frequency REAL,
                effectiveness REAL,
                discovery_date TEXT
            )
        ''')
        
        # جدول التحليل الصرفي
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS morphological_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT,
                morphemes TEXT,
                grammatical_info TEXT,
                derivation_path TEXT,
                analysis_confidence REAL,
                analysis_date TEXT
            )
        ''')
        
        self.connection.commit()
        
        # إدراج البيانات الأساسية
        self._insert_initial_linguistic_data()
    
    def _insert_initial_linguistic_data(self):
        """إدراج البيانات اللغوية الأساسية."""
        
        # دلالات الحروف العربية الأساسية
        letter_meanings = [
            ('ا', 'البداية والوحدة والألف', 'صوت مفتوح', 1.0, 'بداية الكلمات', 'رمز الوحدة'),
            ('ب', 'البيت والاحتواء', 'صوت شفوي', 0.9, 'الأماكن والمفاهيم', 'رمز الاحتواء'),
            ('ت', 'التاء والأنوثة', 'صوت أسناني', 0.8, 'التأنيث والتفعيل', 'رمز الأنوثة'),
            ('ث', 'الثبات والاستقرار', 'صوت احتكاكي', 0.7, 'الثبات والدوام', 'رمز الاستقرار'),
            ('ج', 'الجمع والتجميع', 'صوت غاري', 0.8, 'الجمع والتجميع', 'رمز التجميع'),
            ('ح', 'الحياة والحركة', 'صوت حلقي', 0.9, 'الحياة والحركة', 'رمز الحياة'),
            ('خ', 'الخروج والانطلاق', 'صوت احتكاكي', 0.7, 'الخروج والحركة', 'رمز الانطلاق'),
            ('د', 'الدوام والاستمرار', 'صوت انفجاري', 0.8, 'الدوام والثبات', 'رمز الاستمرار'),
            ('ذ', 'الذكر والتذكير', 'صوت احتكاكي', 0.7, 'التذكير والذكر', 'رمز التذكير'),
            ('ر', 'الرحمة والرقة', 'صوت تكراري', 0.9, 'الرحمة والحنان', 'رمز الرحمة'),
            ('ز', 'الزينة والجمال', 'صوت احتكاكي', 0.8, 'الجمال والزينة', 'رمز الجمال'),
            ('س', 'السلام والسكينة', 'صوت صفيري', 0.9, 'السلام والهدوء', 'رمز السكينة'),
            ('ش', 'الشمول والانتشار', 'صوت صفيري', 0.8, 'الانتشار والشمول', 'رمز الشمول'),
            ('ص', 'الصفاء والنقاء', 'صوت مفخم', 0.9, 'النقاء والصفاء', 'رمز النقاء'),
            ('ض', 'الضوء والوضوح', 'صوت مفخم', 0.8, 'الوضوح والضوء', 'رمز الوضوح'),
            ('ط', 'الطهارة والنظافة', 'صوت مفخم', 0.8, 'الطهارة والنظافة', 'رمز الطهارة'),
            ('ظ', 'الظهور والبروز', 'صوت مفخم', 0.7, 'الظهور والبروز', 'رمز الظهور'),
            ('ع', 'العلم والمعرفة', 'صوت حلقي', 0.9, 'العلم والمعرفة', 'رمز المعرفة'),
            ('غ', 'الغموض والخفاء', 'صوت احتكاكي', 0.7, 'الغموض والخفاء', 'رمز الغموض'),
            ('ف', 'الفهم والإدراك', 'صوت شفوي', 0.8, 'الفهم والإدراك', 'رمز الفهم'),
            ('ق', 'القوة والشدة', 'صوت انفجاري', 0.9, 'القوة والشدة', 'رمز القوة'),
            ('ك', 'الكمال والتمام', 'صوت انفجاري', 0.8, 'الكمال والتمام', 'رمز الكمال'),
            ('ل', 'اللطف والرقة', 'صوت جانبي', 0.9, 'اللطف والرقة', 'رمز اللطف'),
            ('م', 'الماء والحياة', 'صوت أنفي', 0.9, 'الماء والحياة', 'رمز الحياة'),
            ('ن', 'النور والإضاءة', 'صوت أنفي', 0.9, 'النور والإضاءة', 'رمز النور'),
            ('ه', 'الهواء والنفس', 'صوت حلقي', 0.8, 'الهواء والتنفس', 'رمز النفس'),
            ('و', 'الوصل والربط', 'صوت شفوي', 0.9, 'الوصل والربط', 'رمز الوصل'),
            ('ي', 'اليد والعمل', 'صوت غاري', 0.8, 'العمل والفعل', 'رمز العمل')
        ]
        
        for letter, meaning, phonetic, value, context, significance in letter_meanings:
            self.cursor.execute('''
                INSERT OR IGNORE INTO letter_semantics 
                (letter, semantic_meaning, phonetic_properties, symbolic_value, usage_contexts, cultural_significance)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (letter, meaning, phonetic, value, context, significance))
        
        self.connection.commit()
    
    def store_learning(self, data: Any, source: LearningSource, metadata: Dict[str, Any] = None):
        """حفظ التعلم اللغوي."""
        
        session_id = f"ling_learning_{uuid.uuid4()}"
        
        try:
            if isinstance(data, dict):
                if 'word' in data:
                    self._store_word_analysis(data, metadata or {})
                elif 'pattern' in data:
                    self._store_linguistic_pattern(data, metadata or {})
                elif 'morphology' in data:
                    self._store_morphological_analysis(data, metadata or {})
            
            elif isinstance(data, str):
                # تحليل تلقائي للنص
                self._analyze_and_store_text(data, metadata or {})
            
            self.log_learning_session(session_id, source, "linguistic_data", True, metadata)
            print(f"   ✅ تم حفظ التعلم اللغوي: {session_id}")
            
        except Exception as e:
            self.log_learning_session(session_id, source, "linguistic_data", False, 
                                    {**(metadata or {}), 'error': str(e)})
            print(f"   ❌ خطأ في حفظ التعلم اللغوي: {e}")
    
    def _store_word_analysis(self, word_data: Dict[str, Any], metadata: Dict[str, Any]):
        """حفظ تحليل كلمة."""
        
        self.cursor.execute('''
            INSERT OR REPLACE INTO words_roots 
            (word, root, pattern, word_type, meaning, semantic_weight, frequency, last_used)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            word_data.get('word', ''),
            word_data.get('root', ''),
            word_data.get('pattern', ''),
            word_data.get('type', 'unknown'),
            word_data.get('meaning', ''),
            word_data.get('semantic_weight', 0.5),
            word_data.get('frequency', 1),
            datetime.now().isoformat()
        ))
        
        self.connection.commit()
    
    def _analyze_and_store_text(self, text: str, metadata: Dict[str, Any]):
        """تحليل وحفظ النص تلقائياً."""
        
        words = text.split()
        for word in words:
            # تحليل بسيط للكلمة
            word_analysis = {
                'word': word,
                'length': len(word),
                'first_letter': word[0] if word else '',
                'last_letter': word[-1] if word else '',
                'analysis_date': datetime.now().isoformat()
            }
            
            # حفظ في جدول التحليل الصرفي
            self.cursor.execute('''
                INSERT INTO morphological_analysis 
                (word, morphemes, grammatical_info, derivation_path, analysis_confidence, analysis_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                word,
                json.dumps([word]),  # تحليل بسيط
                json.dumps(word_analysis),
                json.dumps([word]),
                0.7,  # ثقة متوسطة للتحليل التلقائي
                datetime.now().isoformat()
            ))
        
        self.connection.commit()
    
    def retrieve_knowledge(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """استرجاع المعرفة اللغوية."""
        
        results = []
        
        # البحث في الكلمات والجذور
        self.cursor.execute('''
            SELECT * FROM words_roots 
            WHERE word LIKE ? OR root LIKE ? OR meaning LIKE ?
            ORDER BY semantic_weight DESC, frequency DESC
            LIMIT ?
        ''', (f'%{query}%', f'%{query}%', f'%{query}%', limit))
        
        for row in self.cursor.fetchall():
            results.append({
                'type': 'word',
                'word': row[1],
                'root': row[2],
                'pattern': row[3],
                'word_type': row[4],
                'meaning': row[5],
                'semantic_weight': row[6],
                'frequency': row[7]
            })
        
        # البحث في دلالات الحروف
        if len(query) == 1:  # حرف واحد
            self.cursor.execute('''
                SELECT * FROM letter_semantics 
                WHERE letter = ?
            ''', (query,))
            
            for row in self.cursor.fetchall():
                results.append({
                    'type': 'letter_semantic',
                    'letter': row[1],
                    'meaning': row[2],
                    'phonetic': row[3],
                    'symbolic_value': row[4],
                    'contexts': row[5],
                    'significance': row[6]
                })
        
        return results[:limit]
    
    def get_letter_semantics(self, letter: str) -> Dict[str, Any]:
        """الحصول على دلالات حرف معين."""
        
        self.cursor.execute('''
            SELECT * FROM letter_semantics WHERE letter = ?
        ''', (letter,))
        
        row = self.cursor.fetchone()
        if row:
            return {
                'letter': row[1],
                'semantic_meaning': row[2],
                'phonetic_properties': row[3],
                'symbolic_value': row[4],
                'usage_contexts': row[5],
                'cultural_significance': row[6]
            }
        
        return {}
    
    def analyze_text_semantics(self, text: str) -> Dict[str, Any]:
        """تحليل دلالات النص."""
        
        analysis = {
            'text': text,
            'length': len(text),
            'word_count': len(text.split()),
            'letter_analysis': {},
            'semantic_score': 0.0,
            'dominant_themes': []
        }
        
        # تحليل الحروف
        letter_counts = {}
        total_semantic_value = 0.0
        
        for char in text:
            if char.isalpha():
                if char not in letter_counts:
                    letter_counts[char] = 0
                letter_counts[char] += 1
                
                # الحصول على القيمة الدلالية
                semantics = self.get_letter_semantics(char)
                if semantics:
                    total_semantic_value += semantics.get('symbolic_value', 0.0)
        
        analysis['letter_analysis'] = letter_counts
        analysis['semantic_score'] = total_semantic_value / max(1, len(text))
        
        # تحديد المواضيع المهيمنة
        for letter, count in letter_counts.items():
            if count > 2:  # حروف متكررة
                semantics = self.get_letter_semantics(letter)
                if semantics:
                    analysis['dominant_themes'].append({
                        'letter': letter,
                        'meaning': semantics.get('semantic_meaning', ''),
                        'frequency': count
                    })
        
        return analysis


# مدير قواعد البيانات المتخصصة
class SpecializedDatabaseManager:
    """
    مدير قواعد البيانات المتخصصة
    يدير جميع قواعد البيانات للطبقات المختلفة
    """
    
    def __init__(self):
        self.databases: Dict[ThinkingLayerType, BaseSpecializedDatabase] = {}
        self.learning_sessions = 0
        self.total_knowledge_items = 0
        
        # إنشاء قواعد البيانات المتخصصة
        self._initialize_databases()
        
        print(f"🗄️🌟 تم إنشاء مدير قواعد البيانات المتخصصة")
        print(f"   قواعد بيانات مفعلة: {len(self.databases)}")
    
    def _initialize_databases(self):
        """تهيئة جميع قواعد البيانات المتخصصة."""
        
        # قاعدة البيانات الرياضية
        self.databases[ThinkingLayerType.MATHEMATICAL] = MathematicalDatabase()
        
        # قاعدة البيانات اللغوية
        self.databases[ThinkingLayerType.LINGUISTIC] = LinguisticDatabase()
        
        # TODO: إضافة باقي قواعد البيانات المتخصصة
        # self.databases[ThinkingLayerType.LOGICAL] = LogicalDatabase()
        # self.databases[ThinkingLayerType.INTERPRETIVE] = InterpretiveDatabase()
        # self.databases[ThinkingLayerType.PHYSICAL] = PhysicalDatabase()
        # self.databases[ThinkingLayerType.SYMBOLIC] = SymbolicDatabase()
        # self.databases[ThinkingLayerType.VISUAL] = VisualDatabase()
        # self.databases[ThinkingLayerType.SEMANTIC] = SemanticDatabase()
        
        print(f"   ✅ تم تهيئة {len(self.databases)} قاعدة بيانات متخصصة")
    
    def store_learning_for_layer(self, layer_type: ThinkingLayerType, data: Any, 
                                source: LearningSource, metadata: Dict[str, Any] = None):
        """حفظ التعلم لطبقة معينة."""
        
        if layer_type in self.databases:
            self.databases[layer_type].store_learning(data, source, metadata)
            self.learning_sessions += 1
            print(f"   📚 تم حفظ التعلم للطبقة {layer_type.value}")
        else:
            print(f"   ❌ قاعدة بيانات الطبقة {layer_type.value} غير متوفرة")
    
    def retrieve_knowledge_from_layer(self, layer_type: ThinkingLayerType, 
                                    query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """استرجاع المعرفة من طبقة معينة."""
        
        if layer_type in self.databases:
            return self.databases[layer_type].retrieve_knowledge(query, limit)
        else:
            return []
    
    def get_all_database_stats(self) -> Dict[str, Any]:
        """إحصائيات جميع قواعد البيانات."""
        
        stats = {
            'total_databases': len(self.databases),
            'total_learning_sessions': self.learning_sessions,
            'database_details': {}
        }
        
        for layer_type, db in self.databases.items():
            stats['database_details'][layer_type.value] = db.get_database_stats()
        
        return stats
    
    def close_all_databases(self):
        """إغلاق جميع قواعد البيانات."""
        
        for db in self.databases.values():
            db.close()
        
        print("🗄️ تم إغلاق جميع قواعد البيانات")


# مثال على الاستخدام والاختبار
if __name__ == "__main__":
    print("🚀 اختبار نظام قواعد البيانات المتخصصة")
    print("=" * 60)
    
    # إنشاء مدير قواعد البيانات
    db_manager = SpecializedDatabaseManager()
    
    # اختبار التعلم الرياضي
    print("\n🧮 اختبار التعلم الرياضي:")
    math_data = {
        'equation': {
            'type': 'sigmoid',
            'formula': '1 / (1 + exp(-k*(x-x0)))',
            'parameters': {'k': 1.0, 'x0': 0.0},
            'accuracy': 0.95
        }
    }
    
    db_manager.store_learning_for_layer(
        ThinkingLayerType.MATHEMATICAL, 
        math_data, 
        LearningSource.USER_INTERACTION,
        {'context': 'sigmoid_learning'}
    )
    
    # اختبار استرجاع المعرفة الرياضية
    math_results = db_manager.retrieve_knowledge_from_layer(
        ThinkingLayerType.MATHEMATICAL, 
        'sigmoid'
    )
    print(f"نتائج البحث الرياضي: {len(math_results)}")
    
    # اختبار التعلم اللغوي
    print("\n🗣️ اختبار التعلم اللغوي:")
    linguistic_data = "الرياضيات هي لغة الكون"
    
    db_manager.store_learning_for_layer(
        ThinkingLayerType.LINGUISTIC,
        linguistic_data,
        LearningSource.USER_INTERACTION,
        {'context': 'text_analysis'}
    )
    
    # اختبار استرجاع المعرفة اللغوية
    ling_results = db_manager.retrieve_knowledge_from_layer(
        ThinkingLayerType.LINGUISTIC,
        'الرياضيات'
    )
    print(f"نتائج البحث اللغوي: {len(ling_results)}")
    
    # إحصائيات شاملة
    print("\n📊 إحصائيات قواعد البيانات:")
    stats = db_manager.get_all_database_stats()
    print(f"- إجمالي قواعد البيانات: {stats['total_databases']}")
    print(f"- إجمالي جلسات التعلم: {stats['total_learning_sessions']}")
    
    for layer_name, layer_stats in stats['database_details'].items():
        print(f"- {layer_name}: {layer_stats['total_learning_sessions']} جلسة تعلم")
    
    # إغلاق قواعد البيانات
    db_manager.close_all_databases()
    
    print("\n✅ تم الانتهاء من اختبار قواعد البيانات المتخصصة!")

