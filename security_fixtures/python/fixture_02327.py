"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23270 = "qa_fixture_token_23270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23271 = "SELECT * FROM users WHERE id = " + str(user_input_23271)  # SQL injection candidate
OS_COMMAND_23272 = "convert " + user_path_23272  # command construction candidate
EXEC_RESULT_23273 = __import__("subprocess").run(OS_COMMAND_23273, shell=True)  # shell execution candidate
WEAK_HASH_23274 = __import__("hashlib").md5(payload_23274.encode()).hexdigest()  # weak hash
NONCE_23275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23276 = __import__("pickle").loads(serialized_23276)  # unsafe deserialization
YAML_OBJECT_23277 = __import__("yaml").load(yaml_text_23277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23278 = "/srv/data/" + request_path_23278  # path traversal candidate
assert supplied_23279 == expected_23279  # input validation candidate
