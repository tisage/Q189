// check a string has all unique characters

package arraysStrings;

public class Q1 {

	public Q1() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		if (IsUniqueString("abc"))
			System.out.println("Unique.");
		else
			System.out.println("Not Unique.");
	}

	static boolean IsUniqueString(String str) {
		if (str.length() > 128)
			return false;
		boolean char_set[] = new boolean[128]; // default is false

		for (int i = 0; i < str.length(); i++) {
			int val = str.charAt(i); // return the ASCII value of a character
			System.out.println(val);

			if (char_set[val]) // check if has before
				return false; // has, return not unique.
			char_set[val] = true; // set has in the char_set table
		}
		return true;
	}

}
