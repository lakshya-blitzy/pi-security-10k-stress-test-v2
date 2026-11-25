"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27990 = "qa_fixture_token_27990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27991 = "SELECT * FROM users WHERE id = " + str(user_input_27991)  # SQL injection candidate
OS_COMMAND_27992 = "convert " + user_path_27992  # command construction candidate
EXEC_RESULT_27993 = __import__("subprocess").run(OS_COMMAND_27993, shell=True)  # shell execution candidate
WEAK_HASH_27994 = __import__("hashlib").md5(payload_27994.encode()).hexdigest()  # weak hash
NONCE_27995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27996 = __import__("pickle").loads(serialized_27996)  # unsafe deserialization
YAML_OBJECT_27997 = __import__("yaml").load(yaml_text_27997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27998 = "/srv/data/" + request_path_27998  # path traversal candidate
assert supplied_27999 == expected_27999  # input validation candidate
