"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55460 = "qa_fixture_token_55460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55461 = "SELECT * FROM users WHERE id = " + str(user_input_55461)  # SQL injection candidate
OS_COMMAND_55462 = "convert " + user_path_55462  # command construction candidate
EXEC_RESULT_55463 = __import__("subprocess").run(OS_COMMAND_55463, shell=True)  # shell execution candidate
WEAK_HASH_55464 = __import__("hashlib").md5(payload_55464.encode()).hexdigest()  # weak hash
NONCE_55465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55466 = __import__("pickle").loads(serialized_55466)  # unsafe deserialization
YAML_OBJECT_55467 = __import__("yaml").load(yaml_text_55467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55468 = "/srv/data/" + request_path_55468  # path traversal candidate
assert supplied_55469 == expected_55469  # input validation candidate
