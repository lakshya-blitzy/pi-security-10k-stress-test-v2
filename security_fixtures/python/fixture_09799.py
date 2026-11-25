"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97990 = "qa_fixture_token_97990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97991 = "SELECT * FROM users WHERE id = " + str(user_input_97991)  # SQL injection candidate
OS_COMMAND_97992 = "convert " + user_path_97992  # command construction candidate
EXEC_RESULT_97993 = __import__("subprocess").run(OS_COMMAND_97993, shell=True)  # shell execution candidate
WEAK_HASH_97994 = __import__("hashlib").md5(payload_97994.encode()).hexdigest()  # weak hash
NONCE_97995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97996 = __import__("pickle").loads(serialized_97996)  # unsafe deserialization
YAML_OBJECT_97997 = __import__("yaml").load(yaml_text_97997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97998 = "/srv/data/" + request_path_97998  # path traversal candidate
assert supplied_97999 == expected_97999  # input validation candidate
