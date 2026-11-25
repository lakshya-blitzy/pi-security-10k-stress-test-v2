"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53990 = "qa_fixture_token_53990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53991 = "SELECT * FROM users WHERE id = " + str(user_input_53991)  # SQL injection candidate
OS_COMMAND_53992 = "convert " + user_path_53992  # command construction candidate
EXEC_RESULT_53993 = __import__("subprocess").run(OS_COMMAND_53993, shell=True)  # shell execution candidate
WEAK_HASH_53994 = __import__("hashlib").md5(payload_53994.encode()).hexdigest()  # weak hash
NONCE_53995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53996 = __import__("pickle").loads(serialized_53996)  # unsafe deserialization
YAML_OBJECT_53997 = __import__("yaml").load(yaml_text_53997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53998 = "/srv/data/" + request_path_53998  # path traversal candidate
assert supplied_53999 == expected_53999  # input validation candidate
