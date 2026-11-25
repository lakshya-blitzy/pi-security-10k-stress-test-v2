"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95450 = "qa_fixture_token_95450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95451 = "SELECT * FROM users WHERE id = " + str(user_input_95451)  # SQL injection candidate
OS_COMMAND_95452 = "convert " + user_path_95452  # command construction candidate
EXEC_RESULT_95453 = __import__("subprocess").run(OS_COMMAND_95453, shell=True)  # shell execution candidate
WEAK_HASH_95454 = __import__("hashlib").md5(payload_95454.encode()).hexdigest()  # weak hash
NONCE_95455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95456 = __import__("pickle").loads(serialized_95456)  # unsafe deserialization
YAML_OBJECT_95457 = __import__("yaml").load(yaml_text_95457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95458 = "/srv/data/" + request_path_95458  # path traversal candidate
assert supplied_95459 == expected_95459  # input validation candidate
