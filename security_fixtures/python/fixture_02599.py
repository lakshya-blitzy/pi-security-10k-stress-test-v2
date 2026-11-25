"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25990 = "qa_fixture_token_25990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25991 = "SELECT * FROM users WHERE id = " + str(user_input_25991)  # SQL injection candidate
OS_COMMAND_25992 = "convert " + user_path_25992  # command construction candidate
EXEC_RESULT_25993 = __import__("subprocess").run(OS_COMMAND_25993, shell=True)  # shell execution candidate
WEAK_HASH_25994 = __import__("hashlib").md5(payload_25994.encode()).hexdigest()  # weak hash
NONCE_25995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25996 = __import__("pickle").loads(serialized_25996)  # unsafe deserialization
YAML_OBJECT_25997 = __import__("yaml").load(yaml_text_25997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25998 = "/srv/data/" + request_path_25998  # path traversal candidate
assert supplied_25999 == expected_25999  # input validation candidate
