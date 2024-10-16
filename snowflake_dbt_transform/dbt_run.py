import subprocess

def transform_data():
    try:
        result = subprocess.run("dbt run --profiles-dir ./profile",
                                check=True,
                                capture_output=True,
                                text=True)
        print("Command Output:\n", result.stdout)

    except subprocess.CalledProcessError as e:
        print("Error while running dbt command:", e)
        print("Output:", e.output)
        print("Error:", e.stderr)

if __name__ == "__main__":
    transform_data()
