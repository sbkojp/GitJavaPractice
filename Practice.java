package ch4;

public class Practice {

	public static void main(String[] args) {
//		
//		int[] moneyList= {121902,8302,55100};
//		for(int i=0;i<moneyList.length;i++) {
//			System.out.println(moneyList[i]);
//		}
//		System.out.println();
//		
//		
//		int[][] moneyList1= {{121902,8302,55100},{221902,2302,25100}};
//		for(int i=0;i<moneyList1.length;i++) {
//			for(int j=0;j<moneyList1[i].length;j++) {
//			System.out.println(moneyList1[i][j]);
//			}
//			System.out.println();
//		}
//		
//		for(int[] zandaka1:moneyList1) {
//			for(int zandaka2:zandaka1) {
//			System.out.println(zandaka2);
//			}
//			System.out.println();
//		}
//		System.out.println();
//		
//		
//		for(int zandaka: moneyList) {
//			System.out.println(zandaka);
//		}
//		System.out.println();
//		
//		
//		int[] numbers= {3,4,9};
//		for(int i=0;i<numbers.length;i++) {
//			System.out.print("1桁の数字を入力してください>");
//			int intput = new java.util.Scanner(System.in).nextInt();
//			if(intput==numbers[i]) {
//				System.out.println("アタリ！");
//			}
//		}
//		System.out.println();
//		
//		int[] numbers1= {3,4,9};
//		for(int nmb:numbers1) {
//			System.out.print("1桁の数字を入力してください>");
//			int intput = new java.util.Scanner(System.in).nextInt();
//			if(intput==nmb) {
//				System.out.println("アタリ！");
//			}
//		}
//		
		int[] integer =new int[10];
		System.out.println("配列を全部出力...");
		for(int i=0;i<integer.length;i++) {
			integer[i]=new java.util.Random().nextInt(100)+1;
			System.out.println(integer[i]);
			
		}
		System.out.println();
		
		System.out.println("配列のうち偶数は...");
		for(int i=0;i<integer.length;i++) {
			if(integer[i]%2==0) {
				System.out.println(integer[i]);
			}
			}
		System.out.println();
		
		System.out.println("配列のうち奇数は...");
		for(int i=0;i<integer.length;i++) {
			if(integer[i]%2!=0) {
				System.out.println(integer[i]);
			}
			}
		System.out.println();
		
		
		System.out.print("名前を入力してください-＞");
		String name=new java.util.Scanner(System.in).nextLine();
		System.out.print("年齢を入力してください-＞");
		String ageString=new java.util.Scanner(System.in).nextLine();
		int age=Integer.parseInt(ageString);
		String[] omikuji= {"大吉","中吉","吉","凶"};
		int fortune=new java.util.Random().nextInt(omikuji.length);
		System.out.println(name+"さん("+age+")の今日の運勢は..."+omikuji[fortune]+"です。");
		
		
		
		

		

		
		
		

	}

}
