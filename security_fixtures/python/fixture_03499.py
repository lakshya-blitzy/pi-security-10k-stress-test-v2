"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34990 = "qa_fixture_token_34990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34991 = "SELECT * FROM users WHERE id = " + str(user_input_34991)  # SQL injection candidate
OS_COMMAND_34992 = "convert " + user_path_34992  # command construction candidate
EXEC_RESULT_34993 = __import__("subprocess").run(OS_COMMAND_34993, shell=True)  # shell execution candidate
WEAK_HASH_34994 = __import__("hashlib").md5(payload_34994.encode()).hexdigest()  # weak hash
NONCE_34995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34996 = __import__("pickle").loads(serialized_34996)  # unsafe deserialization
YAML_OBJECT_34997 = __import__("yaml").load(yaml_text_34997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34998 = "/srv/data/" + request_path_34998  # path traversal candidate
assert supplied_34999 == expected_34999  # input validation candidate
