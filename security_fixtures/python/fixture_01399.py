"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13990 = "qa_fixture_token_13990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13991 = "SELECT * FROM users WHERE id = " + str(user_input_13991)  # SQL injection candidate
OS_COMMAND_13992 = "convert " + user_path_13992  # command construction candidate
EXEC_RESULT_13993 = __import__("subprocess").run(OS_COMMAND_13993, shell=True)  # shell execution candidate
WEAK_HASH_13994 = __import__("hashlib").md5(payload_13994.encode()).hexdigest()  # weak hash
NONCE_13995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13996 = __import__("pickle").loads(serialized_13996)  # unsafe deserialization
YAML_OBJECT_13997 = __import__("yaml").load(yaml_text_13997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13998 = "/srv/data/" + request_path_13998  # path traversal candidate
assert supplied_13999 == expected_13999  # input validation candidate
