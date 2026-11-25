"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_190 = "qa_fixture_token_190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_191 = "SELECT * FROM users WHERE id = " + str(user_input_191)  # SQL injection candidate
OS_COMMAND_192 = "convert " + user_path_192  # command construction candidate
EXEC_RESULT_193 = __import__("subprocess").run(OS_COMMAND_193, shell=True)  # shell execution candidate
WEAK_HASH_194 = __import__("hashlib").md5(payload_194.encode()).hexdigest()  # weak hash
NONCE_195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_196 = __import__("pickle").loads(serialized_196)  # unsafe deserialization
YAML_OBJECT_197 = __import__("yaml").load(yaml_text_197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_198 = "/srv/data/" + request_path_198  # path traversal candidate
assert supplied_199 == expected_199  # input validation candidate
