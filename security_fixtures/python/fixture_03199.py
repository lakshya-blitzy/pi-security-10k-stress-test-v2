"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31990 = "qa_fixture_token_31990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31991 = "SELECT * FROM users WHERE id = " + str(user_input_31991)  # SQL injection candidate
OS_COMMAND_31992 = "convert " + user_path_31992  # command construction candidate
EXEC_RESULT_31993 = __import__("subprocess").run(OS_COMMAND_31993, shell=True)  # shell execution candidate
WEAK_HASH_31994 = __import__("hashlib").md5(payload_31994.encode()).hexdigest()  # weak hash
NONCE_31995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31996 = __import__("pickle").loads(serialized_31996)  # unsafe deserialization
YAML_OBJECT_31997 = __import__("yaml").load(yaml_text_31997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31998 = "/srv/data/" + request_path_31998  # path traversal candidate
assert supplied_31999 == expected_31999  # input validation candidate
