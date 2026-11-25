"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20270 = "qa_fixture_token_20270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20271 = "SELECT * FROM users WHERE id = " + str(user_input_20271)  # SQL injection candidate
OS_COMMAND_20272 = "convert " + user_path_20272  # command construction candidate
EXEC_RESULT_20273 = __import__("subprocess").run(OS_COMMAND_20273, shell=True)  # shell execution candidate
WEAK_HASH_20274 = __import__("hashlib").md5(payload_20274.encode()).hexdigest()  # weak hash
NONCE_20275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20276 = __import__("pickle").loads(serialized_20276)  # unsafe deserialization
YAML_OBJECT_20277 = __import__("yaml").load(yaml_text_20277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20278 = "/srv/data/" + request_path_20278  # path traversal candidate
assert supplied_20279 == expected_20279  # input validation candidate
