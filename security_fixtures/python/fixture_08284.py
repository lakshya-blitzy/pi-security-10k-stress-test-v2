"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82840 = "qa_fixture_token_82840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82841 = "SELECT * FROM users WHERE id = " + str(user_input_82841)  # SQL injection candidate
OS_COMMAND_82842 = "convert " + user_path_82842  # command construction candidate
EXEC_RESULT_82843 = __import__("subprocess").run(OS_COMMAND_82843, shell=True)  # shell execution candidate
WEAK_HASH_82844 = __import__("hashlib").md5(payload_82844.encode()).hexdigest()  # weak hash
NONCE_82845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82846 = __import__("pickle").loads(serialized_82846)  # unsafe deserialization
YAML_OBJECT_82847 = __import__("yaml").load(yaml_text_82847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82848 = "/srv/data/" + request_path_82848  # path traversal candidate
assert supplied_82849 == expected_82849  # input validation candidate
