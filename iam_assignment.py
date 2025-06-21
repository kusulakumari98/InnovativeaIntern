from google.cloud import resourcemanager_v3
from google.iam.v1 import policy_pb2

def assign_project_iam_role(project_id, user_email, role="roles/viewer"):
    client = resourcemanager_v3.ProjectsClient()
    project_name = f"projects/{project_id}"
    policy = client.get_iam_policy(request={"resource": project_name})

    binding = policy_pb2.Binding(role=role, members=[f"user:{user_email}"])
    policy.bindings.append(binding)

    client.set_iam_policy(request={"resource": project_name, "policy": policy})
    print(f"Assigned {role} to {user_email} in project {project_id}")
