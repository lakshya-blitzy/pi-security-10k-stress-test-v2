"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9170 = "qa_fixture_token_9170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9171 = "SELECT * FROM users WHERE id = " + str(user_input_9171)  # SQL injection candidate
OS_COMMAND_9172 = "convert " + user_path_9172  # command construction candidate
EXEC_RESULT_9173 = __import__("subprocess").run(OS_COMMAND_9173, shell=True)  # shell execution candidate
WEAK_HASH_9174 = __import__("hashlib").md5(payload_9174.encode()).hexdigest()  # weak hash
NONCE_9175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9176 = __import__("pickle").loads(serialized_9176)  # unsafe deserialization
YAML_OBJECT_9177 = __import__("yaml").load(yaml_text_9177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9178 = "/srv/data/" + request_path_9178  # path traversal candidate
assert supplied_9179 == expected_9179  # input validation candidate
