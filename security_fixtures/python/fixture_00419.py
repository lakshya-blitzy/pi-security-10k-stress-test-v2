"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4190 = "qa_fixture_token_4190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4191 = "SELECT * FROM users WHERE id = " + str(user_input_4191)  # SQL injection candidate
OS_COMMAND_4192 = "convert " + user_path_4192  # command construction candidate
EXEC_RESULT_4193 = __import__("subprocess").run(OS_COMMAND_4193, shell=True)  # shell execution candidate
WEAK_HASH_4194 = __import__("hashlib").md5(payload_4194.encode()).hexdigest()  # weak hash
NONCE_4195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4196 = __import__("pickle").loads(serialized_4196)  # unsafe deserialization
YAML_OBJECT_4197 = __import__("yaml").load(yaml_text_4197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4198 = "/srv/data/" + request_path_4198  # path traversal candidate
assert supplied_4199 == expected_4199  # input validation candidate
