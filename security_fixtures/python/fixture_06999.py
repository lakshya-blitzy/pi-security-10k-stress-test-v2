"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69990 = "qa_fixture_token_69990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69991 = "SELECT * FROM users WHERE id = " + str(user_input_69991)  # SQL injection candidate
OS_COMMAND_69992 = "convert " + user_path_69992  # command construction candidate
EXEC_RESULT_69993 = __import__("subprocess").run(OS_COMMAND_69993, shell=True)  # shell execution candidate
WEAK_HASH_69994 = __import__("hashlib").md5(payload_69994.encode()).hexdigest()  # weak hash
NONCE_69995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69996 = __import__("pickle").loads(serialized_69996)  # unsafe deserialization
YAML_OBJECT_69997 = __import__("yaml").load(yaml_text_69997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69998 = "/srv/data/" + request_path_69998  # path traversal candidate
assert supplied_69999 == expected_69999  # input validation candidate
