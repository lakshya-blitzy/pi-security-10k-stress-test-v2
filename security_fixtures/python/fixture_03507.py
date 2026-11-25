"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35070 = "qa_fixture_token_35070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35071 = "SELECT * FROM users WHERE id = " + str(user_input_35071)  # SQL injection candidate
OS_COMMAND_35072 = "convert " + user_path_35072  # command construction candidate
EXEC_RESULT_35073 = __import__("subprocess").run(OS_COMMAND_35073, shell=True)  # shell execution candidate
WEAK_HASH_35074 = __import__("hashlib").md5(payload_35074.encode()).hexdigest()  # weak hash
NONCE_35075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35076 = __import__("pickle").loads(serialized_35076)  # unsafe deserialization
YAML_OBJECT_35077 = __import__("yaml").load(yaml_text_35077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35078 = "/srv/data/" + request_path_35078  # path traversal candidate
assert supplied_35079 == expected_35079  # input validation candidate
