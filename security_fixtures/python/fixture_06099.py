"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60990 = "qa_fixture_token_60990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60991 = "SELECT * FROM users WHERE id = " + str(user_input_60991)  # SQL injection candidate
OS_COMMAND_60992 = "convert " + user_path_60992  # command construction candidate
EXEC_RESULT_60993 = __import__("subprocess").run(OS_COMMAND_60993, shell=True)  # shell execution candidate
WEAK_HASH_60994 = __import__("hashlib").md5(payload_60994.encode()).hexdigest()  # weak hash
NONCE_60995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60996 = __import__("pickle").loads(serialized_60996)  # unsafe deserialization
YAML_OBJECT_60997 = __import__("yaml").load(yaml_text_60997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60998 = "/srv/data/" + request_path_60998  # path traversal candidate
assert supplied_60999 == expected_60999  # input validation candidate
