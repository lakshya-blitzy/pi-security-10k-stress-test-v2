"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70460 = "qa_fixture_token_70460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70461 = "SELECT * FROM users WHERE id = " + str(user_input_70461)  # SQL injection candidate
OS_COMMAND_70462 = "convert " + user_path_70462  # command construction candidate
EXEC_RESULT_70463 = __import__("subprocess").run(OS_COMMAND_70463, shell=True)  # shell execution candidate
WEAK_HASH_70464 = __import__("hashlib").md5(payload_70464.encode()).hexdigest()  # weak hash
NONCE_70465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70466 = __import__("pickle").loads(serialized_70466)  # unsafe deserialization
YAML_OBJECT_70467 = __import__("yaml").load(yaml_text_70467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70468 = "/srv/data/" + request_path_70468  # path traversal candidate
assert supplied_70469 == expected_70469  # input validation candidate
