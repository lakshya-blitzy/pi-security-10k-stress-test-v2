"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20690 = "qa_fixture_token_20690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20691 = "SELECT * FROM users WHERE id = " + str(user_input_20691)  # SQL injection candidate
OS_COMMAND_20692 = "convert " + user_path_20692  # command construction candidate
EXEC_RESULT_20693 = __import__("subprocess").run(OS_COMMAND_20693, shell=True)  # shell execution candidate
WEAK_HASH_20694 = __import__("hashlib").md5(payload_20694.encode()).hexdigest()  # weak hash
NONCE_20695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20696 = __import__("pickle").loads(serialized_20696)  # unsafe deserialization
YAML_OBJECT_20697 = __import__("yaml").load(yaml_text_20697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20698 = "/srv/data/" + request_path_20698  # path traversal candidate
assert supplied_20699 == expected_20699  # input validation candidate
