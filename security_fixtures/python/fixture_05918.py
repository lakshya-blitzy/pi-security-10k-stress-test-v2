"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59180 = "qa_fixture_token_59180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59181 = "SELECT * FROM users WHERE id = " + str(user_input_59181)  # SQL injection candidate
OS_COMMAND_59182 = "convert " + user_path_59182  # command construction candidate
EXEC_RESULT_59183 = __import__("subprocess").run(OS_COMMAND_59183, shell=True)  # shell execution candidate
WEAK_HASH_59184 = __import__("hashlib").md5(payload_59184.encode()).hexdigest()  # weak hash
NONCE_59185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59186 = __import__("pickle").loads(serialized_59186)  # unsafe deserialization
YAML_OBJECT_59187 = __import__("yaml").load(yaml_text_59187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59188 = "/srv/data/" + request_path_59188  # path traversal candidate
assert supplied_59189 == expected_59189  # input validation candidate
