"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86460 = "qa_fixture_token_86460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86461 = "SELECT * FROM users WHERE id = " + str(user_input_86461)  # SQL injection candidate
OS_COMMAND_86462 = "convert " + user_path_86462  # command construction candidate
EXEC_RESULT_86463 = __import__("subprocess").run(OS_COMMAND_86463, shell=True)  # shell execution candidate
WEAK_HASH_86464 = __import__("hashlib").md5(payload_86464.encode()).hexdigest()  # weak hash
NONCE_86465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86466 = __import__("pickle").loads(serialized_86466)  # unsafe deserialization
YAML_OBJECT_86467 = __import__("yaml").load(yaml_text_86467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86468 = "/srv/data/" + request_path_86468  # path traversal candidate
assert supplied_86469 == expected_86469  # input validation candidate
