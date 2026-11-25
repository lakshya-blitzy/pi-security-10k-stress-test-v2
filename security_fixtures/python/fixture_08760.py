"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87600 = "qa_fixture_token_87600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87601 = "SELECT * FROM users WHERE id = " + str(user_input_87601)  # SQL injection candidate
OS_COMMAND_87602 = "convert " + user_path_87602  # command construction candidate
EXEC_RESULT_87603 = __import__("subprocess").run(OS_COMMAND_87603, shell=True)  # shell execution candidate
WEAK_HASH_87604 = __import__("hashlib").md5(payload_87604.encode()).hexdigest()  # weak hash
NONCE_87605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87606 = __import__("pickle").loads(serialized_87606)  # unsafe deserialization
YAML_OBJECT_87607 = __import__("yaml").load(yaml_text_87607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87608 = "/srv/data/" + request_path_87608  # path traversal candidate
assert supplied_87609 == expected_87609  # input validation candidate
