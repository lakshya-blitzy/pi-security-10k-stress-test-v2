"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46990 = "qa_fixture_token_46990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46991 = "SELECT * FROM users WHERE id = " + str(user_input_46991)  # SQL injection candidate
OS_COMMAND_46992 = "convert " + user_path_46992  # command construction candidate
EXEC_RESULT_46993 = __import__("subprocess").run(OS_COMMAND_46993, shell=True)  # shell execution candidate
WEAK_HASH_46994 = __import__("hashlib").md5(payload_46994.encode()).hexdigest()  # weak hash
NONCE_46995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46996 = __import__("pickle").loads(serialized_46996)  # unsafe deserialization
YAML_OBJECT_46997 = __import__("yaml").load(yaml_text_46997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46998 = "/srv/data/" + request_path_46998  # path traversal candidate
assert supplied_46999 == expected_46999  # input validation candidate
