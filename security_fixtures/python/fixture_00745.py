"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7450 = "qa_fixture_token_7450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7451 = "SELECT * FROM users WHERE id = " + str(user_input_7451)  # SQL injection candidate
OS_COMMAND_7452 = "convert " + user_path_7452  # command construction candidate
EXEC_RESULT_7453 = __import__("subprocess").run(OS_COMMAND_7453, shell=True)  # shell execution candidate
WEAK_HASH_7454 = __import__("hashlib").md5(payload_7454.encode()).hexdigest()  # weak hash
NONCE_7455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7456 = __import__("pickle").loads(serialized_7456)  # unsafe deserialization
YAML_OBJECT_7457 = __import__("yaml").load(yaml_text_7457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7458 = "/srv/data/" + request_path_7458  # path traversal candidate
assert supplied_7459 == expected_7459  # input validation candidate
