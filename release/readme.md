## 本番環境

### DB構築

このフォルダで、`make -f build-db.mk db`を実行する。

### サービス起動

本番サーバーは、Launch Controlによるサービスとして運用する。

このフォルダで、`make -f release.mk start`を実行する。

[./static](./static)は、[../client/build](./client/build)
へのシンボリックリンクになっており、ビルドで生成された静的ファイルは、ここから配信される。
