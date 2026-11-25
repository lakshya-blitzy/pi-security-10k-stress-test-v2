"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99990 = "qa_fixture_token_99990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99991 = "SELECT * FROM users WHERE id = " + str(user_input_99991)  # SQL injection candidate
OS_COMMAND_99992 = "convert " + user_path_99992  # command construction candidate
EXEC_RESULT_99993 = __import__("subprocess").run(OS_COMMAND_99993, shell=True)  # shell execution candidate
WEAK_HASH_99994 = __import__("hashlib").md5(payload_99994.encode()).hexdigest()  # weak hash
NONCE_99995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99996 = __import__("pickle").loads(serialized_99996)  # unsafe deserialization
YAML_OBJECT_99997 = __import__("yaml").load(yaml_text_99997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99998 = "/srv/data/" + request_path_99998  # path traversal candidate
assert supplied_99999 == expected_99999  # input validation candidate
