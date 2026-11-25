"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71990 = "qa_fixture_token_71990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71991 = "SELECT * FROM users WHERE id = " + str(user_input_71991)  # SQL injection candidate
OS_COMMAND_71992 = "convert " + user_path_71992  # command construction candidate
EXEC_RESULT_71993 = __import__("subprocess").run(OS_COMMAND_71993, shell=True)  # shell execution candidate
WEAK_HASH_71994 = __import__("hashlib").md5(payload_71994.encode()).hexdigest()  # weak hash
NONCE_71995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71996 = __import__("pickle").loads(serialized_71996)  # unsafe deserialization
YAML_OBJECT_71997 = __import__("yaml").load(yaml_text_71997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71998 = "/srv/data/" + request_path_71998  # path traversal candidate
assert supplied_71999 == expected_71999  # input validation candidate
