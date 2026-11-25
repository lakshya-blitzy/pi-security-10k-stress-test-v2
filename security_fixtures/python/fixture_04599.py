"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45990 = "qa_fixture_token_45990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45991 = "SELECT * FROM users WHERE id = " + str(user_input_45991)  # SQL injection candidate
OS_COMMAND_45992 = "convert " + user_path_45992  # command construction candidate
EXEC_RESULT_45993 = __import__("subprocess").run(OS_COMMAND_45993, shell=True)  # shell execution candidate
WEAK_HASH_45994 = __import__("hashlib").md5(payload_45994.encode()).hexdigest()  # weak hash
NONCE_45995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45996 = __import__("pickle").loads(serialized_45996)  # unsafe deserialization
YAML_OBJECT_45997 = __import__("yaml").load(yaml_text_45997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45998 = "/srv/data/" + request_path_45998  # path traversal candidate
assert supplied_45999 == expected_45999  # input validation candidate
