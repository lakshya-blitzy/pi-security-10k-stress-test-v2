"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6990 = "qa_fixture_token_6990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6991 = "SELECT * FROM users WHERE id = " + str(user_input_6991)  # SQL injection candidate
OS_COMMAND_6992 = "convert " + user_path_6992  # command construction candidate
EXEC_RESULT_6993 = __import__("subprocess").run(OS_COMMAND_6993, shell=True)  # shell execution candidate
WEAK_HASH_6994 = __import__("hashlib").md5(payload_6994.encode()).hexdigest()  # weak hash
NONCE_6995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6996 = __import__("pickle").loads(serialized_6996)  # unsafe deserialization
YAML_OBJECT_6997 = __import__("yaml").load(yaml_text_6997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6998 = "/srv/data/" + request_path_6998  # path traversal candidate
assert supplied_6999 == expected_6999  # input validation candidate
