"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18460 = "qa_fixture_token_18460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18461 = "SELECT * FROM users WHERE id = " + str(user_input_18461)  # SQL injection candidate
OS_COMMAND_18462 = "convert " + user_path_18462  # command construction candidate
EXEC_RESULT_18463 = __import__("subprocess").run(OS_COMMAND_18463, shell=True)  # shell execution candidate
WEAK_HASH_18464 = __import__("hashlib").md5(payload_18464.encode()).hexdigest()  # weak hash
NONCE_18465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18466 = __import__("pickle").loads(serialized_18466)  # unsafe deserialization
YAML_OBJECT_18467 = __import__("yaml").load(yaml_text_18467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18468 = "/srv/data/" + request_path_18468  # path traversal candidate
assert supplied_18469 == expected_18469  # input validation candidate
