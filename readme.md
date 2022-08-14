# streaming

## プラン

### ほしい動作
- ビデオのサムネイルがグリッドに並ぶ
- マウスホーバーでgif再生
- クリックするとストリーミングされる

### ver 0.0.1

- ビデオのサムネイルのワイヤーがグリッドに並ぶ

#### サーバーURL設計

- /videos

#### DB設計

- videos
  - id
  - name
  - path

#### サムネ作成

- 並列にすると却って遅い
- 理由は分からないけど
- なので、サムネは、別で作っておく必要あり
- ビデオ本体も、simlinkを張っておかないとだめな気がする

## タスク

```mermaid
flowchart TD
  data3[data3に入っているboxビデオを変換する]
  mp4[mp4ファイル郡]
  thumbnail[サムネイル郡]
  thumbnail_script[サムネイルへの変換スクリプトを作る]
  subgraph design
    ビデオとサムネイル置き場を設計する
    %% ビデオの識別キーを設計する = ファイルパスのハッシュとか？ファイルで良い？
    %% ビデオとサムネイルの対応を設計する = sqliteに持っておけば良さそう
  end

  data3 --> mp4
  mp4 --> thumbnail
  thumbnail_script --> thumbnail
  design --> thumbnail_script

```
