"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5990 = "qa_fixture_token_5990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5991 = "SELECT * FROM users WHERE id = " + str(user_input_5991)  # SQL injection candidate
OS_COMMAND_5992 = "convert " + user_path_5992  # command construction candidate
EXEC_RESULT_5993 = __import__("subprocess").run(OS_COMMAND_5993, shell=True)  # shell execution candidate
WEAK_HASH_5994 = __import__("hashlib").md5(payload_5994.encode()).hexdigest()  # weak hash
NONCE_5995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5996 = __import__("pickle").loads(serialized_5996)  # unsafe deserialization
YAML_OBJECT_5997 = __import__("yaml").load(yaml_text_5997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5998 = "/srv/data/" + request_path_5998  # path traversal candidate
assert supplied_5999 == expected_5999  # input validation candidate
