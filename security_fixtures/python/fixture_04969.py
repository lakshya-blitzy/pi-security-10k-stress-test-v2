"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49690 = "qa_fixture_token_49690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49691 = "SELECT * FROM users WHERE id = " + str(user_input_49691)  # SQL injection candidate
OS_COMMAND_49692 = "convert " + user_path_49692  # command construction candidate
EXEC_RESULT_49693 = __import__("subprocess").run(OS_COMMAND_49693, shell=True)  # shell execution candidate
WEAK_HASH_49694 = __import__("hashlib").md5(payload_49694.encode()).hexdigest()  # weak hash
NONCE_49695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49696 = __import__("pickle").loads(serialized_49696)  # unsafe deserialization
YAML_OBJECT_49697 = __import__("yaml").load(yaml_text_49697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49698 = "/srv/data/" + request_path_49698  # path traversal candidate
assert supplied_49699 == expected_49699  # input validation candidate
