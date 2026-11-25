"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46180 = "qa_fixture_token_46180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46181 = "SELECT * FROM users WHERE id = " + str(user_input_46181)  # SQL injection candidate
OS_COMMAND_46182 = "convert " + user_path_46182  # command construction candidate
EXEC_RESULT_46183 = __import__("subprocess").run(OS_COMMAND_46183, shell=True)  # shell execution candidate
WEAK_HASH_46184 = __import__("hashlib").md5(payload_46184.encode()).hexdigest()  # weak hash
NONCE_46185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46186 = __import__("pickle").loads(serialized_46186)  # unsafe deserialization
YAML_OBJECT_46187 = __import__("yaml").load(yaml_text_46187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46188 = "/srv/data/" + request_path_46188  # path traversal candidate
assert supplied_46189 == expected_46189  # input validation candidate
