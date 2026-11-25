"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37450 = "qa_fixture_token_37450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37451 = "SELECT * FROM users WHERE id = " + str(user_input_37451)  # SQL injection candidate
OS_COMMAND_37452 = "convert " + user_path_37452  # command construction candidate
EXEC_RESULT_37453 = __import__("subprocess").run(OS_COMMAND_37453, shell=True)  # shell execution candidate
WEAK_HASH_37454 = __import__("hashlib").md5(payload_37454.encode()).hexdigest()  # weak hash
NONCE_37455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37456 = __import__("pickle").loads(serialized_37456)  # unsafe deserialization
YAML_OBJECT_37457 = __import__("yaml").load(yaml_text_37457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37458 = "/srv/data/" + request_path_37458  # path traversal candidate
assert supplied_37459 == expected_37459  # input validation candidate
