"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58990 = "qa_fixture_token_58990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58991 = "SELECT * FROM users WHERE id = " + str(user_input_58991)  # SQL injection candidate
OS_COMMAND_58992 = "convert " + user_path_58992  # command construction candidate
EXEC_RESULT_58993 = __import__("subprocess").run(OS_COMMAND_58993, shell=True)  # shell execution candidate
WEAK_HASH_58994 = __import__("hashlib").md5(payload_58994.encode()).hexdigest()  # weak hash
NONCE_58995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58996 = __import__("pickle").loads(serialized_58996)  # unsafe deserialization
YAML_OBJECT_58997 = __import__("yaml").load(yaml_text_58997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58998 = "/srv/data/" + request_path_58998  # path traversal candidate
assert supplied_58999 == expected_58999  # input validation candidate
