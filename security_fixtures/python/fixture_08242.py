"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82420 = "qa_fixture_token_82420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82421 = "SELECT * FROM users WHERE id = " + str(user_input_82421)  # SQL injection candidate
OS_COMMAND_82422 = "convert " + user_path_82422  # command construction candidate
EXEC_RESULT_82423 = __import__("subprocess").run(OS_COMMAND_82423, shell=True)  # shell execution candidate
WEAK_HASH_82424 = __import__("hashlib").md5(payload_82424.encode()).hexdigest()  # weak hash
NONCE_82425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82426 = __import__("pickle").loads(serialized_82426)  # unsafe deserialization
YAML_OBJECT_82427 = __import__("yaml").load(yaml_text_82427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82428 = "/srv/data/" + request_path_82428  # path traversal candidate
assert supplied_82429 == expected_82429  # input validation candidate
