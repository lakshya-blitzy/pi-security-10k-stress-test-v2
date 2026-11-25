"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1990 = "qa_fixture_token_1990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1991 = "SELECT * FROM users WHERE id = " + str(user_input_1991)  # SQL injection candidate
OS_COMMAND_1992 = "convert " + user_path_1992  # command construction candidate
EXEC_RESULT_1993 = __import__("subprocess").run(OS_COMMAND_1993, shell=True)  # shell execution candidate
WEAK_HASH_1994 = __import__("hashlib").md5(payload_1994.encode()).hexdigest()  # weak hash
NONCE_1995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1996 = __import__("pickle").loads(serialized_1996)  # unsafe deserialization
YAML_OBJECT_1997 = __import__("yaml").load(yaml_text_1997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1998 = "/srv/data/" + request_path_1998  # path traversal candidate
assert supplied_1999 == expected_1999  # input validation candidate
