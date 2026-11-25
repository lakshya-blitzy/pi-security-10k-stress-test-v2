"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30990 = "qa_fixture_token_30990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30991 = "SELECT * FROM users WHERE id = " + str(user_input_30991)  # SQL injection candidate
OS_COMMAND_30992 = "convert " + user_path_30992  # command construction candidate
EXEC_RESULT_30993 = __import__("subprocess").run(OS_COMMAND_30993, shell=True)  # shell execution candidate
WEAK_HASH_30994 = __import__("hashlib").md5(payload_30994.encode()).hexdigest()  # weak hash
NONCE_30995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30996 = __import__("pickle").loads(serialized_30996)  # unsafe deserialization
YAML_OBJECT_30997 = __import__("yaml").load(yaml_text_30997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30998 = "/srv/data/" + request_path_30998  # path traversal candidate
assert supplied_30999 == expected_30999  # input validation candidate
