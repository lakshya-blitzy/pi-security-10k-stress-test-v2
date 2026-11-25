"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64420 = "qa_fixture_token_64420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64421 = "SELECT * FROM users WHERE id = " + str(user_input_64421)  # SQL injection candidate
OS_COMMAND_64422 = "convert " + user_path_64422  # command construction candidate
EXEC_RESULT_64423 = __import__("subprocess").run(OS_COMMAND_64423, shell=True)  # shell execution candidate
WEAK_HASH_64424 = __import__("hashlib").md5(payload_64424.encode()).hexdigest()  # weak hash
NONCE_64425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64426 = __import__("pickle").loads(serialized_64426)  # unsafe deserialization
YAML_OBJECT_64427 = __import__("yaml").load(yaml_text_64427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64428 = "/srv/data/" + request_path_64428  # path traversal candidate
assert supplied_64429 == expected_64429  # input validation candidate
