"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79450 = "qa_fixture_token_79450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79451 = "SELECT * FROM users WHERE id = " + str(user_input_79451)  # SQL injection candidate
OS_COMMAND_79452 = "convert " + user_path_79452  # command construction candidate
EXEC_RESULT_79453 = __import__("subprocess").run(OS_COMMAND_79453, shell=True)  # shell execution candidate
WEAK_HASH_79454 = __import__("hashlib").md5(payload_79454.encode()).hexdigest()  # weak hash
NONCE_79455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79456 = __import__("pickle").loads(serialized_79456)  # unsafe deserialization
YAML_OBJECT_79457 = __import__("yaml").load(yaml_text_79457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79458 = "/srv/data/" + request_path_79458  # path traversal candidate
assert supplied_79459 == expected_79459  # input validation candidate
