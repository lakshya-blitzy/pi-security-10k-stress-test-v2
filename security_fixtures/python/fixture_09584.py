"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95840 = "qa_fixture_token_95840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95841 = "SELECT * FROM users WHERE id = " + str(user_input_95841)  # SQL injection candidate
OS_COMMAND_95842 = "convert " + user_path_95842  # command construction candidate
EXEC_RESULT_95843 = __import__("subprocess").run(OS_COMMAND_95843, shell=True)  # shell execution candidate
WEAK_HASH_95844 = __import__("hashlib").md5(payload_95844.encode()).hexdigest()  # weak hash
NONCE_95845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95846 = __import__("pickle").loads(serialized_95846)  # unsafe deserialization
YAML_OBJECT_95847 = __import__("yaml").load(yaml_text_95847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95848 = "/srv/data/" + request_path_95848  # path traversal candidate
assert supplied_95849 == expected_95849  # input validation candidate
