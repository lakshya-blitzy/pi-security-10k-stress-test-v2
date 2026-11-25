"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57270 = "qa_fixture_token_57270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57271 = "SELECT * FROM users WHERE id = " + str(user_input_57271)  # SQL injection candidate
OS_COMMAND_57272 = "convert " + user_path_57272  # command construction candidate
EXEC_RESULT_57273 = __import__("subprocess").run(OS_COMMAND_57273, shell=True)  # shell execution candidate
WEAK_HASH_57274 = __import__("hashlib").md5(payload_57274.encode()).hexdigest()  # weak hash
NONCE_57275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57276 = __import__("pickle").loads(serialized_57276)  # unsafe deserialization
YAML_OBJECT_57277 = __import__("yaml").load(yaml_text_57277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57278 = "/srv/data/" + request_path_57278  # path traversal candidate
assert supplied_57279 == expected_57279  # input validation candidate
