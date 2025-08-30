# Repository Guidelines

## プロジェクト構成とモジュール
- Python バージョン: `3.12`（`.python-version` 参照）。
- 主要コードは `src/` に配置（パッケージ構成）：
  - `src/application/`：アプリケーションサービス層。
  - `src/resources/`：ドメインモデルと抽象（例: `abstract/`, `network/`）。
  - `src/infra/azure_api/`：Azure API 連携（例: `network/`）。
- 例: `from src.resources.abstract.base_class import Location`。

## ビルド・テスト・開発コマンド
- 仮想環境作成（推奨）:
  - macOS/Linux: `python3.12 -m venv venv && source venv/bin/activate`
  - Windows: `py -3.12 -m venv venv; .\\venv\\Scripts\\Activate.ps1`
- 開発ツール導入（例）: `pip install -U pytest black ruff mypy`。
- テスト実行（導入後）: `pytest -q`。
- フォーマット: `black src tests`。
- リント: `ruff check src tests`。

## コーディング規約と命名
- PEP 8 準拠、インデントは 4 スペース、型ヒントを使用。
- 命名: モジュール/関数は `snake_case`、クラスは `PascalCase`、定数は `UPPER_CASE`。
- 公開 API は `src/` 配下に集約し、各ディレクトリに `__init__.py` を配置。
- 相対 import より `src.*` の明示的 import を優先。

## テストガイドライン
- フレームワーク: `pytest`。
- 配置: `src/` をミラーする `tests/`（例: `tests/resources/test_base_class.py`）。
- 命名: ファイルは `test_*.py`、関数は `test_*`。共通準備は fixture を使用。
- 目標カバレッジ: 意味のあるカバレッジ（例: 80%以上）。`pytest --cov=src` を利用可（設定時）。

## コミットと PR ガイドライン
- コミットは Conventional Commits 推奨（例: `feat: add virtual network model`, `fix: correct tag initialization`）。
- PR には概要・背景・関連 Issue・挙動変更のログ/スクショを添付。
- PR は小さく焦点を絞り、公開仕様変更時はドキュメントを更新。

## セキュリティと設定のヒント
- 秘密情報はコミットしない。環境変数や Azure Key Vault を使用。
- ローカル環境は `venv/` で分離（`.gitignore` で除外済み）。
- Azure 連携は最小権限で検証し、サブスクリプション ID/キーはハードコードしない。

## アーキテクチャ概要
- レイヤー構造: `application`（ユースケース）→ `resources`（ドメイン）→ `infra/azure_api`（アダプタ）。
- ドメイン型は Azure SDK から独立させ、SDK 依存は `infra/` に隔離。

## コミュニケーションと言語ポリシー
- 以降のやり取りは日本語でお願いします。コードやコマンド、ファイルパスは英語表記のままで問題ありません。
- Issue/PR のタイトルや説明は日本語・英語どちらでも構いませんが、識別子（クラス名・関数名・変数名）は英語を使用してください。
