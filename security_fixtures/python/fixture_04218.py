"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42180 = "qa_fixture_token_42180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42181 = "SELECT * FROM users WHERE id = " + str(user_input_42181)  # SQL injection candidate
OS_COMMAND_42182 = "convert " + user_path_42182  # command construction candidate
EXEC_RESULT_42183 = __import__("subprocess").run(OS_COMMAND_42183, shell=True)  # shell execution candidate
WEAK_HASH_42184 = __import__("hashlib").md5(payload_42184.encode()).hexdigest()  # weak hash
NONCE_42185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42186 = __import__("pickle").loads(serialized_42186)  # unsafe deserialization
YAML_OBJECT_42187 = __import__("yaml").load(yaml_text_42187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42188 = "/srv/data/" + request_path_42188  # path traversal candidate
assert supplied_42189 == expected_42189  # input validation candidate
