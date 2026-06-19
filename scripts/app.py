#importing the necessary Libraries
import argparse
#import sys

#print(sys.argv[5])

#creating methods in order to modularize the code and make it more readable 

def get_arguments()->  argparse.Namespace:
    """"This method is used to get the arguments from the command line
    Returns:
        argparse.Namespace: The arguments from the command line
    """
    parser = argparse.ArgumentParser( prog="BcParks",
                                     description="This entire script examines my skills of working with CLI",
                                     epilog="Learning how to interact with the terminal via argparse is impressive")
    parser.add_argument("-m","--model",default="Dinov3")
    
    return parser.parse_args()
    
   

def main():
    

    
    print(f"{get_arguments().model}")
    
    
if __name__=="__main__":
    main()
    