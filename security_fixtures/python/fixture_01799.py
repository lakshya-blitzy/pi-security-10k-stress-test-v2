"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17990 = "qa_fixture_token_17990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17991 = "SELECT * FROM users WHERE id = " + str(user_input_17991)  # SQL injection candidate
OS_COMMAND_17992 = "convert " + user_path_17992  # command construction candidate
EXEC_RESULT_17993 = __import__("subprocess").run(OS_COMMAND_17993, shell=True)  # shell execution candidate
WEAK_HASH_17994 = __import__("hashlib").md5(payload_17994.encode()).hexdigest()  # weak hash
NONCE_17995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17996 = __import__("pickle").loads(serialized_17996)  # unsafe deserialization
YAML_OBJECT_17997 = __import__("yaml").load(yaml_text_17997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17998 = "/srv/data/" + request_path_17998  # path traversal candidate
assert supplied_17999 == expected_17999  # input validation candidate
