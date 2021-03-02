void DFS(int lv, int* s, int idx) {
	if (lv == m) {							 
		Dtn(s);
		return;
	}
 
	int size = chicken.size();
	for (int i = idx; i < size; i++) {		//중복을 피하기 위한 idx
		if (!visited[i]) {
			visited[i] = true;
			s[lv] = i;						//선택
			DFS(lv + 1, s, i + 1);
			visited[i] = false;
		}
	}
}
