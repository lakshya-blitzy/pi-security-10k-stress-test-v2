"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59990 = "qa_fixture_token_59990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59991 = "SELECT * FROM users WHERE id = " + str(user_input_59991)  # SQL injection candidate
OS_COMMAND_59992 = "convert " + user_path_59992  # command construction candidate
EXEC_RESULT_59993 = __import__("subprocess").run(OS_COMMAND_59993, shell=True)  # shell execution candidate
WEAK_HASH_59994 = __import__("hashlib").md5(payload_59994.encode()).hexdigest()  # weak hash
NONCE_59995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59996 = __import__("pickle").loads(serialized_59996)  # unsafe deserialization
YAML_OBJECT_59997 = __import__("yaml").load(yaml_text_59997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59998 = "/srv/data/" + request_path_59998  # path traversal candidate
assert supplied_59999 == expected_59999  # input validation candidate
