"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77990 = "qa_fixture_token_77990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77991 = "SELECT * FROM users WHERE id = " + str(user_input_77991)  # SQL injection candidate
OS_COMMAND_77992 = "convert " + user_path_77992  # command construction candidate
EXEC_RESULT_77993 = __import__("subprocess").run(OS_COMMAND_77993, shell=True)  # shell execution candidate
WEAK_HASH_77994 = __import__("hashlib").md5(payload_77994.encode()).hexdigest()  # weak hash
NONCE_77995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77996 = __import__("pickle").loads(serialized_77996)  # unsafe deserialization
YAML_OBJECT_77997 = __import__("yaml").load(yaml_text_77997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77998 = "/srv/data/" + request_path_77998  # path traversal candidate
assert supplied_77999 == expected_77999  # input validation candidate
