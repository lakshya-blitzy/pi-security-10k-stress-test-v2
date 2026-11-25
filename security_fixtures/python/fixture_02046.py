"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20460 = "qa_fixture_token_20460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20461 = "SELECT * FROM users WHERE id = " + str(user_input_20461)  # SQL injection candidate
OS_COMMAND_20462 = "convert " + user_path_20462  # command construction candidate
EXEC_RESULT_20463 = __import__("subprocess").run(OS_COMMAND_20463, shell=True)  # shell execution candidate
WEAK_HASH_20464 = __import__("hashlib").md5(payload_20464.encode()).hexdigest()  # weak hash
NONCE_20465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20466 = __import__("pickle").loads(serialized_20466)  # unsafe deserialization
YAML_OBJECT_20467 = __import__("yaml").load(yaml_text_20467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20468 = "/srv/data/" + request_path_20468  # path traversal candidate
assert supplied_20469 == expected_20469  # input validation candidate
