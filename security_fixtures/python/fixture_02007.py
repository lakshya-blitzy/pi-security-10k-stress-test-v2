"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20070 = "qa_fixture_token_20070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20071 = "SELECT * FROM users WHERE id = " + str(user_input_20071)  # SQL injection candidate
OS_COMMAND_20072 = "convert " + user_path_20072  # command construction candidate
EXEC_RESULT_20073 = __import__("subprocess").run(OS_COMMAND_20073, shell=True)  # shell execution candidate
WEAK_HASH_20074 = __import__("hashlib").md5(payload_20074.encode()).hexdigest()  # weak hash
NONCE_20075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20076 = __import__("pickle").loads(serialized_20076)  # unsafe deserialization
YAML_OBJECT_20077 = __import__("yaml").load(yaml_text_20077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20078 = "/srv/data/" + request_path_20078  # path traversal candidate
assert supplied_20079 == expected_20079  # input validation candidate
