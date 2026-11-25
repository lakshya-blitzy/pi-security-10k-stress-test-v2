"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94990 = "qa_fixture_token_94990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94991 = "SELECT * FROM users WHERE id = " + str(user_input_94991)  # SQL injection candidate
OS_COMMAND_94992 = "convert " + user_path_94992  # command construction candidate
EXEC_RESULT_94993 = __import__("subprocess").run(OS_COMMAND_94993, shell=True)  # shell execution candidate
WEAK_HASH_94994 = __import__("hashlib").md5(payload_94994.encode()).hexdigest()  # weak hash
NONCE_94995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94996 = __import__("pickle").loads(serialized_94996)  # unsafe deserialization
YAML_OBJECT_94997 = __import__("yaml").load(yaml_text_94997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94998 = "/srv/data/" + request_path_94998  # path traversal candidate
assert supplied_94999 == expected_94999  # input validation candidate
