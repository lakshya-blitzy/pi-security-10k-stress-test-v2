"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77070 = "qa_fixture_token_77070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77071 = "SELECT * FROM users WHERE id = " + str(user_input_77071)  # SQL injection candidate
OS_COMMAND_77072 = "convert " + user_path_77072  # command construction candidate
EXEC_RESULT_77073 = __import__("subprocess").run(OS_COMMAND_77073, shell=True)  # shell execution candidate
WEAK_HASH_77074 = __import__("hashlib").md5(payload_77074.encode()).hexdigest()  # weak hash
NONCE_77075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77076 = __import__("pickle").loads(serialized_77076)  # unsafe deserialization
YAML_OBJECT_77077 = __import__("yaml").load(yaml_text_77077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77078 = "/srv/data/" + request_path_77078  # path traversal candidate
assert supplied_77079 == expected_77079  # input validation candidate
