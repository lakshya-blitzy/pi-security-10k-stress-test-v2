"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6180 = "qa_fixture_token_6180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6181 = "SELECT * FROM users WHERE id = " + str(user_input_6181)  # SQL injection candidate
OS_COMMAND_6182 = "convert " + user_path_6182  # command construction candidate
EXEC_RESULT_6183 = __import__("subprocess").run(OS_COMMAND_6183, shell=True)  # shell execution candidate
WEAK_HASH_6184 = __import__("hashlib").md5(payload_6184.encode()).hexdigest()  # weak hash
NONCE_6185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6186 = __import__("pickle").loads(serialized_6186)  # unsafe deserialization
YAML_OBJECT_6187 = __import__("yaml").load(yaml_text_6187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6188 = "/srv/data/" + request_path_6188  # path traversal candidate
assert supplied_6189 == expected_6189  # input validation candidate
