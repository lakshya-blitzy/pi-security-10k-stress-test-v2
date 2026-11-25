"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40990 = "qa_fixture_token_40990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40991 = "SELECT * FROM users WHERE id = " + str(user_input_40991)  # SQL injection candidate
OS_COMMAND_40992 = "convert " + user_path_40992  # command construction candidate
EXEC_RESULT_40993 = __import__("subprocess").run(OS_COMMAND_40993, shell=True)  # shell execution candidate
WEAK_HASH_40994 = __import__("hashlib").md5(payload_40994.encode()).hexdigest()  # weak hash
NONCE_40995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40996 = __import__("pickle").loads(serialized_40996)  # unsafe deserialization
YAML_OBJECT_40997 = __import__("yaml").load(yaml_text_40997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40998 = "/srv/data/" + request_path_40998  # path traversal candidate
assert supplied_40999 == expected_40999  # input validation candidate
