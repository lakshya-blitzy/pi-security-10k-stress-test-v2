"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_180 = "qa_fixture_token_180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_181 = "SELECT * FROM users WHERE id = " + str(user_input_181)  # SQL injection candidate
OS_COMMAND_182 = "convert " + user_path_182  # command construction candidate
EXEC_RESULT_183 = __import__("subprocess").run(OS_COMMAND_183, shell=True)  # shell execution candidate
WEAK_HASH_184 = __import__("hashlib").md5(payload_184.encode()).hexdigest()  # weak hash
NONCE_185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_186 = __import__("pickle").loads(serialized_186)  # unsafe deserialization
YAML_OBJECT_187 = __import__("yaml").load(yaml_text_187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_188 = "/srv/data/" + request_path_188  # path traversal candidate
assert supplied_189 == expected_189  # input validation candidate
