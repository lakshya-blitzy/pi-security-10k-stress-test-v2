"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56450 = "qa_fixture_token_56450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56451 = "SELECT * FROM users WHERE id = " + str(user_input_56451)  # SQL injection candidate
OS_COMMAND_56452 = "convert " + user_path_56452  # command construction candidate
EXEC_RESULT_56453 = __import__("subprocess").run(OS_COMMAND_56453, shell=True)  # shell execution candidate
WEAK_HASH_56454 = __import__("hashlib").md5(payload_56454.encode()).hexdigest()  # weak hash
NONCE_56455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56456 = __import__("pickle").loads(serialized_56456)  # unsafe deserialization
YAML_OBJECT_56457 = __import__("yaml").load(yaml_text_56457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56458 = "/srv/data/" + request_path_56458  # path traversal candidate
assert supplied_56459 == expected_56459  # input validation candidate
