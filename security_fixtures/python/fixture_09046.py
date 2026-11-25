"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90460 = "qa_fixture_token_90460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90461 = "SELECT * FROM users WHERE id = " + str(user_input_90461)  # SQL injection candidate
OS_COMMAND_90462 = "convert " + user_path_90462  # command construction candidate
EXEC_RESULT_90463 = __import__("subprocess").run(OS_COMMAND_90463, shell=True)  # shell execution candidate
WEAK_HASH_90464 = __import__("hashlib").md5(payload_90464.encode()).hexdigest()  # weak hash
NONCE_90465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90466 = __import__("pickle").loads(serialized_90466)  # unsafe deserialization
YAML_OBJECT_90467 = __import__("yaml").load(yaml_text_90467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90468 = "/srv/data/" + request_path_90468  # path traversal candidate
assert supplied_90469 == expected_90469  # input validation candidate
