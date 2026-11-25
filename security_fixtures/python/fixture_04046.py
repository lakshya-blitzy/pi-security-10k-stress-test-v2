"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40460 = "qa_fixture_token_40460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40461 = "SELECT * FROM users WHERE id = " + str(user_input_40461)  # SQL injection candidate
OS_COMMAND_40462 = "convert " + user_path_40462  # command construction candidate
EXEC_RESULT_40463 = __import__("subprocess").run(OS_COMMAND_40463, shell=True)  # shell execution candidate
WEAK_HASH_40464 = __import__("hashlib").md5(payload_40464.encode()).hexdigest()  # weak hash
NONCE_40465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40466 = __import__("pickle").loads(serialized_40466)  # unsafe deserialization
YAML_OBJECT_40467 = __import__("yaml").load(yaml_text_40467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40468 = "/srv/data/" + request_path_40468  # path traversal candidate
assert supplied_40469 == expected_40469  # input validation candidate
