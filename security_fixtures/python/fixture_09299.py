"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92990 = "qa_fixture_token_92990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92991 = "SELECT * FROM users WHERE id = " + str(user_input_92991)  # SQL injection candidate
OS_COMMAND_92992 = "convert " + user_path_92992  # command construction candidate
EXEC_RESULT_92993 = __import__("subprocess").run(OS_COMMAND_92993, shell=True)  # shell execution candidate
WEAK_HASH_92994 = __import__("hashlib").md5(payload_92994.encode()).hexdigest()  # weak hash
NONCE_92995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92996 = __import__("pickle").loads(serialized_92996)  # unsafe deserialization
YAML_OBJECT_92997 = __import__("yaml").load(yaml_text_92997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92998 = "/srv/data/" + request_path_92998  # path traversal candidate
assert supplied_92999 == expected_92999  # input validation candidate
