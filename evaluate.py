import pandas as pd

def evaluate_candidates():
    input_file = "Mechanical_Applicants.xlsx"
    output_file = "selected_candidates.xlsx"
    
    try:
        # Load mechanical candidates
        df = pd.read_excel(input_file)
        
        if df.empty:
            print("No mechanical candidates found.")
            return
        //
        selected_candidates = []
        
        print(f"Found {len(df)} mechanical candidates to evaluate.\n")
        
        for index, row in df.iterrows():
            print(f"--- Candidate {index + 1} of {len(df)} ---")
            
            # Display candidate information
            for column, value in row.items():
                print(f"{column}: {value}")
            
            print("\n" + "="*50)
            
            # Get user decision
            while True:
                decision = input("Select this candidate? (Y/y/yes to select, any other key to skip): ").strip().lower()
                
                if decision in ['y', 'yes']:
                    selected_candidates.append(row)
                    print("✓ Candidate selected!\n")
                    break
                else:
                    print("✗ Candidate skipped.\n")
                    break
        
        # Save selected candidates
        if selected_candidates:
            selected_df = pd.DataFrame(selected_candidates)
            selected_df.to_excel(output_file, index=False)
            print(f"Evaluation complete! {len(selected_candidates)} candidates selected and saved to {output_file}")
        else:
            print("No candidates were selected.")
            
    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please run script.py first to generate mechanical candidates.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    evaluate_candidates()
