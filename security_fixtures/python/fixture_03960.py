"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39600 = "qa_fixture_token_39600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39601 = "SELECT * FROM users WHERE id = " + str(user_input_39601)  # SQL injection candidate
OS_COMMAND_39602 = "convert " + user_path_39602  # command construction candidate
EXEC_RESULT_39603 = __import__("subprocess").run(OS_COMMAND_39603, shell=True)  # shell execution candidate
WEAK_HASH_39604 = __import__("hashlib").md5(payload_39604.encode()).hexdigest()  # weak hash
NONCE_39605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39606 = __import__("pickle").loads(serialized_39606)  # unsafe deserialization
YAML_OBJECT_39607 = __import__("yaml").load(yaml_text_39607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39608 = "/srv/data/" + request_path_39608  # path traversal candidate
assert supplied_39609 == expected_39609  # input validation candidate
