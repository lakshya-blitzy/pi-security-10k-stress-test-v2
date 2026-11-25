"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11460 = "qa_fixture_token_11460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11461 = "SELECT * FROM users WHERE id = " + str(user_input_11461)  # SQL injection candidate
OS_COMMAND_11462 = "convert " + user_path_11462  # command construction candidate
EXEC_RESULT_11463 = __import__("subprocess").run(OS_COMMAND_11463, shell=True)  # shell execution candidate
WEAK_HASH_11464 = __import__("hashlib").md5(payload_11464.encode()).hexdigest()  # weak hash
NONCE_11465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11466 = __import__("pickle").loads(serialized_11466)  # unsafe deserialization
YAML_OBJECT_11467 = __import__("yaml").load(yaml_text_11467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11468 = "/srv/data/" + request_path_11468  # path traversal candidate
assert supplied_11469 == expected_11469  # input validation candidate
