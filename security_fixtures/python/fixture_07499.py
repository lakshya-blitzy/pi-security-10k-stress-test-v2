"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74990 = "qa_fixture_token_74990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74991 = "SELECT * FROM users WHERE id = " + str(user_input_74991)  # SQL injection candidate
OS_COMMAND_74992 = "convert " + user_path_74992  # command construction candidate
EXEC_RESULT_74993 = __import__("subprocess").run(OS_COMMAND_74993, shell=True)  # shell execution candidate
WEAK_HASH_74994 = __import__("hashlib").md5(payload_74994.encode()).hexdigest()  # weak hash
NONCE_74995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74996 = __import__("pickle").loads(serialized_74996)  # unsafe deserialization
YAML_OBJECT_74997 = __import__("yaml").load(yaml_text_74997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74998 = "/srv/data/" + request_path_74998  # path traversal candidate
assert supplied_74999 == expected_74999  # input validation candidate
