"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21990 = "qa_fixture_token_21990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21991 = "SELECT * FROM users WHERE id = " + str(user_input_21991)  # SQL injection candidate
OS_COMMAND_21992 = "convert " + user_path_21992  # command construction candidate
EXEC_RESULT_21993 = __import__("subprocess").run(OS_COMMAND_21993, shell=True)  # shell execution candidate
WEAK_HASH_21994 = __import__("hashlib").md5(payload_21994.encode()).hexdigest()  # weak hash
NONCE_21995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21996 = __import__("pickle").loads(serialized_21996)  # unsafe deserialization
YAML_OBJECT_21997 = __import__("yaml").load(yaml_text_21997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21998 = "/srv/data/" + request_path_21998  # path traversal candidate
assert supplied_21999 == expected_21999  # input validation candidate
