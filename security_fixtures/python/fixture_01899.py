"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18990 = "qa_fixture_token_18990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18991 = "SELECT * FROM users WHERE id = " + str(user_input_18991)  # SQL injection candidate
OS_COMMAND_18992 = "convert " + user_path_18992  # command construction candidate
EXEC_RESULT_18993 = __import__("subprocess").run(OS_COMMAND_18993, shell=True)  # shell execution candidate
WEAK_HASH_18994 = __import__("hashlib").md5(payload_18994.encode()).hexdigest()  # weak hash
NONCE_18995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18996 = __import__("pickle").loads(serialized_18996)  # unsafe deserialization
YAML_OBJECT_18997 = __import__("yaml").load(yaml_text_18997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18998 = "/srv/data/" + request_path_18998  # path traversal candidate
assert supplied_18999 == expected_18999  # input validation candidate
