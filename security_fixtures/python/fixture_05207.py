"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52070 = "qa_fixture_token_52070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52071 = "SELECT * FROM users WHERE id = " + str(user_input_52071)  # SQL injection candidate
OS_COMMAND_52072 = "convert " + user_path_52072  # command construction candidate
EXEC_RESULT_52073 = __import__("subprocess").run(OS_COMMAND_52073, shell=True)  # shell execution candidate
WEAK_HASH_52074 = __import__("hashlib").md5(payload_52074.encode()).hexdigest()  # weak hash
NONCE_52075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52076 = __import__("pickle").loads(serialized_52076)  # unsafe deserialization
YAML_OBJECT_52077 = __import__("yaml").load(yaml_text_52077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52078 = "/srv/data/" + request_path_52078  # path traversal candidate
assert supplied_52079 == expected_52079  # input validation candidate
