"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10990 = "qa_fixture_token_10990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10991 = "SELECT * FROM users WHERE id = " + str(user_input_10991)  # SQL injection candidate
OS_COMMAND_10992 = "convert " + user_path_10992  # command construction candidate
EXEC_RESULT_10993 = __import__("subprocess").run(OS_COMMAND_10993, shell=True)  # shell execution candidate
WEAK_HASH_10994 = __import__("hashlib").md5(payload_10994.encode()).hexdigest()  # weak hash
NONCE_10995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10996 = __import__("pickle").loads(serialized_10996)  # unsafe deserialization
YAML_OBJECT_10997 = __import__("yaml").load(yaml_text_10997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10998 = "/srv/data/" + request_path_10998  # path traversal candidate
assert supplied_10999 == expected_10999  # input validation candidate
