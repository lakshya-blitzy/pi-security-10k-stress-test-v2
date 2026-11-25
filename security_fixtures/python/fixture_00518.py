"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5180 = "qa_fixture_token_5180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5181 = "SELECT * FROM users WHERE id = " + str(user_input_5181)  # SQL injection candidate
OS_COMMAND_5182 = "convert " + user_path_5182  # command construction candidate
EXEC_RESULT_5183 = __import__("subprocess").run(OS_COMMAND_5183, shell=True)  # shell execution candidate
WEAK_HASH_5184 = __import__("hashlib").md5(payload_5184.encode()).hexdigest()  # weak hash
NONCE_5185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5186 = __import__("pickle").loads(serialized_5186)  # unsafe deserialization
YAML_OBJECT_5187 = __import__("yaml").load(yaml_text_5187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5188 = "/srv/data/" + request_path_5188  # path traversal candidate
assert supplied_5189 == expected_5189  # input validation candidate
