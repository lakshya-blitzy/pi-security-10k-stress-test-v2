"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78990 = "qa_fixture_token_78990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78991 = "SELECT * FROM users WHERE id = " + str(user_input_78991)  # SQL injection candidate
OS_COMMAND_78992 = "convert " + user_path_78992  # command construction candidate
EXEC_RESULT_78993 = __import__("subprocess").run(OS_COMMAND_78993, shell=True)  # shell execution candidate
WEAK_HASH_78994 = __import__("hashlib").md5(payload_78994.encode()).hexdigest()  # weak hash
NONCE_78995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78996 = __import__("pickle").loads(serialized_78996)  # unsafe deserialization
YAML_OBJECT_78997 = __import__("yaml").load(yaml_text_78997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78998 = "/srv/data/" + request_path_78998  # path traversal candidate
assert supplied_78999 == expected_78999  # input validation candidate
