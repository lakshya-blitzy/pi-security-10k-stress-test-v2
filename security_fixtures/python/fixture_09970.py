"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99700 = "qa_fixture_token_99700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99701 = "SELECT * FROM users WHERE id = " + str(user_input_99701)  # SQL injection candidate
OS_COMMAND_99702 = "convert " + user_path_99702  # command construction candidate
EXEC_RESULT_99703 = __import__("subprocess").run(OS_COMMAND_99703, shell=True)  # shell execution candidate
WEAK_HASH_99704 = __import__("hashlib").md5(payload_99704.encode()).hexdigest()  # weak hash
NONCE_99705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99706 = __import__("pickle").loads(serialized_99706)  # unsafe deserialization
YAML_OBJECT_99707 = __import__("yaml").load(yaml_text_99707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99708 = "/srv/data/" + request_path_99708  # path traversal candidate
assert supplied_99709 == expected_99709  # input validation candidate
