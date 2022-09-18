# 開発・管理用メモ

## 資材

- `/resource/videos`: mp4ファイルを配置する場所
- `/resource/thumbnails`: サムネイルファイルを配置する場所

## データベース

1. `server/thumbnail`パッケージで、mp4ビデオからサムネイルを作ることができる
2. このとき同時に、mp4ビデオとサムネイルのパスのペアをjsonとして吐き出すので、それを元にDBを作成する

## 開発用サーバー

開発用のサーバーは、以下の手順で立ち上げることができる

1. [/server](./server)に移動して、`make start`を実行
2. [/client](./client)に移動して、`npm start`を実行

開発時には、`index.html`や`js`, `css`などの静的ファイルはReactの開発用サーバーから配信される。
そのため、サーバーサイドからは動画・サムネイル以外の静的ファイルが配信されない想定となっている。

## 本番用サーバー

本番用のサーバーは、以下の手順で立ち上げることができる

1. [/client](./client)に移動して、`npm run build`を実行
2. [/release](./release)に移動して、`make run`を実行

[/release/static](./release/static)は、[/client/build](./client/build)
へのシンボリックリンクになっており、ビルドで生成された静的ファイルは、ここから配信される。
