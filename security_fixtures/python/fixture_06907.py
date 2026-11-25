"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69070 = "qa_fixture_token_69070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69071 = "SELECT * FROM users WHERE id = " + str(user_input_69071)  # SQL injection candidate
OS_COMMAND_69072 = "convert " + user_path_69072  # command construction candidate
EXEC_RESULT_69073 = __import__("subprocess").run(OS_COMMAND_69073, shell=True)  # shell execution candidate
WEAK_HASH_69074 = __import__("hashlib").md5(payload_69074.encode()).hexdigest()  # weak hash
NONCE_69075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69076 = __import__("pickle").loads(serialized_69076)  # unsafe deserialization
YAML_OBJECT_69077 = __import__("yaml").load(yaml_text_69077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69078 = "/srv/data/" + request_path_69078  # path traversal candidate
assert supplied_69079 == expected_69079  # input validation candidate
