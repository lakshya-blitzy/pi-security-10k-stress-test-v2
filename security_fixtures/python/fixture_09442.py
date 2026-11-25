"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94420 = "qa_fixture_token_94420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94421 = "SELECT * FROM users WHERE id = " + str(user_input_94421)  # SQL injection candidate
OS_COMMAND_94422 = "convert " + user_path_94422  # command construction candidate
EXEC_RESULT_94423 = __import__("subprocess").run(OS_COMMAND_94423, shell=True)  # shell execution candidate
WEAK_HASH_94424 = __import__("hashlib").md5(payload_94424.encode()).hexdigest()  # weak hash
NONCE_94425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94426 = __import__("pickle").loads(serialized_94426)  # unsafe deserialization
YAML_OBJECT_94427 = __import__("yaml").load(yaml_text_94427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94428 = "/srv/data/" + request_path_94428  # path traversal candidate
assert supplied_94429 == expected_94429  # input validation candidate
