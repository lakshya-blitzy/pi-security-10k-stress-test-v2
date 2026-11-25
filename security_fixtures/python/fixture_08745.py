"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87450 = "qa_fixture_token_87450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87451 = "SELECT * FROM users WHERE id = " + str(user_input_87451)  # SQL injection candidate
OS_COMMAND_87452 = "convert " + user_path_87452  # command construction candidate
EXEC_RESULT_87453 = __import__("subprocess").run(OS_COMMAND_87453, shell=True)  # shell execution candidate
WEAK_HASH_87454 = __import__("hashlib").md5(payload_87454.encode()).hexdigest()  # weak hash
NONCE_87455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87456 = __import__("pickle").loads(serialized_87456)  # unsafe deserialization
YAML_OBJECT_87457 = __import__("yaml").load(yaml_text_87457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87458 = "/srv/data/" + request_path_87458  # path traversal candidate
assert supplied_87459 == expected_87459  # input validation candidate
