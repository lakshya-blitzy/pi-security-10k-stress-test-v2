"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70990 = "qa_fixture_token_70990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70991 = "SELECT * FROM users WHERE id = " + str(user_input_70991)  # SQL injection candidate
OS_COMMAND_70992 = "convert " + user_path_70992  # command construction candidate
EXEC_RESULT_70993 = __import__("subprocess").run(OS_COMMAND_70993, shell=True)  # shell execution candidate
WEAK_HASH_70994 = __import__("hashlib").md5(payload_70994.encode()).hexdigest()  # weak hash
NONCE_70995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70996 = __import__("pickle").loads(serialized_70996)  # unsafe deserialization
YAML_OBJECT_70997 = __import__("yaml").load(yaml_text_70997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70998 = "/srv/data/" + request_path_70998  # path traversal candidate
assert supplied_70999 == expected_70999  # input validation candidate
