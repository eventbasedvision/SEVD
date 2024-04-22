import carla
import random
import logging
import math

# @todo cannot import these directly.
SpawnActor = carla.command.SpawnActor
SetAutopilot = carla.command.SetAutopilot
SetVehicleLightState = carla.command.SetVehicleLightState
FutureActor = carla.command.FutureActor


def spawnVehicles(client, world, spawn_points, blueprintsVehicles, number):
    print("Spawning vehicles...")
    customBp = {
        'vehicle.bh.crossbike': 8,
        'vehicle.carlamotors.firetruck': 3,
        'vehicle.ford.ambulance': 3,
        'vehicle.dodge.charger_police': 6,
        'vehicle.mercedes.coupe': 7,
        'vehicle.tesla.model3': 7,
        'vehicle.audi.a2': 7,
        'vehicle.jeep.wrangler_rubicon': 7,
        'vehicle.tesla.cybertruck': 3,
        'vehicle.ford.mustang': 8,
        'vehicle.toyota.prius': 8,
        'vehicle.kawasaki.ninja': 11,
        'vehicle.vespa.zx125': 11,
        'vehicle.harley-davidson.low_rider': 11
    }

    batch = []
    if number < 10:
        for i in range(number):
            spawn_point = random.choice(spawn_points)
            vehicle_bp = "vehicle.tesla.model3"
            batch.append(carla.command.SpawnActor(vehicle_bp, spawn_point).then(
                carla.command.SetAutopilot(carla.command.FutureActor, True)))
    else:

        for model, percentage in customBp.items():
            num_per_blueprint = math.floor((number * percentage)/100)
            vehicle_bp = world.get_blueprint_library().find(model)
            for _ in range(num_per_blueprint):
                spawn_point = random.choice(spawn_points)
                batch.append(carla.command.SpawnActor(vehicle_bp, spawn_point).then(
                    carla.command.SetAutopilot(carla.command.FutureActor, True)))

    results = client.apply_batch_sync(batch, True)

    all_id = [results[i].actor_id for i in range(len(results))]
    all_actors = world.get_actors(all_id)
    return all_actors, all_id


def spawnWalkers(client, world, blueprintsWalkers, number):
    print("Spawning walkers...")
    # 1. Take all the random locations to spawn
    spawn_points = []
    for i in range(number):
        spawn_point = carla.Transform()
        spawn_point.location = world.get_random_location_from_navigation()
        if (spawn_point.location != None):
            spawn_points.append(spawn_point)

    # 2. Build the batch of commands to spawn the pedestrians
    batch = []
    for spawn_point in spawn_points:
        walker_bp = random.choice(blueprintsWalkers)
        batch.append(carla.command.SpawnActor(walker_bp, spawn_point))

    # 2.1 apply the batch
    results = client.apply_batch_sync(batch, True)
    walkers_list = []
    for i in range(len(results)):
        walkers_list.append({"id": results[i].actor_id})

    # 3. Spawn walker AI controllers for each walker
    batch = []
    walker_controller_bp = world.get_blueprint_library().find('controller.ai.walker')

    for i in range(len(walkers_list)):
        batch.append(carla.command.SpawnActor(walker_controller_bp,
                     carla.Transform(), walkers_list[i]["id"]))

    # 3.1 apply the batch
    results = client.apply_batch_sync(batch, True)
    for i in range(len(results)):
        walkers_list[i]["con"] = results[i].actor_id

    # 4. Put altogether the walker and controller ids
    all_id = []
    for i in range(len(walkers_list)):
        all_id.append(walkers_list[i]["con"])
        all_id.append(walkers_list[i]["id"])
    all_actors = world.get_actors(all_id)

    # wait for a tick to ensure client receives the last transform of the walkers we have just created
    world.tick()

    # 5. initialize each controller and set target to walk to (list is [controller, actor, controller, actor ...])
    for i in range(0, len(all_actors), 2):
        # start walker
        all_actors[i].start()
        # set walk to random point
        all_actors[i].go_to_location(
            world.get_random_location_from_navigation())
        # random max speed
        # max speed between 1 and 2 (default is 1.4 m/s)
        all_actors[i].set_max_speed(1 + random.random())
    return all_actors, all_id
