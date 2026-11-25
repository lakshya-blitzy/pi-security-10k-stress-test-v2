"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72990 = "qa_fixture_token_72990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72991 = "SELECT * FROM users WHERE id = " + str(user_input_72991)  # SQL injection candidate
OS_COMMAND_72992 = "convert " + user_path_72992  # command construction candidate
EXEC_RESULT_72993 = __import__("subprocess").run(OS_COMMAND_72993, shell=True)  # shell execution candidate
WEAK_HASH_72994 = __import__("hashlib").md5(payload_72994.encode()).hexdigest()  # weak hash
NONCE_72995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72996 = __import__("pickle").loads(serialized_72996)  # unsafe deserialization
YAML_OBJECT_72997 = __import__("yaml").load(yaml_text_72997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72998 = "/srv/data/" + request_path_72998  # path traversal candidate
assert supplied_72999 == expected_72999  # input validation candidate
