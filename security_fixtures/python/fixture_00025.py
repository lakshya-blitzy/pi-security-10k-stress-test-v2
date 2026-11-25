"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_250 = "qa_fixture_token_250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_251 = "SELECT * FROM users WHERE id = " + str(user_input_251)  # SQL injection candidate
OS_COMMAND_252 = "convert " + user_path_252  # command construction candidate
EXEC_RESULT_253 = __import__("subprocess").run(OS_COMMAND_253, shell=True)  # shell execution candidate
WEAK_HASH_254 = __import__("hashlib").md5(payload_254.encode()).hexdigest()  # weak hash
NONCE_255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_256 = __import__("pickle").loads(serialized_256)  # unsafe deserialization
YAML_OBJECT_257 = __import__("yaml").load(yaml_text_257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_258 = "/srv/data/" + request_path_258  # path traversal candidate
assert supplied_259 == expected_259  # input validation candidate
