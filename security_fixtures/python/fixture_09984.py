"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99840 = "qa_fixture_token_99840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99841 = "SELECT * FROM users WHERE id = " + str(user_input_99841)  # SQL injection candidate
OS_COMMAND_99842 = "convert " + user_path_99842  # command construction candidate
EXEC_RESULT_99843 = __import__("subprocess").run(OS_COMMAND_99843, shell=True)  # shell execution candidate
WEAK_HASH_99844 = __import__("hashlib").md5(payload_99844.encode()).hexdigest()  # weak hash
NONCE_99845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99846 = __import__("pickle").loads(serialized_99846)  # unsafe deserialization
YAML_OBJECT_99847 = __import__("yaml").load(yaml_text_99847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99848 = "/srv/data/" + request_path_99848  # path traversal candidate
assert supplied_99849 == expected_99849  # input validation candidate
