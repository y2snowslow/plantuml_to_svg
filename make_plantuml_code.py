import os
import subprocess
from pathlib import Path

# ダイアグラムを生成する関数
def generate_diagram(plantuml_file, output_file):
    cmd = ['java', '-jar', 'C:\\Users\\snow_\\.vscode\\extensions\\jebbs.plantuml-2.17.5\\plantuml.jar', '-tsvg', '-pipe']
    with open(plantuml_file, 'r') as puml_file:
        with open(output_file, 'w') as out_file:
            subprocess.run(cmd, stdin=puml_file, stdout=out_file)
    print(f"Generated diagram at {output_file.absolute()}")

# スクリプトの存在するディレクトリを取得
current_dir = Path(__file__).parent

# 出力ディレクトリを設定
output_dir = current_dir / 'imgdir'
output_dir.mkdir(parents=True, exist_ok=True)

# .puファイルを見つける
for plantuml_file in current_dir.glob('*.pu'):
    # 出力ファイルのパスを生成
    output_file = output_dir / (plantuml_file.stem + '.svg')
    # ダイアグラムを生成
    generate_diagram(plantuml_file, output_file)

print("Diagrams have been generated.")
