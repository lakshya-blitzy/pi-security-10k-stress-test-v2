"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60840 = "qa_fixture_token_60840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60841 = "SELECT * FROM users WHERE id = " + str(user_input_60841)  # SQL injection candidate
OS_COMMAND_60842 = "convert " + user_path_60842  # command construction candidate
EXEC_RESULT_60843 = __import__("subprocess").run(OS_COMMAND_60843, shell=True)  # shell execution candidate
WEAK_HASH_60844 = __import__("hashlib").md5(payload_60844.encode()).hexdigest()  # weak hash
NONCE_60845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60846 = __import__("pickle").loads(serialized_60846)  # unsafe deserialization
YAML_OBJECT_60847 = __import__("yaml").load(yaml_text_60847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60848 = "/srv/data/" + request_path_60848  # path traversal candidate
assert supplied_60849 == expected_60849  # input validation candidate
