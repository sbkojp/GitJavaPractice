package ch4;

public class Main {

	public static void main(String[] args) {
		int[]scores = {20,30,40,50,80};
		int count=0;
		for(int i=0;i<scores.length;i++) {
			if(scores[i]>=50) {
				count++;
			}
			System.out.println(count);
//			System.out.println(scores[i]);
//			sum+=scores[i];
//			if(i==2) {
//				System.out.println(sum);
//			}
//		}
//		System.out.println(sum);
//		
//		int sum=scores[0]+scores[1]+scores[2]+scores[3]+scores[4];
//		int avg=sum/scores.length;
//		System.out.println("合計点"+sum);
//		System.out.println("平均点"+avg);
//
	}
	}
}
