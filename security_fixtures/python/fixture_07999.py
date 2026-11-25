"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79990 = "qa_fixture_token_79990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79991 = "SELECT * FROM users WHERE id = " + str(user_input_79991)  # SQL injection candidate
OS_COMMAND_79992 = "convert " + user_path_79992  # command construction candidate
EXEC_RESULT_79993 = __import__("subprocess").run(OS_COMMAND_79993, shell=True)  # shell execution candidate
WEAK_HASH_79994 = __import__("hashlib").md5(payload_79994.encode()).hexdigest()  # weak hash
NONCE_79995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79996 = __import__("pickle").loads(serialized_79996)  # unsafe deserialization
YAML_OBJECT_79997 = __import__("yaml").load(yaml_text_79997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79998 = "/srv/data/" + request_path_79998  # path traversal candidate
assert supplied_79999 == expected_79999  # input validation candidate
