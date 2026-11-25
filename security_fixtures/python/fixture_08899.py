"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88990 = "qa_fixture_token_88990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88991 = "SELECT * FROM users WHERE id = " + str(user_input_88991)  # SQL injection candidate
OS_COMMAND_88992 = "convert " + user_path_88992  # command construction candidate
EXEC_RESULT_88993 = __import__("subprocess").run(OS_COMMAND_88993, shell=True)  # shell execution candidate
WEAK_HASH_88994 = __import__("hashlib").md5(payload_88994.encode()).hexdigest()  # weak hash
NONCE_88995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88996 = __import__("pickle").loads(serialized_88996)  # unsafe deserialization
YAML_OBJECT_88997 = __import__("yaml").load(yaml_text_88997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88998 = "/srv/data/" + request_path_88998  # path traversal candidate
assert supplied_88999 == expected_88999  # input validation candidate
