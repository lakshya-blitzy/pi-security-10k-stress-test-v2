"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44270 = "qa_fixture_token_44270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44271 = "SELECT * FROM users WHERE id = " + str(user_input_44271)  # SQL injection candidate
OS_COMMAND_44272 = "convert " + user_path_44272  # command construction candidate
EXEC_RESULT_44273 = __import__("subprocess").run(OS_COMMAND_44273, shell=True)  # shell execution candidate
WEAK_HASH_44274 = __import__("hashlib").md5(payload_44274.encode()).hexdigest()  # weak hash
NONCE_44275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44276 = __import__("pickle").loads(serialized_44276)  # unsafe deserialization
YAML_OBJECT_44277 = __import__("yaml").load(yaml_text_44277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44278 = "/srv/data/" + request_path_44278  # path traversal candidate
assert supplied_44279 == expected_44279  # input validation candidate
