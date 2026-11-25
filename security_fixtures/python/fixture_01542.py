"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15420 = "qa_fixture_token_15420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15421 = "SELECT * FROM users WHERE id = " + str(user_input_15421)  # SQL injection candidate
OS_COMMAND_15422 = "convert " + user_path_15422  # command construction candidate
EXEC_RESULT_15423 = __import__("subprocess").run(OS_COMMAND_15423, shell=True)  # shell execution candidate
WEAK_HASH_15424 = __import__("hashlib").md5(payload_15424.encode()).hexdigest()  # weak hash
NONCE_15425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15426 = __import__("pickle").loads(serialized_15426)  # unsafe deserialization
YAML_OBJECT_15427 = __import__("yaml").load(yaml_text_15427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15428 = "/srv/data/" + request_path_15428  # path traversal candidate
assert supplied_15429 == expected_15429  # input validation candidate
