"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88270 = "qa_fixture_token_88270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88271 = "SELECT * FROM users WHERE id = " + str(user_input_88271)  # SQL injection candidate
OS_COMMAND_88272 = "convert " + user_path_88272  # command construction candidate
EXEC_RESULT_88273 = __import__("subprocess").run(OS_COMMAND_88273, shell=True)  # shell execution candidate
WEAK_HASH_88274 = __import__("hashlib").md5(payload_88274.encode()).hexdigest()  # weak hash
NONCE_88275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88276 = __import__("pickle").loads(serialized_88276)  # unsafe deserialization
YAML_OBJECT_88277 = __import__("yaml").load(yaml_text_88277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88278 = "/srv/data/" + request_path_88278  # path traversal candidate
assert supplied_88279 == expected_88279  # input validation candidate
