import time
import tracemalloc
import statistics
import matplotlib.pyplot as plt
from fpdf import FPDF
import argparse
import os

def measure_performance(func, iterations=5):
    times = []
    memories = []
    for _ in range(iterations):
        tracemalloc.start()
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append(end_time - start_time)
        memories.append(peak / 1024)  # KB
    return {
        "time": statistics.mean(times),
        "memory": statistics.mean(memories)
    }

def compare_algorithms(algorithms):
    results = {}
    for name, func in algorithms.items():
        print(f"⏳ Measuring '{name}' ...")
        results[name] = measure_performance(func)
    return results

def visualize_results(results, output_path="performance_comparison.png"):
    names = list(results.keys())
    times = [results[name]["time"] for name in names]
    memories = [results[name]["memory"] for name in names]

    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    axs[0].bar(names, times, color="skyblue")
    axs[0].set_title("Execution Time (seconds)")
    axs[1].bar(names, memories, color="salmon")
    axs[1].set_title("Memory Usage (KB)")

    plt.tight_layout()
    plt.savefig(output_path)
    return output_path

def generate_pdf_report(results, graph_path, output_path="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Algorithm Performance Report", ln=True, align='C')

    pdf.set_font("Arial", size=12)
    for name, data in results.items():
        pdf.ln()
        pdf.cell(200, 10, txt=f"{name}: Time = {data['time']:.6f}s, Memory = {data['memory']:.2f}KB", ln=True)

    pdf.ln()
    pdf.image(graph_path, x=10, y=pdf.get_y(), w=180)
    pdf.output(output_path)

def load_function_from_code(code_str, func_name="user_func"):
    namespace = {}
    exec(f"def {func_name}():\n" + "\n".join("    " + line for line in code_str.splitlines()), namespace)
    return namespace[func_name]

def main():
    parser = argparse.ArgumentParser(description="Compare algorithms' performance (CLI Tool)")
    parser.add_argument('--file', nargs='*', help='Python source file(s) with a single function body to test')
    args = parser.parse_args()

    algorithms = {}

    if args.file:
        for path in args.file:
            with open(path, 'r') as f:
                code = f.read()
                func = load_function_from_code(code, os.path.basename(path).replace(".py", ""))
                algorithms[os.path.basename(path)] = func
    else:
        print(" Enter your Python function code block. Type 'END' when done:")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)
        name = input(" Enter a name for this algorithm: ")
        func = load_function_from_code(code, name)
        algorithms[name] = func

    results = compare_algorithms(algorithms)
    graph_path = visualize_results(results)
    generate_pdf_report(results, graph_path)
    print("\n 리포트가 생성되었습니다: report.pdf")

if __name__ == "__main__":
    main()
