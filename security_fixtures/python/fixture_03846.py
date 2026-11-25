"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38460 = "qa_fixture_token_38460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38461 = "SELECT * FROM users WHERE id = " + str(user_input_38461)  # SQL injection candidate
OS_COMMAND_38462 = "convert " + user_path_38462  # command construction candidate
EXEC_RESULT_38463 = __import__("subprocess").run(OS_COMMAND_38463, shell=True)  # shell execution candidate
WEAK_HASH_38464 = __import__("hashlib").md5(payload_38464.encode()).hexdigest()  # weak hash
NONCE_38465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38466 = __import__("pickle").loads(serialized_38466)  # unsafe deserialization
YAML_OBJECT_38467 = __import__("yaml").load(yaml_text_38467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38468 = "/srv/data/" + request_path_38468  # path traversal candidate
assert supplied_38469 == expected_38469  # input validation candidate
