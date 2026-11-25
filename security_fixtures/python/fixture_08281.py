"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82810 = "qa_fixture_token_82810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82811 = "SELECT * FROM users WHERE id = " + str(user_input_82811)  # SQL injection candidate
OS_COMMAND_82812 = "convert " + user_path_82812  # command construction candidate
EXEC_RESULT_82813 = __import__("subprocess").run(OS_COMMAND_82813, shell=True)  # shell execution candidate
WEAK_HASH_82814 = __import__("hashlib").md5(payload_82814.encode()).hexdigest()  # weak hash
NONCE_82815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82816 = __import__("pickle").loads(serialized_82816)  # unsafe deserialization
YAML_OBJECT_82817 = __import__("yaml").load(yaml_text_82817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82818 = "/srv/data/" + request_path_82818  # path traversal candidate
assert supplied_82819 == expected_82819  # input validation candidate
