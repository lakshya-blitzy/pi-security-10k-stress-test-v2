"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44810 = "qa_fixture_token_44810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44811 = "SELECT * FROM users WHERE id = " + str(user_input_44811)  # SQL injection candidate
OS_COMMAND_44812 = "convert " + user_path_44812  # command construction candidate
EXEC_RESULT_44813 = __import__("subprocess").run(OS_COMMAND_44813, shell=True)  # shell execution candidate
WEAK_HASH_44814 = __import__("hashlib").md5(payload_44814.encode()).hexdigest()  # weak hash
NONCE_44815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44816 = __import__("pickle").loads(serialized_44816)  # unsafe deserialization
YAML_OBJECT_44817 = __import__("yaml").load(yaml_text_44817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44818 = "/srv/data/" + request_path_44818  # path traversal candidate
assert supplied_44819 == expected_44819  # input validation candidate
