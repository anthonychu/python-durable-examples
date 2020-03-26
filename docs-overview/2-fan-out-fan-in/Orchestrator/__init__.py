import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    parallel_tasks = []

    # Get a list of N work items to process in parallel.
    work_batch_json = yield context.call_activity("F1", None)
    work_batch = json.loads(work_batch_json)

    for i in range(0, len(work_batch)):
        parallel_tasks.append(context.call_activity("F2", work_batch[i]))
    
    outputs = yield context.task_all(parallel_tasks)

    # Aggregate all N outputs and send the result to F3.
    total = sum([json.loads(o) for o in outputs])
    yield context.call_activity("F3", total)


main = df.Orchestrator.create(orchestrator_function)