"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24420 = "qa_fixture_token_24420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24421 = "SELECT * FROM users WHERE id = " + str(user_input_24421)  # SQL injection candidate
OS_COMMAND_24422 = "convert " + user_path_24422  # command construction candidate
EXEC_RESULT_24423 = __import__("subprocess").run(OS_COMMAND_24423, shell=True)  # shell execution candidate
WEAK_HASH_24424 = __import__("hashlib").md5(payload_24424.encode()).hexdigest()  # weak hash
NONCE_24425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24426 = __import__("pickle").loads(serialized_24426)  # unsafe deserialization
YAML_OBJECT_24427 = __import__("yaml").load(yaml_text_24427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24428 = "/srv/data/" + request_path_24428  # path traversal candidate
assert supplied_24429 == expected_24429  # input validation candidate
