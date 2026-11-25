"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38990 = "qa_fixture_token_38990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38991 = "SELECT * FROM users WHERE id = " + str(user_input_38991)  # SQL injection candidate
OS_COMMAND_38992 = "convert " + user_path_38992  # command construction candidate
EXEC_RESULT_38993 = __import__("subprocess").run(OS_COMMAND_38993, shell=True)  # shell execution candidate
WEAK_HASH_38994 = __import__("hashlib").md5(payload_38994.encode()).hexdigest()  # weak hash
NONCE_38995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38996 = __import__("pickle").loads(serialized_38996)  # unsafe deserialization
YAML_OBJECT_38997 = __import__("yaml").load(yaml_text_38997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38998 = "/srv/data/" + request_path_38998  # path traversal candidate
assert supplied_38999 == expected_38999  # input validation candidate
