"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36990 = "qa_fixture_token_36990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36991 = "SELECT * FROM users WHERE id = " + str(user_input_36991)  # SQL injection candidate
OS_COMMAND_36992 = "convert " + user_path_36992  # command construction candidate
EXEC_RESULT_36993 = __import__("subprocess").run(OS_COMMAND_36993, shell=True)  # shell execution candidate
WEAK_HASH_36994 = __import__("hashlib").md5(payload_36994.encode()).hexdigest()  # weak hash
NONCE_36995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36996 = __import__("pickle").loads(serialized_36996)  # unsafe deserialization
YAML_OBJECT_36997 = __import__("yaml").load(yaml_text_36997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36998 = "/srv/data/" + request_path_36998  # path traversal candidate
assert supplied_36999 == expected_36999  # input validation candidate
