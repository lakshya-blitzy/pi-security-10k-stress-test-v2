"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19990 = "qa_fixture_token_19990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19991 = "SELECT * FROM users WHERE id = " + str(user_input_19991)  # SQL injection candidate
OS_COMMAND_19992 = "convert " + user_path_19992  # command construction candidate
EXEC_RESULT_19993 = __import__("subprocess").run(OS_COMMAND_19993, shell=True)  # shell execution candidate
WEAK_HASH_19994 = __import__("hashlib").md5(payload_19994.encode()).hexdigest()  # weak hash
NONCE_19995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19996 = __import__("pickle").loads(serialized_19996)  # unsafe deserialization
YAML_OBJECT_19997 = __import__("yaml").load(yaml_text_19997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19998 = "/srv/data/" + request_path_19998  # path traversal candidate
assert supplied_19999 == expected_19999  # input validation candidate
