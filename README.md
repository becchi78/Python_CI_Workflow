# イベント処理 Lambda 関数

イベントを処理する AWS Lambda 関数と自動テスト・コード品質チェックの環境です。

## 概要

このプロジェクトは以下の機能を持つ AWS Lambda 関数を含みます：

- イベントのバリデーション
- イベントデータの変換処理
- エラーハンドリングとロギング
- 包括的なテストカバレッジ
- 静的型チェック
- コードスタイルチェック（PEP 8 準拠）

## プロジェクト構造

```
/
├── .github/
│   └── workflows/
│       └── python-lambda-check.yml  # CI パイプラインの定義
├── functions/
│   └── process_event.py            # Lambda 関数本体
├── tests/
│   └── test_process_event.py       # テストコード
├── requirements.txt                # 関数の依存関係
└── requirements-dev.txt           # テストライブラリ
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
pip install -r requirements-dev.txt

# 関数の依存関係のインストール
pip install -r requirements.txt
```

## 開発ガイド

### コード品質チェック

以下のコマンドでコード品質をチェックできます：

```bash
# PEP 8 スタイルチェック
flake8 functions/ --count --max-complexity=10 --max-line-length=100 --statistics

# 静的型チェック
mypy functions/ --strict

# ユニットテスト
pytest tests/ -v
```

### GitHub Actions

以下のタイミングで自動的にチェックが実行されます：

- feature/\* ブランチへのプッシュ時
- fix/\* ブランチへのプッシュ時

チェック内容：

1. コードスタイル（flake8）
2. 静的型チェック（mypy）
3. ユニットテスト（pytest）

### 新機能の追加手順

1. 新しいブランチの作成：

```bash
git checkout -b feature/機能名
```

2. 変更を加え、ローカルでテストを実行
3. 変更をコミット
4. GitHub にプッシュしてプルリクエストを作成

## Lambda 関数の使用方法

Lambda 関数は以下の形式のイベントを受け付けます：

```json
{
  "userId": "12345",
  "eventType": "click",
  "timestamp": "2024-01-21T10:00:00Z",
  "metadata": {
    "page": "home"
  }
}
```

### エラーハンドリング

- バリデーションエラー：ステータスコード 400 が返却されます
- 内部エラー：ステータスコード 500 が返却されます

## 注意事項

- このプロジェクトは Python 3.12 で動作確認しています
- 開発時は必ずテストライブラリ（requirements-dev.txt）をインストールしてください
- コミット前に必ずローカルでテストを実行してください

## ライセンス

[ライセンス情報を記載]
