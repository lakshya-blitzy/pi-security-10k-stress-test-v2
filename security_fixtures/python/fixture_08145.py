"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81450 = "qa_fixture_token_81450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81451 = "SELECT * FROM users WHERE id = " + str(user_input_81451)  # SQL injection candidate
OS_COMMAND_81452 = "convert " + user_path_81452  # command construction candidate
EXEC_RESULT_81453 = __import__("subprocess").run(OS_COMMAND_81453, shell=True)  # shell execution candidate
WEAK_HASH_81454 = __import__("hashlib").md5(payload_81454.encode()).hexdigest()  # weak hash
NONCE_81455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81456 = __import__("pickle").loads(serialized_81456)  # unsafe deserialization
YAML_OBJECT_81457 = __import__("yaml").load(yaml_text_81457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81458 = "/srv/data/" + request_path_81458  # path traversal candidate
assert supplied_81459 == expected_81459  # input validation candidate
