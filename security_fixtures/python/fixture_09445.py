"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94450 = "qa_fixture_token_94450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94451 = "SELECT * FROM users WHERE id = " + str(user_input_94451)  # SQL injection candidate
OS_COMMAND_94452 = "convert " + user_path_94452  # command construction candidate
EXEC_RESULT_94453 = __import__("subprocess").run(OS_COMMAND_94453, shell=True)  # shell execution candidate
WEAK_HASH_94454 = __import__("hashlib").md5(payload_94454.encode()).hexdigest()  # weak hash
NONCE_94455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94456 = __import__("pickle").loads(serialized_94456)  # unsafe deserialization
YAML_OBJECT_94457 = __import__("yaml").load(yaml_text_94457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94458 = "/srv/data/" + request_path_94458  # path traversal candidate
assert supplied_94459 == expected_94459  # input validation candidate
