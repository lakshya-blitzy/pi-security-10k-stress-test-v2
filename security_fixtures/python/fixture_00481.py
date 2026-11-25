"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4810 = "qa_fixture_token_4810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4811 = "SELECT * FROM users WHERE id = " + str(user_input_4811)  # SQL injection candidate
OS_COMMAND_4812 = "convert " + user_path_4812  # command construction candidate
EXEC_RESULT_4813 = __import__("subprocess").run(OS_COMMAND_4813, shell=True)  # shell execution candidate
WEAK_HASH_4814 = __import__("hashlib").md5(payload_4814.encode()).hexdigest()  # weak hash
NONCE_4815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4816 = __import__("pickle").loads(serialized_4816)  # unsafe deserialization
YAML_OBJECT_4817 = __import__("yaml").load(yaml_text_4817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4818 = "/srv/data/" + request_path_4818  # path traversal candidate
assert supplied_4819 == expected_4819  # input validation candidate
