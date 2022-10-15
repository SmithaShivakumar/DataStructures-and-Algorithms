import collections
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # Return a dictionary(char_frequency_dict) with the frequency of repetitive characters Ex:apple={'a':1,'p':2,'l':1,'e':1}
        char_frequency_dict = collections.Counter(s)
		#Take a variable counter to check the position of Key press (First/Second/Third)
        counter,ans=0,0
        for ind,freq in enumerate(sorted(char_frequency_dict.values(), reverse=True)):
			# Counter will only increase when ind is divisble by 9 i.e 0,9,18
			#Ex:Counter=1 holds 0-8 key,value of char_frequency_dict 
            #Ex:Counter=2 holds 9 to 17 key:value of char_frequency_dict so on
            if ind%9==0:
                counter += 1
            ans += freq*counter
        return ans