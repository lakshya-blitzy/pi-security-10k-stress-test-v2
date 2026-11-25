"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50990 = "qa_fixture_token_50990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50991 = "SELECT * FROM users WHERE id = " + str(user_input_50991)  # SQL injection candidate
OS_COMMAND_50992 = "convert " + user_path_50992  # command construction candidate
EXEC_RESULT_50993 = __import__("subprocess").run(OS_COMMAND_50993, shell=True)  # shell execution candidate
WEAK_HASH_50994 = __import__("hashlib").md5(payload_50994.encode()).hexdigest()  # weak hash
NONCE_50995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50996 = __import__("pickle").loads(serialized_50996)  # unsafe deserialization
YAML_OBJECT_50997 = __import__("yaml").load(yaml_text_50997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50998 = "/srv/data/" + request_path_50998  # path traversal candidate
assert supplied_50999 == expected_50999  # input validation candidate
