// [BOJ] 11053. 가장 긴 증가하는 부분 수열
// 실행 시간 : 148 ms
// 메모리 : 14496 KB

import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	
    	st = new StringTokenizer(br.readLine());
    	int[] numbers = new int[N];
    	for (int i = 0; i < N; i++) {
    		numbers[i] = Integer.parseInt(st.nextToken());
    	}
    	
    	int[] dp = new int[N];
    	for (int i = 0; i < N; i++) {
    		dp[i] = 1;
    	}
    	
    	for (int i = 1; i < N; i++) {
    		for (int j = 0; j < i; j++) {
    			if (numbers[i] > numbers[j]) {
    				dp[i] = Math.max(dp[i], dp[j] + 1);
    			}
    		}
    	}
    	
    	int answer = 0;
    	for (int i = 0; i < N; i++) {
    		if (answer < dp[i]) {
    			answer = dp[i];
    		}
    	}
    	
    	System.out.println(answer);
    }
}