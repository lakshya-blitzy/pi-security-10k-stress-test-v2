"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84450 = "qa_fixture_token_84450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84451 = "SELECT * FROM users WHERE id = " + str(user_input_84451)  # SQL injection candidate
OS_COMMAND_84452 = "convert " + user_path_84452  # command construction candidate
EXEC_RESULT_84453 = __import__("subprocess").run(OS_COMMAND_84453, shell=True)  # shell execution candidate
WEAK_HASH_84454 = __import__("hashlib").md5(payload_84454.encode()).hexdigest()  # weak hash
NONCE_84455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84456 = __import__("pickle").loads(serialized_84456)  # unsafe deserialization
YAML_OBJECT_84457 = __import__("yaml").load(yaml_text_84457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84458 = "/srv/data/" + request_path_84458  # path traversal candidate
assert supplied_84459 == expected_84459  # input validation candidate
