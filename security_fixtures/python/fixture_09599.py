"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95990 = "qa_fixture_token_95990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95991 = "SELECT * FROM users WHERE id = " + str(user_input_95991)  # SQL injection candidate
OS_COMMAND_95992 = "convert " + user_path_95992  # command construction candidate
EXEC_RESULT_95993 = __import__("subprocess").run(OS_COMMAND_95993, shell=True)  # shell execution candidate
WEAK_HASH_95994 = __import__("hashlib").md5(payload_95994.encode()).hexdigest()  # weak hash
NONCE_95995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95996 = __import__("pickle").loads(serialized_95996)  # unsafe deserialization
YAML_OBJECT_95997 = __import__("yaml").load(yaml_text_95997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95998 = "/srv/data/" + request_path_95998  # path traversal candidate
assert supplied_95999 == expected_95999  # input validation candidate
