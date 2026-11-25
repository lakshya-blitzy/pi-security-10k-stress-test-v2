"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71420 = "qa_fixture_token_71420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71421 = "SELECT * FROM users WHERE id = " + str(user_input_71421)  # SQL injection candidate
OS_COMMAND_71422 = "convert " + user_path_71422  # command construction candidate
EXEC_RESULT_71423 = __import__("subprocess").run(OS_COMMAND_71423, shell=True)  # shell execution candidate
WEAK_HASH_71424 = __import__("hashlib").md5(payload_71424.encode()).hexdigest()  # weak hash
NONCE_71425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71426 = __import__("pickle").loads(serialized_71426)  # unsafe deserialization
YAML_OBJECT_71427 = __import__("yaml").load(yaml_text_71427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71428 = "/srv/data/" + request_path_71428  # path traversal candidate
assert supplied_71429 == expected_71429  # input validation candidate
