#!/usr/bin/env python3
"""
محلل الأداء - Performance Analyzer
نظام بصيرة المتكامل

📊 تحليل مفصل لأداء النظام
⚡ قياس السرعة والكفاءة
🎯 تحسين الأداء

المطور: باسل يحيى عبدالله
جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله
"""

import time
import statistics
from typing import Dict, List, Any, Callable
from dataclasses import dataclass
from datetime import datetime

@dataclass
class PerformanceResult:
    """نتيجة قياس الأداء"""
    function_name: str
    execution_time: float
    memory_usage: float
    success: bool
    error_message: str = ""

class BaseraPerformanceAnalyzer:
    """
    محلل أداء نظام بصيرة
    
    📊 تحليل شامل للأداء:
    - قياس أوقات التنفيذ
    - مراقبة استخدام الذاكرة
    - تحليل الكفاءة
    - تقارير مفصلة
    """
    
    def __init__(self):
        self.creation_time = datetime.now()
        self.performance_results: List[PerformanceResult] = []
        
        print(f"📊⚡ تم إنشاء محلل أداء نظام بصيرة")
        print(f"   🕐 وقت الإنشاء: {self.creation_time}")
    
    def measure_performance(self, func: Callable, *args, **kwargs) -> PerformanceResult:
        """قياس أداء دالة"""
        import tracemalloc
        
        function_name = func.__name__ if hasattr(func, '__name__') else str(func)
        
        # بدء قياس الذاكرة
        tracemalloc.start()
        
        start_time = time.time()
        success = True
        error_message = ""
        
        try:
            # تنفيذ الدالة
            result = func(*args, **kwargs)
            
        except Exception as e:
            success = False
            error_message = str(e)
            result = None
        
        execution_time = time.time() - start_time
        
        # قياس استخدام الذاكرة
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        memory_usage = peak / 1024 / 1024  # تحويل إلى MB
        
        performance_result = PerformanceResult(
            function_name=function_name,
            execution_time=execution_time,
            memory_usage=memory_usage,
            success=success,
            error_message=error_message
        )
        
        self.performance_results.append(performance_result)
        
        print(f"⚡ قياس الأداء: {function_name}")
        print(f"   ⏱️ الوقت: {execution_time:.4f}s")
        print(f"   💾 الذاكرة: {memory_usage:.2f}MB")
        print(f"   ✅ النجاح: {success}")
        
        return performance_result
    
    def benchmark_function(self, func: Callable, iterations: int = 10, *args, **kwargs) -> Dict[str, Any]:
        """قياس أداء دالة عدة مرات"""
        print(f"🏃 بدء قياس الأداء المتكرر: {func.__name__} ({iterations} مرات)")
        
        execution_times = []
        memory_usages = []
        successes = 0
        
        for i in range(iterations):
            result = self.measure_performance(func, *args, **kwargs)
            
            if result.success:
                execution_times.append(result.execution_time)
                memory_usages.append(result.memory_usage)
                successes += 1
        
        if not execution_times:
            return {
                "function_name": func.__name__,
                "iterations": iterations,
                "success_rate": 0.0,
                "error": "جميع المحاولات فشلت"
            }
        
        benchmark_result = {
            "function_name": func.__name__,
            "iterations": iterations,
            "success_rate": successes / iterations * 100,
            "execution_time": {
                "min": min(execution_times),
                "max": max(execution_times),
                "mean": statistics.mean(execution_times),
                "median": statistics.median(execution_times),
                "stdev": statistics.stdev(execution_times) if len(execution_times) > 1 else 0
            },
            "memory_usage": {
                "min": min(memory_usages),
                "max": max(memory_usages),
                "mean": statistics.mean(memory_usages),
                "median": statistics.median(memory_usages)
            }
        }
        
        print(f"📊 نتائج القياس المتكرر:")
        print(f"   ✅ معدل النجاح: {benchmark_result['success_rate']:.1f}%")
        print(f"   ⏱️ متوسط الوقت: {benchmark_result['execution_time']['mean']:.4f}s")
        print(f"   💾 متوسط الذاكرة: {benchmark_result['memory_usage']['mean']:.2f}MB")
        
        return benchmark_result
    
    def compare_functions(self, functions: List[Callable], iterations: int = 5, *args, **kwargs) -> Dict[str, Any]:
        """مقارنة أداء عدة دوال"""
        print(f"🔄 مقارنة أداء {len(functions)} دالة")
        
        comparison_results = {}
        
        for func in functions:
            benchmark = self.benchmark_function(func, iterations, *args, **kwargs)
            comparison_results[func.__name__] = benchmark
        
        # ترتيب النتائج حسب السرعة
        sorted_by_speed = sorted(
            comparison_results.items(),
            key=lambda x: x[1]['execution_time']['mean'] if x[1].get('execution_time') else float('inf')
        )
        
        print(f"\n🏆 ترتيب الدوال حسب السرعة:")
        for i, (name, result) in enumerate(sorted_by_speed, 1):
            if result.get('execution_time'):
                print(f"   {i}. {name}: {result['execution_time']['mean']:.4f}s")
            else:
                print(f"   {i}. {name}: فشل")
        
        return {
            "comparison_results": comparison_results,
            "fastest_function": sorted_by_speed[0][0] if sorted_by_speed and sorted_by_speed[0][1].get('execution_time') else None,
            "performance_ranking": [name for name, _ in sorted_by_speed]
        }
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """ملخص الأداء العام"""
        if not self.performance_results:
            return {"error": "لا توجد نتائج أداء"}
        
        total_tests = len(self.performance_results)
        successful_tests = sum(1 for r in self.performance_results if r.success)
        
        execution_times = [r.execution_time for r in self.performance_results if r.success]
        memory_usages = [r.memory_usage for r in self.performance_results if r.success]
        
        summary = {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "success_rate": successful_tests / total_tests * 100,
            "testing_duration": str(datetime.now() - self.creation_time)
        }
        
        if execution_times:
            summary["performance_stats"] = {
                "avg_execution_time": statistics.mean(execution_times),
                "avg_memory_usage": statistics.mean(memory_usages),
                "fastest_execution": min(execution_times),
                "slowest_execution": max(execution_times)
            }
        
        return summary
    
    def generate_performance_report(self) -> str:
        """إنشاء تقرير أداء مفصل"""
        summary = self.get_performance_summary()
        
        report = f"""
📊 تقرير أداء نظام بصيرة الثوري
{'='*50}

📈 الإحصائيات العامة:
   📊 إجمالي الاختبارات: {summary.get('total_tests', 0)}
   ✅ الاختبارات الناجحة: {summary.get('successful_tests', 0)}
   📊 معدل النجاح: {summary.get('success_rate', 0):.1f}%
   ⏱️ مدة الاختبار: {summary.get('testing_duration', 'غير محدد')}

"""
        
        if summary.get('performance_stats'):
            stats = summary['performance_stats']
            report += f"""⚡ إحصائيات الأداء:
   ⏱️ متوسط وقت التنفيذ: {stats['avg_execution_time']:.4f}s
   💾 متوسط استخدام الذاكرة: {stats['avg_memory_usage']:.2f}MB
   🚀 أسرع تنفيذ: {stats['fastest_execution']:.4f}s
   🐌 أبطأ تنفيذ: {stats['slowest_execution']:.4f}s

"""
        
        # تفاصيل الاختبارات الفردية
        report += "📋 تفاصيل الاختبارات:\n"
        for i, result in enumerate(self.performance_results[-10:], 1):  # آخر 10 اختبارات
            status = "✅" if result.success else "❌"
            report += f"   {i}. {status} {result.function_name}: {result.execution_time:.4f}s, {result.memory_usage:.2f}MB\n"
        
        report += f"\n🧬 جميع الأفكار والنظريات من إبداع باسل يحيى عبدالله"
        
        return report

def test_performance_analyzer():
    """اختبار محلل الأداء"""
    analyzer = BaseraPerformanceAnalyzer()
    
    # دوال اختبار
    def fast_function():
        return sum(range(1000))
    
    def slow_function():
        time.sleep(0.1)
        return sum(range(10000))
    
    def memory_intensive_function():
        data = [i**2 for i in range(100000)]
        return len(data)
    
    # قياس أداء فردي
    analyzer.measure_performance(fast_function)
    analyzer.measure_performance(slow_function)
    analyzer.measure_performance(memory_intensive_function)
    
    # قياس متكرر
    analyzer.benchmark_function(fast_function, iterations=5)
    
    # مقارنة الدوال
    analyzer.compare_functions([fast_function, slow_function], iterations=3)
    
    # تقرير الأداء
    print(analyzer.generate_performance_report())

def main():
    """الدالة الرئيسية"""
    test_performance_analyzer()

if __name__ == "__main__":
    main()

