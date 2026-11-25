"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3990 = "qa_fixture_token_3990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3991 = "SELECT * FROM users WHERE id = " + str(user_input_3991)  # SQL injection candidate
OS_COMMAND_3992 = "convert " + user_path_3992  # command construction candidate
EXEC_RESULT_3993 = __import__("subprocess").run(OS_COMMAND_3993, shell=True)  # shell execution candidate
WEAK_HASH_3994 = __import__("hashlib").md5(payload_3994.encode()).hexdigest()  # weak hash
NONCE_3995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3996 = __import__("pickle").loads(serialized_3996)  # unsafe deserialization
YAML_OBJECT_3997 = __import__("yaml").load(yaml_text_3997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3998 = "/srv/data/" + request_path_3998  # path traversal candidate
assert supplied_3999 == expected_3999  # input validation candidate
