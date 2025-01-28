# Python CI Workflow

このプロジェクトは、イベント処理を行う AWS Lambda 関数とその自動テスト・コード品質チェックの環境を提供します。

## 概要

このプロジェクトは以下の機能を持つ AWS Lambda 関数を含みます：

- イベントのバリデーション
- イベントデータの変換処理
- エラーハンドリングとロギング
- 包括的なテストカバレッジ
- 静的型チェック
- コードスタイルチェック（PEP 8 準拠）

## プロジェクト構造

```text
/
├── .github/
│   └── workflows/
│       └── python-test.yaml        # CI パイプラインの定義
├── functions/
│   └── __init__.py                 # パッケージ初期化ファイル
├── tests/
│   ├── requirements.txt            # テスト依存関係
│   ├── requirements_test_tools.txt # テストツール依存関係
│   └── test_process_event.py       # テストコード
├── .gitignore                      # Git 無視ファイル
├── pytest.ini                      # pytest 設定ファイル
├── requirements.txt                # 関数の依存関係
├── setup.cfg                       # flake8 と mypy の設定ファイル
└── README.md                       # このREADME
```

## 開発環境のセットアップ

### 前提条件

- Python 3.12
- pip（Python パッケージマネージャー）
- Git

### インストール手順

1. リポジトリのクローン：

```bash
git clone [リポジトリURL]
cd [リポジトリ名]
```

2. 依存パッケージのインストール：

```bash
# テストライブラリのインストール（flake8, pytest, mypy）
pip install -r tests/requirements_test_tools.txt

# 関数の依存関係のインストール
pip install -r tests/requirements.txt
```

## 開発ガイド

### コード品質チェック

以下のコマンドでコード品質をチェックできます：

```bash
# PEP 8 スタイルチェック
flake8 functions/

# 静的型チェック
mypy functions/

# ユニットテスト
pytest tests/
```

### GitHub Actions

以下のタイミングで自動的にチェックが実行されます：

- feature/\* ブランチへのプッシュ時
- fix/\* ブランチへのプッシュ時

チェック内容：

1. コードスタイル（flake8）
2. 静的型チェック（mypy）
3. ユニットテスト（pytest）
