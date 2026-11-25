"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22700 = "qa_fixture_token_22700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22701 = "SELECT * FROM users WHERE id = " + str(user_input_22701)  # SQL injection candidate
OS_COMMAND_22702 = "convert " + user_path_22702  # command construction candidate
EXEC_RESULT_22703 = __import__("subprocess").run(OS_COMMAND_22703, shell=True)  # shell execution candidate
WEAK_HASH_22704 = __import__("hashlib").md5(payload_22704.encode()).hexdigest()  # weak hash
NONCE_22705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22706 = __import__("pickle").loads(serialized_22706)  # unsafe deserialization
YAML_OBJECT_22707 = __import__("yaml").load(yaml_text_22707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22708 = "/srv/data/" + request_path_22708  # path traversal candidate
assert supplied_22709 == expected_22709  # input validation candidate
