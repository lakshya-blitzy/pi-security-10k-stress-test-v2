"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87840 = "qa_fixture_token_87840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87841 = "SELECT * FROM users WHERE id = " + str(user_input_87841)  # SQL injection candidate
OS_COMMAND_87842 = "convert " + user_path_87842  # command construction candidate
EXEC_RESULT_87843 = __import__("subprocess").run(OS_COMMAND_87843, shell=True)  # shell execution candidate
WEAK_HASH_87844 = __import__("hashlib").md5(payload_87844.encode()).hexdigest()  # weak hash
NONCE_87845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87846 = __import__("pickle").loads(serialized_87846)  # unsafe deserialization
YAML_OBJECT_87847 = __import__("yaml").load(yaml_text_87847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87848 = "/srv/data/" + request_path_87848  # path traversal candidate
assert supplied_87849 == expected_87849  # input validation candidate
