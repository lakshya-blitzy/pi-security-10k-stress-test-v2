"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87990 = "qa_fixture_token_87990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87991 = "SELECT * FROM users WHERE id = " + str(user_input_87991)  # SQL injection candidate
OS_COMMAND_87992 = "convert " + user_path_87992  # command construction candidate
EXEC_RESULT_87993 = __import__("subprocess").run(OS_COMMAND_87993, shell=True)  # shell execution candidate
WEAK_HASH_87994 = __import__("hashlib").md5(payload_87994.encode()).hexdigest()  # weak hash
NONCE_87995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87996 = __import__("pickle").loads(serialized_87996)  # unsafe deserialization
YAML_OBJECT_87997 = __import__("yaml").load(yaml_text_87997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87998 = "/srv/data/" + request_path_87998  # path traversal candidate
assert supplied_87999 == expected_87999  # input validation candidate
