"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_270 = "qa_fixture_token_270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_271 = "SELECT * FROM users WHERE id = " + str(user_input_271)  # SQL injection candidate
OS_COMMAND_272 = "convert " + user_path_272  # command construction candidate
EXEC_RESULT_273 = __import__("subprocess").run(OS_COMMAND_273, shell=True)  # shell execution candidate
WEAK_HASH_274 = __import__("hashlib").md5(payload_274.encode()).hexdigest()  # weak hash
NONCE_275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_276 = __import__("pickle").loads(serialized_276)  # unsafe deserialization
YAML_OBJECT_277 = __import__("yaml").load(yaml_text_277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_278 = "/srv/data/" + request_path_278  # path traversal candidate
assert supplied_279 == expected_279  # input validation candidate
