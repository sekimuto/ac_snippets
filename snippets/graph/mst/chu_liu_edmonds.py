def chu_liu_edmonds(n, edges, r):
    """
        Chu-Liu/Edmondsのアルゴリズム

        最小有向全域木を求めるアルゴリズム

        Args:
            n: 頂点数
            edges: (始点, 終点, 重み)のリスト
            r: 根の頂点番号
    """

    INF = 1 << 61

    # ii番目の頂点に対して、(重み, 辺が伸びてくる頂点)の最小の重みのものを計算
    min_edges = [(INF, -1) for _ in range(n)]

    for s, t, w in edges:
        min_edges[t] = min(min_edges[t], (w, s))
    
    # 根はわかるように特別な値を入れておく
    min_edges[r] = (0, -1)

    # 各頂点に対して辺を逆に進んでいき、閉路に行きあたるかを調べる
    group = [0] * n     # 縮約したあとに割り振られる頂点番号
    is_comp = [False] * n   # その頂点が縮約されたか
    induced_v_cnt = 0       # 縮約したあとの頂点数

    seen = [False] * n

    for v in range(n):
        if not seen[v]:
            # vからの探索でたどっていった頂点を格納するリスト
            chain = []
            cur = v

            # vを通っていって、根にいきつくか、それとも閉路に入っていってしまうのかを調べる
            # seenはループ全体で共通なので、すでに探索済みの頂点に行きあたった場合も調査終了になる
            while not seen[cur] and cur != -1:
                chain.append(cur)
                seen[cur] = True
                cur = min_edges[cur][1]
            

            # 根まで到達できなかった場合、
            # 閉路に入った or すでに探索済みの頂点に行きあたった、の2通り
            if cur != -1:
                # 閉路判定フラグ
                is_cycle = False
                # 探索チェーンを辿っていって、閉路上の頂点であれば集約する
                for u in chain:
                    group[u] = induced_v_cnt
                    # 閉路に入ったらフラグをつける
                    if u == cur:
                        is_cycle = True
                        is_comp[induced_v_cnt] = True

                    if not is_cycle:
                        induced_v_cnt += 1
            
            # 根まで到達できた場合、新しい頂点番号を順番に振る
            else:
                for v in chain:
                    group[v] = induced_v_cnt
                    induced_v_cnt += 1

    # ここまでで、すべての頂点を始点に1回は逆向きの探索が完了して、
    # 縮約後の新しい頂点番号が、すべての頂点に対して振り直されている

    # この時点でinduced_v_cntがnと一致していれば、すべての頂点番号が縮約されずそのまま
    # すなわち、閉路が存在せず、有向木が作成できたので、コストを合計して返す
    # +1してるのは、rootの-1分の補正
    if induced_v_cnt == n:
        res = sum(map(lambda x: x[0], min_edges))
        return res
    
    # 閉路が含まれていた場合は、閉路上の頂点が選択した辺のコストを合計する
    res = sum((min_edges[v][0] for v in range(n) if v != r and is_comp[group[v]]))

    # 新しいグラフを作成して、この関数を再帰的に呼ぶ
    # このとき、
    # 1. 閉路 -> 閉路なら取り除く
    # 2. 閉路 -> 外部ならコストそのままに縮約した頂点 -> 外部に置き換える
    # 3. 外部 -> 閉路なら外部 -> 縮約した頂点に置き換え、コストはcost(外部 -> 縮約頂点) - cost(外部 -> 閉路)に置き換える
    edges_new = []
    for start, end, cost in edges:
        # パターン1
        if group[start] == group[end]:
            continue

        # パターン3
        if is_comp[group[end]]:
            edges_new.append((group[start], group[end], cost-min_edges))

        # それ以外(2も含む)
        else:
            edges_new.append((group[start], group[end], cost))
    
    # 新しいグラフのコストはres分だけ少なくなっているので、res + 再帰で呼んだ結果が答えになる
    return res + chu_liu_edmonds(induced_v_cnt, edges_new, group[r])
