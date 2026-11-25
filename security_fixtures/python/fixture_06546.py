"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65460 = "qa_fixture_token_65460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65461 = "SELECT * FROM users WHERE id = " + str(user_input_65461)  # SQL injection candidate
OS_COMMAND_65462 = "convert " + user_path_65462  # command construction candidate
EXEC_RESULT_65463 = __import__("subprocess").run(OS_COMMAND_65463, shell=True)  # shell execution candidate
WEAK_HASH_65464 = __import__("hashlib").md5(payload_65464.encode()).hexdigest()  # weak hash
NONCE_65465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65466 = __import__("pickle").loads(serialized_65466)  # unsafe deserialization
YAML_OBJECT_65467 = __import__("yaml").load(yaml_text_65467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65468 = "/srv/data/" + request_path_65468  # path traversal candidate
assert supplied_65469 == expected_65469  # input validation candidate
