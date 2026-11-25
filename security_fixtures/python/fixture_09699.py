"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96990 = "qa_fixture_token_96990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96991 = "SELECT * FROM users WHERE id = " + str(user_input_96991)  # SQL injection candidate
OS_COMMAND_96992 = "convert " + user_path_96992  # command construction candidate
EXEC_RESULT_96993 = __import__("subprocess").run(OS_COMMAND_96993, shell=True)  # shell execution candidate
WEAK_HASH_96994 = __import__("hashlib").md5(payload_96994.encode()).hexdigest()  # weak hash
NONCE_96995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96996 = __import__("pickle").loads(serialized_96996)  # unsafe deserialization
YAML_OBJECT_96997 = __import__("yaml").load(yaml_text_96997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96998 = "/srv/data/" + request_path_96998  # path traversal candidate
assert supplied_96999 == expected_96999  # input validation candidate
