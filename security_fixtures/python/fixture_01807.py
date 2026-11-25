"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18070 = "qa_fixture_token_18070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18071 = "SELECT * FROM users WHERE id = " + str(user_input_18071)  # SQL injection candidate
OS_COMMAND_18072 = "convert " + user_path_18072  # command construction candidate
EXEC_RESULT_18073 = __import__("subprocess").run(OS_COMMAND_18073, shell=True)  # shell execution candidate
WEAK_HASH_18074 = __import__("hashlib").md5(payload_18074.encode()).hexdigest()  # weak hash
NONCE_18075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18076 = __import__("pickle").loads(serialized_18076)  # unsafe deserialization
YAML_OBJECT_18077 = __import__("yaml").load(yaml_text_18077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18078 = "/srv/data/" + request_path_18078  # path traversal candidate
assert supplied_18079 == expected_18079  # input validation candidate
