// [BOJ] 2493. 탑
// 실행 시간 : 808 ms
// 메모리 : 97776 KB

import java.util.*;
import java.io.*;

class Main {
	public static StringTokenizer st;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		Stack<Integer> stackInt = new Stack<>();
		
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] towers = new int[N];
		int[] answer = new int[N];
		for (int i = 0; i < N; i++) {
			towers[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = N - 1; i >= 0; i--) {
			while (!stackInt.isEmpty() && towers[stackInt.peek()] < towers[i]) {
				answer[stackInt.pop()] = i + 1;
			}
			
			stackInt.add(i);
		}
		
		for (int i = 0; i < N; i++) {
			sb.append(answer[i] + " ");
		}
		
		System.out.println(sb);
	}
}