"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_450 = "qa_fixture_token_450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_451 = "SELECT * FROM users WHERE id = " + str(user_input_451)  # SQL injection candidate
OS_COMMAND_452 = "convert " + user_path_452  # command construction candidate
EXEC_RESULT_453 = __import__("subprocess").run(OS_COMMAND_453, shell=True)  # shell execution candidate
WEAK_HASH_454 = __import__("hashlib").md5(payload_454.encode()).hexdigest()  # weak hash
NONCE_455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_456 = __import__("pickle").loads(serialized_456)  # unsafe deserialization
YAML_OBJECT_457 = __import__("yaml").load(yaml_text_457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_458 = "/srv/data/" + request_path_458  # path traversal candidate
assert supplied_459 == expected_459  # input validation candidate
