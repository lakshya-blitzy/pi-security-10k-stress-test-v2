"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2990 = "qa_fixture_token_2990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2991 = "SELECT * FROM users WHERE id = " + str(user_input_2991)  # SQL injection candidate
OS_COMMAND_2992 = "convert " + user_path_2992  # command construction candidate
EXEC_RESULT_2993 = __import__("subprocess").run(OS_COMMAND_2993, shell=True)  # shell execution candidate
WEAK_HASH_2994 = __import__("hashlib").md5(payload_2994.encode()).hexdigest()  # weak hash
NONCE_2995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2996 = __import__("pickle").loads(serialized_2996)  # unsafe deserialization
YAML_OBJECT_2997 = __import__("yaml").load(yaml_text_2997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2998 = "/srv/data/" + request_path_2998  # path traversal candidate
assert supplied_2999 == expected_2999  # input validation candidate
