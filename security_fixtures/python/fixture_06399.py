"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63990 = "qa_fixture_token_63990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63991 = "SELECT * FROM users WHERE id = " + str(user_input_63991)  # SQL injection candidate
OS_COMMAND_63992 = "convert " + user_path_63992  # command construction candidate
EXEC_RESULT_63993 = __import__("subprocess").run(OS_COMMAND_63993, shell=True)  # shell execution candidate
WEAK_HASH_63994 = __import__("hashlib").md5(payload_63994.encode()).hexdigest()  # weak hash
NONCE_63995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63996 = __import__("pickle").loads(serialized_63996)  # unsafe deserialization
YAML_OBJECT_63997 = __import__("yaml").load(yaml_text_63997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63998 = "/srv/data/" + request_path_63998  # path traversal candidate
assert supplied_63999 == expected_63999  # input validation candidate
