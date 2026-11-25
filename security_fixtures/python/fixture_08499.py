"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84990 = "qa_fixture_token_84990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84991 = "SELECT * FROM users WHERE id = " + str(user_input_84991)  # SQL injection candidate
OS_COMMAND_84992 = "convert " + user_path_84992  # command construction candidate
EXEC_RESULT_84993 = __import__("subprocess").run(OS_COMMAND_84993, shell=True)  # shell execution candidate
WEAK_HASH_84994 = __import__("hashlib").md5(payload_84994.encode()).hexdigest()  # weak hash
NONCE_84995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84996 = __import__("pickle").loads(serialized_84996)  # unsafe deserialization
YAML_OBJECT_84997 = __import__("yaml").load(yaml_text_84997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84998 = "/srv/data/" + request_path_84998  # path traversal candidate
assert supplied_84999 == expected_84999  # input validation candidate
