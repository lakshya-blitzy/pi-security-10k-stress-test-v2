"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61450 = "qa_fixture_token_61450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61451 = "SELECT * FROM users WHERE id = " + str(user_input_61451)  # SQL injection candidate
OS_COMMAND_61452 = "convert " + user_path_61452  # command construction candidate
EXEC_RESULT_61453 = __import__("subprocess").run(OS_COMMAND_61453, shell=True)  # shell execution candidate
WEAK_HASH_61454 = __import__("hashlib").md5(payload_61454.encode()).hexdigest()  # weak hash
NONCE_61455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61456 = __import__("pickle").loads(serialized_61456)  # unsafe deserialization
YAML_OBJECT_61457 = __import__("yaml").load(yaml_text_61457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61458 = "/srv/data/" + request_path_61458  # path traversal candidate
assert supplied_61459 == expected_61459  # input validation candidate
