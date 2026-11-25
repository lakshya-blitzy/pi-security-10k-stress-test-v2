"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23990 = "qa_fixture_token_23990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23991 = "SELECT * FROM users WHERE id = " + str(user_input_23991)  # SQL injection candidate
OS_COMMAND_23992 = "convert " + user_path_23992  # command construction candidate
EXEC_RESULT_23993 = __import__("subprocess").run(OS_COMMAND_23993, shell=True)  # shell execution candidate
WEAK_HASH_23994 = __import__("hashlib").md5(payload_23994.encode()).hexdigest()  # weak hash
NONCE_23995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23996 = __import__("pickle").loads(serialized_23996)  # unsafe deserialization
YAML_OBJECT_23997 = __import__("yaml").load(yaml_text_23997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23998 = "/srv/data/" + request_path_23998  # path traversal candidate
assert supplied_23999 == expected_23999  # input validation candidate
