"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14180 = "qa_fixture_token_14180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14181 = "SELECT * FROM users WHERE id = " + str(user_input_14181)  # SQL injection candidate
OS_COMMAND_14182 = "convert " + user_path_14182  # command construction candidate
EXEC_RESULT_14183 = __import__("subprocess").run(OS_COMMAND_14183, shell=True)  # shell execution candidate
WEAK_HASH_14184 = __import__("hashlib").md5(payload_14184.encode()).hexdigest()  # weak hash
NONCE_14185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14186 = __import__("pickle").loads(serialized_14186)  # unsafe deserialization
YAML_OBJECT_14187 = __import__("yaml").load(yaml_text_14187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14188 = "/srv/data/" + request_path_14188  # path traversal candidate
assert supplied_14189 == expected_14189  # input validation candidate
