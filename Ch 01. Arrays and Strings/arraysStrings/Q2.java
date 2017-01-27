// check two strings, whether one is a permutation of the other
// Pay attention: it's a string not an string array

package arraysStrings;

import java.util.Arrays;

public class Q2 {

	public Q2() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a = "abc";
		String b = "cab";
		if (IsPermutation(a, b))
			System.out.println("Is Permutation.");
		else
			System.out.println("Not Permutation.");
	}

	static boolean IsPermutation(String a, String b) {
		if (a.length() != b.length()) // assume that subset is not a permutation
			return false;

		char[] content1 = a.toCharArray(); // single string to a char array
		char[] content2 = b.toCharArray();

		Arrays.sort(content1); // sort array
		Arrays.sort(content2);

		String sorted_a = new String(content1); // call constructor
		String sorted_b = new String(content2);

		return (sorted_a).equals(sorted_b);
	}

}
