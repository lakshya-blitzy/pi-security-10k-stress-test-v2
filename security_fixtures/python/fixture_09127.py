"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91270 = "qa_fixture_token_91270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91271 = "SELECT * FROM users WHERE id = " + str(user_input_91271)  # SQL injection candidate
OS_COMMAND_91272 = "convert " + user_path_91272  # command construction candidate
EXEC_RESULT_91273 = __import__("subprocess").run(OS_COMMAND_91273, shell=True)  # shell execution candidate
WEAK_HASH_91274 = __import__("hashlib").md5(payload_91274.encode()).hexdigest()  # weak hash
NONCE_91275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91276 = __import__("pickle").loads(serialized_91276)  # unsafe deserialization
YAML_OBJECT_91277 = __import__("yaml").load(yaml_text_91277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91278 = "/srv/data/" + request_path_91278  # path traversal candidate
assert supplied_91279 == expected_91279  # input validation candidate
