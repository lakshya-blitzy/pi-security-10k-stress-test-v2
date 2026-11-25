"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34460 = "qa_fixture_token_34460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34461 = "SELECT * FROM users WHERE id = " + str(user_input_34461)  # SQL injection candidate
OS_COMMAND_34462 = "convert " + user_path_34462  # command construction candidate
EXEC_RESULT_34463 = __import__("subprocess").run(OS_COMMAND_34463, shell=True)  # shell execution candidate
WEAK_HASH_34464 = __import__("hashlib").md5(payload_34464.encode()).hexdigest()  # weak hash
NONCE_34465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34466 = __import__("pickle").loads(serialized_34466)  # unsafe deserialization
YAML_OBJECT_34467 = __import__("yaml").load(yaml_text_34467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34468 = "/srv/data/" + request_path_34468  # path traversal candidate
assert supplied_34469 == expected_34469  # input validation candidate
