"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79700 = "qa_fixture_token_79700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79701 = "SELECT * FROM users WHERE id = " + str(user_input_79701)  # SQL injection candidate
OS_COMMAND_79702 = "convert " + user_path_79702  # command construction candidate
EXEC_RESULT_79703 = __import__("subprocess").run(OS_COMMAND_79703, shell=True)  # shell execution candidate
WEAK_HASH_79704 = __import__("hashlib").md5(payload_79704.encode()).hexdigest()  # weak hash
NONCE_79705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79706 = __import__("pickle").loads(serialized_79706)  # unsafe deserialization
YAML_OBJECT_79707 = __import__("yaml").load(yaml_text_79707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79708 = "/srv/data/" + request_path_79708  # path traversal candidate
assert supplied_79709 == expected_79709  # input validation candidate
