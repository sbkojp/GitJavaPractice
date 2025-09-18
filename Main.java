package ch4;

public class Main {

	public static void main(String[] args) {
//		String[]fortunes= {"大吉","中吉","吉","末吉","小吉","凶"};
//		String[]EgFortunes= {"Exselent","luckey","unluckey"};
//				int[]fortuneNumbers=new int[10];
//		for(int i=0;i<fortuneNumbers.length;i++) {
//			fortuneNumbers[i]=(int)(Math.random()*6);
//		}
//		for(int num:fortuneNumbers) {
//			System.out.println(num+":"+fortunes[num]);
//			System.out.println(num+":"+EgFortunes[num]);
//			System.out.println();
//		}
		int[]arrayA= {1,2,3};
		int[]arrayB;
		arrayB=arrayA;
		arrayB[1]=100;
		System.out.println(arrayA[1]);
		
		
		int A= 1;
		int B;
		B=A;
		B=100;
		System.out.println(A);
		
		int[]array= {1,2,6};
		for(int num:array) {
			int i=1;
			while(i<=num) {
				System.out.println(i++);
			}
		}
		
		
//		int[] seq =new int[10];
//		for(int i=0;i<seq.length;i++) {
//			seq[i]=new java.util.Random().nextInt(4);
//			System.out.print(seq[i]);
//		}
//		System.out.println();
//		char[] base= {'A','T','G','C'};
//		for(int i=0;i<seq.length;i++) {
//			System.out.print(base[seq[i]]);
//		}
//		System.out.println();
//		
//		String[] array= {"大吉","中吉","吉","凶"};
//		int ran=(int)(Math.random()*4);
//		System.out.println(array[ran]);
//		System.out.println(ran);
//		
//		for(int num:seq) {
//			System.out.print(base[num]);//拡張For文
//		}
//		
		
		
		
		
		
//		int[]scores = {20,30,40,50,80};
//		int count=0;
//		for(int i=0;i<scores.length;i++) {
//			if(scores[i]>=50) {
//				count++;
//			}
//		}
//			System.out.println("50点以上の科目の数"+count);
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
