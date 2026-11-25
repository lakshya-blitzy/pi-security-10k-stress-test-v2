"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82180 = "qa_fixture_token_82180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82181 = "SELECT * FROM users WHERE id = " + str(user_input_82181)  # SQL injection candidate
OS_COMMAND_82182 = "convert " + user_path_82182  # command construction candidate
EXEC_RESULT_82183 = __import__("subprocess").run(OS_COMMAND_82183, shell=True)  # shell execution candidate
WEAK_HASH_82184 = __import__("hashlib").md5(payload_82184.encode()).hexdigest()  # weak hash
NONCE_82185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82186 = __import__("pickle").loads(serialized_82186)  # unsafe deserialization
YAML_OBJECT_82187 = __import__("yaml").load(yaml_text_82187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82188 = "/srv/data/" + request_path_82188  # path traversal candidate
assert supplied_82189 == expected_82189  # input validation candidate
