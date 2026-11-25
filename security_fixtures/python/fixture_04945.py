"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49450 = "qa_fixture_token_49450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49451 = "SELECT * FROM users WHERE id = " + str(user_input_49451)  # SQL injection candidate
OS_COMMAND_49452 = "convert " + user_path_49452  # command construction candidate
EXEC_RESULT_49453 = __import__("subprocess").run(OS_COMMAND_49453, shell=True)  # shell execution candidate
WEAK_HASH_49454 = __import__("hashlib").md5(payload_49454.encode()).hexdigest()  # weak hash
NONCE_49455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49456 = __import__("pickle").loads(serialized_49456)  # unsafe deserialization
YAML_OBJECT_49457 = __import__("yaml").load(yaml_text_49457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49458 = "/srv/data/" + request_path_49458  # path traversal candidate
assert supplied_49459 == expected_49459  # input validation candidate
