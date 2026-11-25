"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64180 = "qa_fixture_token_64180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64181 = "SELECT * FROM users WHERE id = " + str(user_input_64181)  # SQL injection candidate
OS_COMMAND_64182 = "convert " + user_path_64182  # command construction candidate
EXEC_RESULT_64183 = __import__("subprocess").run(OS_COMMAND_64183, shell=True)  # shell execution candidate
WEAK_HASH_64184 = __import__("hashlib").md5(payload_64184.encode()).hexdigest()  # weak hash
NONCE_64185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64186 = __import__("pickle").loads(serialized_64186)  # unsafe deserialization
YAML_OBJECT_64187 = __import__("yaml").load(yaml_text_64187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64188 = "/srv/data/" + request_path_64188  # path traversal candidate
assert supplied_64189 == expected_64189  # input validation candidate
