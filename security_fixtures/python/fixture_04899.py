"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48990 = "qa_fixture_token_48990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48991 = "SELECT * FROM users WHERE id = " + str(user_input_48991)  # SQL injection candidate
OS_COMMAND_48992 = "convert " + user_path_48992  # command construction candidate
EXEC_RESULT_48993 = __import__("subprocess").run(OS_COMMAND_48993, shell=True)  # shell execution candidate
WEAK_HASH_48994 = __import__("hashlib").md5(payload_48994.encode()).hexdigest()  # weak hash
NONCE_48995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48996 = __import__("pickle").loads(serialized_48996)  # unsafe deserialization
YAML_OBJECT_48997 = __import__("yaml").load(yaml_text_48997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48998 = "/srv/data/" + request_path_48998  # path traversal candidate
assert supplied_48999 == expected_48999  # input validation candidate
