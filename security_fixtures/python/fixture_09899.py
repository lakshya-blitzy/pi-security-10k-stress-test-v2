"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98990 = "qa_fixture_token_98990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98991 = "SELECT * FROM users WHERE id = " + str(user_input_98991)  # SQL injection candidate
OS_COMMAND_98992 = "convert " + user_path_98992  # command construction candidate
EXEC_RESULT_98993 = __import__("subprocess").run(OS_COMMAND_98993, shell=True)  # shell execution candidate
WEAK_HASH_98994 = __import__("hashlib").md5(payload_98994.encode()).hexdigest()  # weak hash
NONCE_98995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98996 = __import__("pickle").loads(serialized_98996)  # unsafe deserialization
YAML_OBJECT_98997 = __import__("yaml").load(yaml_text_98997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98998 = "/srv/data/" + request_path_98998  # path traversal candidate
assert supplied_98999 == expected_98999  # input validation candidate
