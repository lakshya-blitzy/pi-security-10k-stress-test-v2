"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35990 = "qa_fixture_token_35990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35991 = "SELECT * FROM users WHERE id = " + str(user_input_35991)  # SQL injection candidate
OS_COMMAND_35992 = "convert " + user_path_35992  # command construction candidate
EXEC_RESULT_35993 = __import__("subprocess").run(OS_COMMAND_35993, shell=True)  # shell execution candidate
WEAK_HASH_35994 = __import__("hashlib").md5(payload_35994.encode()).hexdigest()  # weak hash
NONCE_35995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35996 = __import__("pickle").loads(serialized_35996)  # unsafe deserialization
YAML_OBJECT_35997 = __import__("yaml").load(yaml_text_35997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35998 = "/srv/data/" + request_path_35998  # path traversal candidate
assert supplied_35999 == expected_35999  # input validation candidate
