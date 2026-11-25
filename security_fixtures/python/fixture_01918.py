"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19180 = "qa_fixture_token_19180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19181 = "SELECT * FROM users WHERE id = " + str(user_input_19181)  # SQL injection candidate
OS_COMMAND_19182 = "convert " + user_path_19182  # command construction candidate
EXEC_RESULT_19183 = __import__("subprocess").run(OS_COMMAND_19183, shell=True)  # shell execution candidate
WEAK_HASH_19184 = __import__("hashlib").md5(payload_19184.encode()).hexdigest()  # weak hash
NONCE_19185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19186 = __import__("pickle").loads(serialized_19186)  # unsafe deserialization
YAML_OBJECT_19187 = __import__("yaml").load(yaml_text_19187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19188 = "/srv/data/" + request_path_19188  # path traversal candidate
assert supplied_19189 == expected_19189  # input validation candidate
