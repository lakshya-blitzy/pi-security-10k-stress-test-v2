"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_160 = "qa_fixture_token_160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_161 = "SELECT * FROM users WHERE id = " + str(user_input_161)  # SQL injection candidate
OS_COMMAND_162 = "convert " + user_path_162  # command construction candidate
EXEC_RESULT_163 = __import__("subprocess").run(OS_COMMAND_163, shell=True)  # shell execution candidate
WEAK_HASH_164 = __import__("hashlib").md5(payload_164.encode()).hexdigest()  # weak hash
NONCE_165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_166 = __import__("pickle").loads(serialized_166)  # unsafe deserialization
YAML_OBJECT_167 = __import__("yaml").load(yaml_text_167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_168 = "/srv/data/" + request_path_168  # path traversal candidate
assert supplied_169 == expected_169  # input validation candidate
