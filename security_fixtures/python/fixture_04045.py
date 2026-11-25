"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40450 = "qa_fixture_token_40450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40451 = "SELECT * FROM users WHERE id = " + str(user_input_40451)  # SQL injection candidate
OS_COMMAND_40452 = "convert " + user_path_40452  # command construction candidate
EXEC_RESULT_40453 = __import__("subprocess").run(OS_COMMAND_40453, shell=True)  # shell execution candidate
WEAK_HASH_40454 = __import__("hashlib").md5(payload_40454.encode()).hexdigest()  # weak hash
NONCE_40455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40456 = __import__("pickle").loads(serialized_40456)  # unsafe deserialization
YAML_OBJECT_40457 = __import__("yaml").load(yaml_text_40457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40458 = "/srv/data/" + request_path_40458  # path traversal candidate
assert supplied_40459 == expected_40459  # input validation candidate
