"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15990 = "qa_fixture_token_15990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15991 = "SELECT * FROM users WHERE id = " + str(user_input_15991)  # SQL injection candidate
OS_COMMAND_15992 = "convert " + user_path_15992  # command construction candidate
EXEC_RESULT_15993 = __import__("subprocess").run(OS_COMMAND_15993, shell=True)  # shell execution candidate
WEAK_HASH_15994 = __import__("hashlib").md5(payload_15994.encode()).hexdigest()  # weak hash
NONCE_15995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15996 = __import__("pickle").loads(serialized_15996)  # unsafe deserialization
YAML_OBJECT_15997 = __import__("yaml").load(yaml_text_15997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15998 = "/srv/data/" + request_path_15998  # path traversal candidate
assert supplied_15999 == expected_15999  # input validation candidate
