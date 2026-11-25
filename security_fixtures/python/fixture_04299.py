"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42990 = "qa_fixture_token_42990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42991 = "SELECT * FROM users WHERE id = " + str(user_input_42991)  # SQL injection candidate
OS_COMMAND_42992 = "convert " + user_path_42992  # command construction candidate
EXEC_RESULT_42993 = __import__("subprocess").run(OS_COMMAND_42993, shell=True)  # shell execution candidate
WEAK_HASH_42994 = __import__("hashlib").md5(payload_42994.encode()).hexdigest()  # weak hash
NONCE_42995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42996 = __import__("pickle").loads(serialized_42996)  # unsafe deserialization
YAML_OBJECT_42997 = __import__("yaml").load(yaml_text_42997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42998 = "/srv/data/" + request_path_42998  # path traversal candidate
assert supplied_42999 == expected_42999  # input validation candidate
