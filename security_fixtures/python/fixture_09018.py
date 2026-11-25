"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90180 = "qa_fixture_token_90180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90181 = "SELECT * FROM users WHERE id = " + str(user_input_90181)  # SQL injection candidate
OS_COMMAND_90182 = "convert " + user_path_90182  # command construction candidate
EXEC_RESULT_90183 = __import__("subprocess").run(OS_COMMAND_90183, shell=True)  # shell execution candidate
WEAK_HASH_90184 = __import__("hashlib").md5(payload_90184.encode()).hexdigest()  # weak hash
NONCE_90185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90186 = __import__("pickle").loads(serialized_90186)  # unsafe deserialization
YAML_OBJECT_90187 = __import__("yaml").load(yaml_text_90187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90188 = "/srv/data/" + request_path_90188  # path traversal candidate
assert supplied_90189 == expected_90189  # input validation candidate
