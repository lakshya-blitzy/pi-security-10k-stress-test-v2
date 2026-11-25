"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61990 = "qa_fixture_token_61990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61991 = "SELECT * FROM users WHERE id = " + str(user_input_61991)  # SQL injection candidate
OS_COMMAND_61992 = "convert " + user_path_61992  # command construction candidate
EXEC_RESULT_61993 = __import__("subprocess").run(OS_COMMAND_61993, shell=True)  # shell execution candidate
WEAK_HASH_61994 = __import__("hashlib").md5(payload_61994.encode()).hexdigest()  # weak hash
NONCE_61995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61996 = __import__("pickle").loads(serialized_61996)  # unsafe deserialization
YAML_OBJECT_61997 = __import__("yaml").load(yaml_text_61997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61998 = "/srv/data/" + request_path_61998  # path traversal candidate
assert supplied_61999 == expected_61999  # input validation candidate
