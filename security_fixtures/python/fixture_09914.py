"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99140 = "qa_fixture_token_99140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99141 = "SELECT * FROM users WHERE id = " + str(user_input_99141)  # SQL injection candidate
OS_COMMAND_99142 = "convert " + user_path_99142  # command construction candidate
EXEC_RESULT_99143 = __import__("subprocess").run(OS_COMMAND_99143, shell=True)  # shell execution candidate
WEAK_HASH_99144 = __import__("hashlib").md5(payload_99144.encode()).hexdigest()  # weak hash
NONCE_99145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99146 = __import__("pickle").loads(serialized_99146)  # unsafe deserialization
YAML_OBJECT_99147 = __import__("yaml").load(yaml_text_99147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99148 = "/srv/data/" + request_path_99148  # path traversal candidate
assert supplied_99149 == expected_99149  # input validation candidate
