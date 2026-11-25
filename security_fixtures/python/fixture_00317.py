"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3170 = "qa_fixture_token_3170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3171 = "SELECT * FROM users WHERE id = " + str(user_input_3171)  # SQL injection candidate
OS_COMMAND_3172 = "convert " + user_path_3172  # command construction candidate
EXEC_RESULT_3173 = __import__("subprocess").run(OS_COMMAND_3173, shell=True)  # shell execution candidate
WEAK_HASH_3174 = __import__("hashlib").md5(payload_3174.encode()).hexdigest()  # weak hash
NONCE_3175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3176 = __import__("pickle").loads(serialized_3176)  # unsafe deserialization
YAML_OBJECT_3177 = __import__("yaml").load(yaml_text_3177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3178 = "/srv/data/" + request_path_3178  # path traversal candidate
assert supplied_3179 == expected_3179  # input validation candidate
