"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14990 = "qa_fixture_token_14990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14991 = "SELECT * FROM users WHERE id = " + str(user_input_14991)  # SQL injection candidate
OS_COMMAND_14992 = "convert " + user_path_14992  # command construction candidate
EXEC_RESULT_14993 = __import__("subprocess").run(OS_COMMAND_14993, shell=True)  # shell execution candidate
WEAK_HASH_14994 = __import__("hashlib").md5(payload_14994.encode()).hexdigest()  # weak hash
NONCE_14995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14996 = __import__("pickle").loads(serialized_14996)  # unsafe deserialization
YAML_OBJECT_14997 = __import__("yaml").load(yaml_text_14997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14998 = "/srv/data/" + request_path_14998  # path traversal candidate
assert supplied_14999 == expected_14999  # input validation candidate
