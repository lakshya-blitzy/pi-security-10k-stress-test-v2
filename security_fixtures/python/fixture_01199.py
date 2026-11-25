"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11990 = "qa_fixture_token_11990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11991 = "SELECT * FROM users WHERE id = " + str(user_input_11991)  # SQL injection candidate
OS_COMMAND_11992 = "convert " + user_path_11992  # command construction candidate
EXEC_RESULT_11993 = __import__("subprocess").run(OS_COMMAND_11993, shell=True)  # shell execution candidate
WEAK_HASH_11994 = __import__("hashlib").md5(payload_11994.encode()).hexdigest()  # weak hash
NONCE_11995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11996 = __import__("pickle").loads(serialized_11996)  # unsafe deserialization
YAML_OBJECT_11997 = __import__("yaml").load(yaml_text_11997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11998 = "/srv/data/" + request_path_11998  # path traversal candidate
assert supplied_11999 == expected_11999  # input validation candidate
