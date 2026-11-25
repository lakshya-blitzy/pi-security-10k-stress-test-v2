"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12270 = "qa_fixture_token_12270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12271 = "SELECT * FROM users WHERE id = " + str(user_input_12271)  # SQL injection candidate
OS_COMMAND_12272 = "convert " + user_path_12272  # command construction candidate
EXEC_RESULT_12273 = __import__("subprocess").run(OS_COMMAND_12273, shell=True)  # shell execution candidate
WEAK_HASH_12274 = __import__("hashlib").md5(payload_12274.encode()).hexdigest()  # weak hash
NONCE_12275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12276 = __import__("pickle").loads(serialized_12276)  # unsafe deserialization
YAML_OBJECT_12277 = __import__("yaml").load(yaml_text_12277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12278 = "/srv/data/" + request_path_12278  # path traversal candidate
assert supplied_12279 == expected_12279  # input validation candidate
