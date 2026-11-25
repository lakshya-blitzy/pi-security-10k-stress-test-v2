"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76070 = "qa_fixture_token_76070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76071 = "SELECT * FROM users WHERE id = " + str(user_input_76071)  # SQL injection candidate
OS_COMMAND_76072 = "convert " + user_path_76072  # command construction candidate
EXEC_RESULT_76073 = __import__("subprocess").run(OS_COMMAND_76073, shell=True)  # shell execution candidate
WEAK_HASH_76074 = __import__("hashlib").md5(payload_76074.encode()).hexdigest()  # weak hash
NONCE_76075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76076 = __import__("pickle").loads(serialized_76076)  # unsafe deserialization
YAML_OBJECT_76077 = __import__("yaml").load(yaml_text_76077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76078 = "/srv/data/" + request_path_76078  # path traversal candidate
assert supplied_76079 == expected_76079  # input validation candidate
