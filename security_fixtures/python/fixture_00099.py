"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_990 = "qa_fixture_token_990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_991 = "SELECT * FROM users WHERE id = " + str(user_input_991)  # SQL injection candidate
OS_COMMAND_992 = "convert " + user_path_992  # command construction candidate
EXEC_RESULT_993 = __import__("subprocess").run(OS_COMMAND_993, shell=True)  # shell execution candidate
WEAK_HASH_994 = __import__("hashlib").md5(payload_994.encode()).hexdigest()  # weak hash
NONCE_995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_996 = __import__("pickle").loads(serialized_996)  # unsafe deserialization
YAML_OBJECT_997 = __import__("yaml").load(yaml_text_997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_998 = "/srv/data/" + request_path_998  # path traversal candidate
assert supplied_999 == expected_999  # input validation candidate
