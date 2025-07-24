import matplotlib # Import matplotlib first
matplotlib.use('TkAgg') # Set the backend to TkAgg BEFORE importing pyplot
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def plot_vector_error_map(csv_filepath):
    """
    Reads data from a CSV file (specified by path) and plots a 2D vector error map.
    (Rest of the docstring and function code remains the same)
    """
    try:
        # Read the data from the CSV file
        data = pd.read_csv(csv_filepath)

        # Ensure the required columns exist
        required_columns = ['x', 'y', 'x_error', 'y_error']
        if not all(col in data.columns for col in required_columns):
            print(f"Error: CSV file must contain the columns: {', '.join(required_columns)}")
            print(f"Found columns: {data.columns.tolist()}")
            return

        x = data['x']
        y = data['y']
        x_error = data['x_error']
        y_error = data['y_error']

        # Create the plot
        plt.figure(figsize=(10, 8))
        
        plt.scatter(x, y, color='blue', s=10, label='Data Points (x,y)')
        plt.quiver(x, y, x_error, y_error, 
                   angles='xy', scale_units='xy', scale=1, 
                   color='red', alpha=0.7, width=0.003, label='Error Vectors (dx, dy)')

        plt.xlabel("X coordinate")
        plt.ylabel("Y coordinate")
        plt.title("2D Vector Error Map")
        plt.axhline(0, color='grey', lw=0.5)
        plt.axvline(0, color='grey', lw=0.5)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        
        plot_min_x = (x + x_error).min() - 0.1 if not x.empty else -1
        plot_max_x = (x + x_error).max() + 0.1 if not x.empty else 1
        plot_min_y = (y + y_error).min() - 0.1 if not y.empty else -1
        plot_max_y = (y + y_error).max() + 0.1 if not y.empty else 1
        
        # Handle empty data for limits
        final_xlim_min = min(0, plot_min_x) if not x.empty else -1
        final_xlim_max = max(1, plot_max_x) if not x.empty else 1
        final_ylim_min = min(0, plot_min_y) if not y.empty else -1
        final_ylim_max = max(1, plot_max_y) if not y.empty else 1

        plt.xlim(final_xlim_min, final_xlim_max)
        plt.ylim(final_ylim_min, final_ylim_max)


        plt.gca().set_aspect('equal', adjustable='box')

        plt.show() # This should now work with TkAgg

    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_filepath}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a 2D vector error map from a CSV file.")
    parser.add_argument("csv_filepath", help="Path to the input CSV file containing x, y, x_error, y_error columns.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the plotting function with the provided filepath
    plot_vector_error_map(args.csv_filepath)