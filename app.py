from workflows.support_workflow import (
    run_support_workflow
)

query = input(
    "Enter Customer Query: "
)

result = run_support_workflow(
    query
)

print(result)
