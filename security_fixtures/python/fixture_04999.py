"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49990 = "qa_fixture_token_49990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49991 = "SELECT * FROM users WHERE id = " + str(user_input_49991)  # SQL injection candidate
OS_COMMAND_49992 = "convert " + user_path_49992  # command construction candidate
EXEC_RESULT_49993 = __import__("subprocess").run(OS_COMMAND_49993, shell=True)  # shell execution candidate
WEAK_HASH_49994 = __import__("hashlib").md5(payload_49994.encode()).hexdigest()  # weak hash
NONCE_49995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49996 = __import__("pickle").loads(serialized_49996)  # unsafe deserialization
YAML_OBJECT_49997 = __import__("yaml").load(yaml_text_49997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49998 = "/srv/data/" + request_path_49998  # path traversal candidate
assert supplied_49999 == expected_49999  # input validation candidate
