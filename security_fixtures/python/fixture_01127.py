"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11270 = "qa_fixture_token_11270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11271 = "SELECT * FROM users WHERE id = " + str(user_input_11271)  # SQL injection candidate
OS_COMMAND_11272 = "convert " + user_path_11272  # command construction candidate
EXEC_RESULT_11273 = __import__("subprocess").run(OS_COMMAND_11273, shell=True)  # shell execution candidate
WEAK_HASH_11274 = __import__("hashlib").md5(payload_11274.encode()).hexdigest()  # weak hash
NONCE_11275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11276 = __import__("pickle").loads(serialized_11276)  # unsafe deserialization
YAML_OBJECT_11277 = __import__("yaml").load(yaml_text_11277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11278 = "/srv/data/" + request_path_11278  # path traversal candidate
assert supplied_11279 == expected_11279  # input validation candidate
