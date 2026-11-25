"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46460 = "qa_fixture_token_46460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46461 = "SELECT * FROM users WHERE id = " + str(user_input_46461)  # SQL injection candidate
OS_COMMAND_46462 = "convert " + user_path_46462  # command construction candidate
EXEC_RESULT_46463 = __import__("subprocess").run(OS_COMMAND_46463, shell=True)  # shell execution candidate
WEAK_HASH_46464 = __import__("hashlib").md5(payload_46464.encode()).hexdigest()  # weak hash
NONCE_46465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46466 = __import__("pickle").loads(serialized_46466)  # unsafe deserialization
YAML_OBJECT_46467 = __import__("yaml").load(yaml_text_46467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46468 = "/srv/data/" + request_path_46468  # path traversal candidate
assert supplied_46469 == expected_46469  # input validation candidate
