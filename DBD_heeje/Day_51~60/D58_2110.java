// [BOJ] 2110. 공유기 설치
// 실행 시간 : 360 ms
// 메모리 : 38220 KB

import java.util.*;
import java.io.*;

class Main {
	public static int N, C;
	public static int[] houses;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		houses = new int[N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			houses[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(houses);
		
		System.out.println(solve());
	}
	
	public static int solve() {
		int start = 1;
		int end = houses[N - 1] - houses[0];
		int maxDis = end / (C - 1);
		int mid, cnt, curHouse;
		while (start <= end) {
			mid = (start + end) / 2;
			if (maxDis < mid) {
				end = mid - 1;
				continue;
			}
			
			cnt = 1;
			curHouse = houses[0];
			for (int i = 1; i < N; i++) {
				if (houses[i] - curHouse >= mid) {
					cnt += 1;
					curHouse = houses[i];
				}
			}
			
			if (cnt >= C) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
		}
		return end;
	}
}