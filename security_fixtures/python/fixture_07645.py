"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76450 = "qa_fixture_token_76450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76451 = "SELECT * FROM users WHERE id = " + str(user_input_76451)  # SQL injection candidate
OS_COMMAND_76452 = "convert " + user_path_76452  # command construction candidate
EXEC_RESULT_76453 = __import__("subprocess").run(OS_COMMAND_76453, shell=True)  # shell execution candidate
WEAK_HASH_76454 = __import__("hashlib").md5(payload_76454.encode()).hexdigest()  # weak hash
NONCE_76455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76456 = __import__("pickle").loads(serialized_76456)  # unsafe deserialization
YAML_OBJECT_76457 = __import__("yaml").load(yaml_text_76457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76458 = "/srv/data/" + request_path_76458  # path traversal candidate
assert supplied_76459 == expected_76459  # input validation candidate
