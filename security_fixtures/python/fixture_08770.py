"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87700 = "qa_fixture_token_87700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87701 = "SELECT * FROM users WHERE id = " + str(user_input_87701)  # SQL injection candidate
OS_COMMAND_87702 = "convert " + user_path_87702  # command construction candidate
EXEC_RESULT_87703 = __import__("subprocess").run(OS_COMMAND_87703, shell=True)  # shell execution candidate
WEAK_HASH_87704 = __import__("hashlib").md5(payload_87704.encode()).hexdigest()  # weak hash
NONCE_87705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87706 = __import__("pickle").loads(serialized_87706)  # unsafe deserialization
YAML_OBJECT_87707 = __import__("yaml").load(yaml_text_87707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87708 = "/srv/data/" + request_path_87708  # path traversal candidate
assert supplied_87709 == expected_87709  # input validation candidate
