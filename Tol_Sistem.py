import simpy
import random
import matplotlib.pyplot as plt
import csv

# Parameter simulasi
RANDOM_SEED = 42
SIM_TIME = 3600  # Simulasi 1 jam (3600 detik)
ARRIVAL_RATE = 48  # Kedatangan kendaraan per menit (bisa bervariasi)
SERVICE_TIME = 4  # Waktu layanan di tol elektronik (detik)
NUM_TOLL_BOOTHS = 3  # Jumlah gerbang tol

random.seed(RANDOM_SEED)

wait_times = []
time_stamps = []
vehicle_data = []

def vehicle(env, name, toll_booth, payment_type):
    arrival_time = env.now
    print(f"{name} tiba di tol pada {arrival_time:.2f}s dengan metode {payment_type}")
    
    with toll_booth.request() as request:
        yield request  # Menunggu giliran di gerbang tol
        service_time = SERVICE_TIME
        wait_time = env.now - arrival_time
        wait_times.append(wait_time)
        time_stamps.append(env.now)
        yield env.timeout(service_time)  # Proses pembayaran tol
        exit_time = env.now
        print(f"{name} keluar dari tol pada {exit_time:.2f}s (waktu tunggu {wait_time:.2f}s)")
        vehicle_data.append([name, arrival_time, payment_type, exit_time, wait_time])

def generate_vehicles(env, toll_booth):
    vehicle_count = 0
    while True:
        yield env.timeout(random.expovariate(ARRIVAL_RATE / 60))  # Kendaraan datang secara acak
        vehicle_count += 1
        env.process(vehicle(env, f"Kendaraan-{vehicle_count}", toll_booth, "electronic"))

# Setup environment dan resource
env = simpy.Environment()
toll_booth = simpy.Resource(env, capacity=NUM_TOLL_BOOTHS)
env.process(generate_vehicles(env, toll_booth))

# Jalankan simulasi
env.run(until=SIM_TIME)

# Simulasi summary
if wait_times:
    avg_wait_time = sum(wait_times) / len(wait_times)
    max_wait_time = max(wait_times)
    min_wait_time = min(wait_times)
    print("\nSimulation Summary:")
    print(f"Average Wait Time: {avg_wait_time:.2f} seconds")
    print(f"Max Wait Time: {max_wait_time:.2f} seconds")
    print(f"Min Wait Time: {min_wait_time:.2f} seconds")

    # Simpan ke CSV
    with open("simulation_results_WE.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Vehicle", "Arrival Time", "Payment Type", "Exit Time", "Wait Time"])
        writer.writerows(vehicle_data)
    print("Hasil simulasi disimpan ke toll_simulation_results.csv")
    
    # Visualisasi hasil dengan grafik garis
    plt.figure(figsize=(10, 5))
    plt.plot(time_stamps, wait_times, marker='o', linestyle='-', color='b', alpha=0.7, label='Wait Times')
    
    # Add average wait time line
    avg_line = [avg_wait_time] * len(time_stamps)
    plt.plot(time_stamps, avg_line, linestyle='--', color='r', label=f'Average ({avg_wait_time:.2f}s)')
    
    plt.xlabel("Simulation Time (seconds)")
    plt.ylabel("Wait Time (seconds)")
    plt.title("Customer Wait Time vs Simulation Time in [WeekEnd 6 Gate]")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('simulation_graph_WE.png')  # Save the graph
    plt.show()
else:
    print("\nNo vehicles were processed.")
