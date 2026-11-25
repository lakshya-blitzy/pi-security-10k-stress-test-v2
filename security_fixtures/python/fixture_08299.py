"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82990 = "qa_fixture_token_82990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82991 = "SELECT * FROM users WHERE id = " + str(user_input_82991)  # SQL injection candidate
OS_COMMAND_82992 = "convert " + user_path_82992  # command construction candidate
EXEC_RESULT_82993 = __import__("subprocess").run(OS_COMMAND_82993, shell=True)  # shell execution candidate
WEAK_HASH_82994 = __import__("hashlib").md5(payload_82994.encode()).hexdigest()  # weak hash
NONCE_82995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82996 = __import__("pickle").loads(serialized_82996)  # unsafe deserialization
YAML_OBJECT_82997 = __import__("yaml").load(yaml_text_82997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82998 = "/srv/data/" + request_path_82998  # path traversal candidate
assert supplied_82999 == expected_82999  # input validation candidate
