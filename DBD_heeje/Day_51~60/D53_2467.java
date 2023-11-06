// [BOJ] 2467. 용액
// 실행 시간 : 
// 메모리 : 

import java.util.*;
import java.io.*;

class Main {
    public static StringTokenizer st;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] liquids = new int[N];
        
        for (int i = 0; i < N; i++) {
            liquids[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = N - 1;
        int mix_liquid;
        int[] answer = new int[2];
        int min_mix_liquid = 2000000000;

        while (start < end) {
            mix_liquid = liquids[start] + liquids[end];
            if (min_mix_liquid > Math.abs(mix_liquid)) {
                min_mix_liquid = Math.min(min_mix_liquid, Math.abs(mix_liquid));
                answer[0] = liquids[start];
                answer[1] = liquids[end];
            }

            if (mix_liquid == 0) {
                break;
            } else if (mix_liquid < 0) {
                start += 1;
            } else {
                end -= 1;
            }
        }

        System.out.println(answer[0] + " " + answer[1]);
    }
}