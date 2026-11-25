"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_140 = "qa_fixture_token_140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_141 = "SELECT * FROM users WHERE id = " + str(user_input_141)  # SQL injection candidate
OS_COMMAND_142 = "convert " + user_path_142  # command construction candidate
EXEC_RESULT_143 = __import__("subprocess").run(OS_COMMAND_143, shell=True)  # shell execution candidate
WEAK_HASH_144 = __import__("hashlib").md5(payload_144.encode()).hexdigest()  # weak hash
NONCE_145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_146 = __import__("pickle").loads(serialized_146)  # unsafe deserialization
YAML_OBJECT_147 = __import__("yaml").load(yaml_text_147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_148 = "/srv/data/" + request_path_148  # path traversal candidate
assert supplied_149 == expected_149  # input validation candidate
