# AzureOperator

Azure リソース（主にネットワーク）を扱う小規模なドメインモデル群です。Python 3.12 を前提とし、レイヤ構成（application → resources → infra）で値オブジェクト・集約・ルールを分離します。

## 設計概要
- レイヤリング: `application`（ユースケース）→ `resources`（ドメイン）→ `infra/azure_api`（SDK 依存を隔離）。
- 値オブジェクト: `Location`, `TagBase`, `NetworkPrefix` などは不変データで表現。
- 集約: `VirtualNetwork` が Location・Prefix・Tags を保持。タグはコレクション側で付け外し。
- ルール: 共通の命名/プレフィックス判定を `resources/common/model` に集約（各モデルはパターンを定義するだけで検証可）。
- 生成: 入力が揃う場合は Factory を推奨。段階的入力が必要なら Builder を併用。

## プロジェクト構成
- `src/resources/abstract/model/` 抽象・基盤（例: `ResourceBase`, `NameRule`）
- `src/resources/common/model/` 共通値/集約/ルール（例: `Location`, `TagBase`）
- `src/resources/network/model/` ネットワーク領域（例: `VirtualNetwork`, `NetworkPrefix`）
- `src/infra/azure_api/` Azure API 連携のアダプタ層
- `tests/` 単体テスト（`tests/conftest.py` が `src` を import パスへ追加）

## セットアップ & 実行
- 仮想環境
  - macOS/Linux: `python3.12 -m venv venv && source venv/bin/activate`
  - Windows (PowerShell): `py -3.12 -m venv venv; .\\venv\\Scripts\\Activate.ps1`
- 開発インストール（推奨）: `pip install -e .[dev]`
- テスト: `pytest -q`（必要に応じて `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q`）

## クイックスタート
```python
from ipaddress import IPv4Network
from src.resources.common.model.common_class import Location, TagBase
from src.resources.common.model.common_class_values import LocationValues
from src.resources.network.model.common.common_network_data_value import NetworkPrefix
from src.resources.network.model.virtual_network.virtual_netowrk import VirtualNetwork

loc = Location(LocationValues.JAPAN_EAST)
prefix = NetworkPrefix(IPv4Network("10.0.0.0/24"))
tags = [TagBase("env", "dev")]

vnet = VirtualNetwork(name="vnet-01", prefix=prefix, location=loc, tags=tags)
print(vnet.name, [(t.tag_key, t.tag_value) for t in vnet.tags])
```

詳細なコーディング規約や PR ルールは `AGENTS.md` を参照してください（会話は日本語、コード/コマンド/パスは英語）。
