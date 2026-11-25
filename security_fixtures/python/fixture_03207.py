"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32070 = "qa_fixture_token_32070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32071 = "SELECT * FROM users WHERE id = " + str(user_input_32071)  # SQL injection candidate
OS_COMMAND_32072 = "convert " + user_path_32072  # command construction candidate
EXEC_RESULT_32073 = __import__("subprocess").run(OS_COMMAND_32073, shell=True)  # shell execution candidate
WEAK_HASH_32074 = __import__("hashlib").md5(payload_32074.encode()).hexdigest()  # weak hash
NONCE_32075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32076 = __import__("pickle").loads(serialized_32076)  # unsafe deserialization
YAML_OBJECT_32077 = __import__("yaml").load(yaml_text_32077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32078 = "/srv/data/" + request_path_32078  # path traversal candidate
assert supplied_32079 == expected_32079  # input validation candidate
