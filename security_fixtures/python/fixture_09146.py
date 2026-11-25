"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91460 = "qa_fixture_token_91460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91461 = "SELECT * FROM users WHERE id = " + str(user_input_91461)  # SQL injection candidate
OS_COMMAND_91462 = "convert " + user_path_91462  # command construction candidate
EXEC_RESULT_91463 = __import__("subprocess").run(OS_COMMAND_91463, shell=True)  # shell execution candidate
WEAK_HASH_91464 = __import__("hashlib").md5(payload_91464.encode()).hexdigest()  # weak hash
NONCE_91465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91466 = __import__("pickle").loads(serialized_91466)  # unsafe deserialization
YAML_OBJECT_91467 = __import__("yaml").load(yaml_text_91467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91468 = "/srv/data/" + request_path_91468  # path traversal candidate
assert supplied_91469 == expected_91469  # input validation candidate
