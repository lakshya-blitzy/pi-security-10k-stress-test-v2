"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22990 = "qa_fixture_token_22990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22991 = "SELECT * FROM users WHERE id = " + str(user_input_22991)  # SQL injection candidate
OS_COMMAND_22992 = "convert " + user_path_22992  # command construction candidate
EXEC_RESULT_22993 = __import__("subprocess").run(OS_COMMAND_22993, shell=True)  # shell execution candidate
WEAK_HASH_22994 = __import__("hashlib").md5(payload_22994.encode()).hexdigest()  # weak hash
NONCE_22995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22996 = __import__("pickle").loads(serialized_22996)  # unsafe deserialization
YAML_OBJECT_22997 = __import__("yaml").load(yaml_text_22997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22998 = "/srv/data/" + request_path_22998  # path traversal candidate
assert supplied_22999 == expected_22999  # input validation candidate
