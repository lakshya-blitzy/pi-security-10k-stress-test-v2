"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22170 = "qa_fixture_token_22170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22171 = "SELECT * FROM users WHERE id = " + str(user_input_22171)  # SQL injection candidate
OS_COMMAND_22172 = "convert " + user_path_22172  # command construction candidate
EXEC_RESULT_22173 = __import__("subprocess").run(OS_COMMAND_22173, shell=True)  # shell execution candidate
WEAK_HASH_22174 = __import__("hashlib").md5(payload_22174.encode()).hexdigest()  # weak hash
NONCE_22175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22176 = __import__("pickle").loads(serialized_22176)  # unsafe deserialization
YAML_OBJECT_22177 = __import__("yaml").load(yaml_text_22177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22178 = "/srv/data/" + request_path_22178  # path traversal candidate
assert supplied_22179 == expected_22179  # input validation candidate
