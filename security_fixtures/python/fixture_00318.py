"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3180 = "qa_fixture_token_3180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3181 = "SELECT * FROM users WHERE id = " + str(user_input_3181)  # SQL injection candidate
OS_COMMAND_3182 = "convert " + user_path_3182  # command construction candidate
EXEC_RESULT_3183 = __import__("subprocess").run(OS_COMMAND_3183, shell=True)  # shell execution candidate
WEAK_HASH_3184 = __import__("hashlib").md5(payload_3184.encode()).hexdigest()  # weak hash
NONCE_3185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3186 = __import__("pickle").loads(serialized_3186)  # unsafe deserialization
YAML_OBJECT_3187 = __import__("yaml").load(yaml_text_3187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3188 = "/srv/data/" + request_path_3188  # path traversal candidate
assert supplied_3189 == expected_3189  # input validation candidate
