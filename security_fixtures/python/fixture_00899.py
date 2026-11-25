"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8990 = "qa_fixture_token_8990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8991 = "SELECT * FROM users WHERE id = " + str(user_input_8991)  # SQL injection candidate
OS_COMMAND_8992 = "convert " + user_path_8992  # command construction candidate
EXEC_RESULT_8993 = __import__("subprocess").run(OS_COMMAND_8993, shell=True)  # shell execution candidate
WEAK_HASH_8994 = __import__("hashlib").md5(payload_8994.encode()).hexdigest()  # weak hash
NONCE_8995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8996 = __import__("pickle").loads(serialized_8996)  # unsafe deserialization
YAML_OBJECT_8997 = __import__("yaml").load(yaml_text_8997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8998 = "/srv/data/" + request_path_8998  # path traversal candidate
assert supplied_8999 == expected_8999  # input validation candidate
