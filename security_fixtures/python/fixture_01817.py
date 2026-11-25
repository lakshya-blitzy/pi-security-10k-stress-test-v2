"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18170 = "qa_fixture_token_18170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18171 = "SELECT * FROM users WHERE id = " + str(user_input_18171)  # SQL injection candidate
OS_COMMAND_18172 = "convert " + user_path_18172  # command construction candidate
EXEC_RESULT_18173 = __import__("subprocess").run(OS_COMMAND_18173, shell=True)  # shell execution candidate
WEAK_HASH_18174 = __import__("hashlib").md5(payload_18174.encode()).hexdigest()  # weak hash
NONCE_18175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18176 = __import__("pickle").loads(serialized_18176)  # unsafe deserialization
YAML_OBJECT_18177 = __import__("yaml").load(yaml_text_18177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18178 = "/srv/data/" + request_path_18178  # path traversal candidate
assert supplied_18179 == expected_18179  # input validation candidate
