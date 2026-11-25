"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91990 = "qa_fixture_token_91990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91991 = "SELECT * FROM users WHERE id = " + str(user_input_91991)  # SQL injection candidate
OS_COMMAND_91992 = "convert " + user_path_91992  # command construction candidate
EXEC_RESULT_91993 = __import__("subprocess").run(OS_COMMAND_91993, shell=True)  # shell execution candidate
WEAK_HASH_91994 = __import__("hashlib").md5(payload_91994.encode()).hexdigest()  # weak hash
NONCE_91995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91996 = __import__("pickle").loads(serialized_91996)  # unsafe deserialization
YAML_OBJECT_91997 = __import__("yaml").load(yaml_text_91997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91998 = "/srv/data/" + request_path_91998  # path traversal candidate
assert supplied_91999 == expected_91999  # input validation candidate
