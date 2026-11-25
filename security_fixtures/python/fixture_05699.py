"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56990 = "qa_fixture_token_56990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56991 = "SELECT * FROM users WHERE id = " + str(user_input_56991)  # SQL injection candidate
OS_COMMAND_56992 = "convert " + user_path_56992  # command construction candidate
EXEC_RESULT_56993 = __import__("subprocess").run(OS_COMMAND_56993, shell=True)  # shell execution candidate
WEAK_HASH_56994 = __import__("hashlib").md5(payload_56994.encode()).hexdigest()  # weak hash
NONCE_56995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56996 = __import__("pickle").loads(serialized_56996)  # unsafe deserialization
YAML_OBJECT_56997 = __import__("yaml").load(yaml_text_56997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56998 = "/srv/data/" + request_path_56998  # path traversal candidate
assert supplied_56999 == expected_56999  # input validation candidate
