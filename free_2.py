import time
import tracemalloc
import argparse
import os

def measure_once(func):
    tracemalloc.start()
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return end - start, peak / 1024  # seconds, KB

def load_function_from_code(code_str, func_name="user_func"):
    namespace = {}
    exec(f"def {func_name}():\n" + "\n".join("    " + line for line in code_str.splitlines()), namespace)
    return namespace[func_name]

def main():
    parser = argparse.ArgumentParser(description="Measure time and memory of a Python code block")
    parser.add_argument('--file', type=str, help='Path to Python source file (only function body)')
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as f:
            code = f.read()
        name = os.path.basename(args.file).replace(".py", "")
    else:
        print(" Python 코드 입력. 'END'를 입력하면 종료됩니다.")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        code = "\n".join(lines)
        name = input(" 코드 이름을 입력하세요: ")

    func = load_function_from_code(code, name)
    exec_time, memory_kb = measure_once(func)

    print(f"\n 결과 for '{name}'")
    print(f"⏱ 실행 시간: {exec_time:.6f}초")
    print(f"📦 메모리 사용량: {memory_kb:.2f}KB")

if __name__ == "__main__":
    main()
