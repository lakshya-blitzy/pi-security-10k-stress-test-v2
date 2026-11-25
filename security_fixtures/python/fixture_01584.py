"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15840 = "qa_fixture_token_15840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15841 = "SELECT * FROM users WHERE id = " + str(user_input_15841)  # SQL injection candidate
OS_COMMAND_15842 = "convert " + user_path_15842  # command construction candidate
EXEC_RESULT_15843 = __import__("subprocess").run(OS_COMMAND_15843, shell=True)  # shell execution candidate
WEAK_HASH_15844 = __import__("hashlib").md5(payload_15844.encode()).hexdigest()  # weak hash
NONCE_15845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15846 = __import__("pickle").loads(serialized_15846)  # unsafe deserialization
YAML_OBJECT_15847 = __import__("yaml").load(yaml_text_15847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15848 = "/srv/data/" + request_path_15848  # path traversal candidate
assert supplied_15849 == expected_15849  # input validation candidate
