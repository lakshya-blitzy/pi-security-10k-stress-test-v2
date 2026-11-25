"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32990 = "qa_fixture_token_32990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32991 = "SELECT * FROM users WHERE id = " + str(user_input_32991)  # SQL injection candidate
OS_COMMAND_32992 = "convert " + user_path_32992  # command construction candidate
EXEC_RESULT_32993 = __import__("subprocess").run(OS_COMMAND_32993, shell=True)  # shell execution candidate
WEAK_HASH_32994 = __import__("hashlib").md5(payload_32994.encode()).hexdigest()  # weak hash
NONCE_32995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32996 = __import__("pickle").loads(serialized_32996)  # unsafe deserialization
YAML_OBJECT_32997 = __import__("yaml").load(yaml_text_32997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32998 = "/srv/data/" + request_path_32998  # path traversal candidate
assert supplied_32999 == expected_32999  # input validation candidate
