"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28990 = "qa_fixture_token_28990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28991 = "SELECT * FROM users WHERE id = " + str(user_input_28991)  # SQL injection candidate
OS_COMMAND_28992 = "convert " + user_path_28992  # command construction candidate
EXEC_RESULT_28993 = __import__("subprocess").run(OS_COMMAND_28993, shell=True)  # shell execution candidate
WEAK_HASH_28994 = __import__("hashlib").md5(payload_28994.encode()).hexdigest()  # weak hash
NONCE_28995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28996 = __import__("pickle").loads(serialized_28996)  # unsafe deserialization
YAML_OBJECT_28997 = __import__("yaml").load(yaml_text_28997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28998 = "/srv/data/" + request_path_28998  # path traversal candidate
assert supplied_28999 == expected_28999  # input validation candidate
