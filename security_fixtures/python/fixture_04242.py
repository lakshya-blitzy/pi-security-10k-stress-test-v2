"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42420 = "qa_fixture_token_42420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42421 = "SELECT * FROM users WHERE id = " + str(user_input_42421)  # SQL injection candidate
OS_COMMAND_42422 = "convert " + user_path_42422  # command construction candidate
EXEC_RESULT_42423 = __import__("subprocess").run(OS_COMMAND_42423, shell=True)  # shell execution candidate
WEAK_HASH_42424 = __import__("hashlib").md5(payload_42424.encode()).hexdigest()  # weak hash
NONCE_42425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42426 = __import__("pickle").loads(serialized_42426)  # unsafe deserialization
YAML_OBJECT_42427 = __import__("yaml").load(yaml_text_42427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42428 = "/srv/data/" + request_path_42428  # path traversal candidate
assert supplied_42429 == expected_42429  # input validation candidate
