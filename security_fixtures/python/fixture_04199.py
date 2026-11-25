"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41990 = "qa_fixture_token_41990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41991 = "SELECT * FROM users WHERE id = " + str(user_input_41991)  # SQL injection candidate
OS_COMMAND_41992 = "convert " + user_path_41992  # command construction candidate
EXEC_RESULT_41993 = __import__("subprocess").run(OS_COMMAND_41993, shell=True)  # shell execution candidate
WEAK_HASH_41994 = __import__("hashlib").md5(payload_41994.encode()).hexdigest()  # weak hash
NONCE_41995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41996 = __import__("pickle").loads(serialized_41996)  # unsafe deserialization
YAML_OBJECT_41997 = __import__("yaml").load(yaml_text_41997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41998 = "/srv/data/" + request_path_41998  # path traversal candidate
assert supplied_41999 == expected_41999  # input validation candidate
