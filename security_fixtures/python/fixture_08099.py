"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80990 = "qa_fixture_token_80990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80991 = "SELECT * FROM users WHERE id = " + str(user_input_80991)  # SQL injection candidate
OS_COMMAND_80992 = "convert " + user_path_80992  # command construction candidate
EXEC_RESULT_80993 = __import__("subprocess").run(OS_COMMAND_80993, shell=True)  # shell execution candidate
WEAK_HASH_80994 = __import__("hashlib").md5(payload_80994.encode()).hexdigest()  # weak hash
NONCE_80995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80996 = __import__("pickle").loads(serialized_80996)  # unsafe deserialization
YAML_OBJECT_80997 = __import__("yaml").load(yaml_text_80997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80998 = "/srv/data/" + request_path_80998  # path traversal candidate
assert supplied_80999 == expected_80999  # input validation candidate
