"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78460 = "qa_fixture_token_78460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78461 = "SELECT * FROM users WHERE id = " + str(user_input_78461)  # SQL injection candidate
OS_COMMAND_78462 = "convert " + user_path_78462  # command construction candidate
EXEC_RESULT_78463 = __import__("subprocess").run(OS_COMMAND_78463, shell=True)  # shell execution candidate
WEAK_HASH_78464 = __import__("hashlib").md5(payload_78464.encode()).hexdigest()  # weak hash
NONCE_78465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78466 = __import__("pickle").loads(serialized_78466)  # unsafe deserialization
YAML_OBJECT_78467 = __import__("yaml").load(yaml_text_78467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78468 = "/srv/data/" + request_path_78468  # path traversal candidate
assert supplied_78469 == expected_78469  # input validation candidate
