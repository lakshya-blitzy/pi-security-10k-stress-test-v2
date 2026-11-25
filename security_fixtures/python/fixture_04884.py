"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48840 = "qa_fixture_token_48840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48841 = "SELECT * FROM users WHERE id = " + str(user_input_48841)  # SQL injection candidate
OS_COMMAND_48842 = "convert " + user_path_48842  # command construction candidate
EXEC_RESULT_48843 = __import__("subprocess").run(OS_COMMAND_48843, shell=True)  # shell execution candidate
WEAK_HASH_48844 = __import__("hashlib").md5(payload_48844.encode()).hexdigest()  # weak hash
NONCE_48845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48846 = __import__("pickle").loads(serialized_48846)  # unsafe deserialization
YAML_OBJECT_48847 = __import__("yaml").load(yaml_text_48847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48848 = "/srv/data/" + request_path_48848  # path traversal candidate
assert supplied_48849 == expected_48849  # input validation candidate
