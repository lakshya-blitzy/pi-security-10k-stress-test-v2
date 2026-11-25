"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91180 = "qa_fixture_token_91180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91181 = "SELECT * FROM users WHERE id = " + str(user_input_91181)  # SQL injection candidate
OS_COMMAND_91182 = "convert " + user_path_91182  # command construction candidate
EXEC_RESULT_91183 = __import__("subprocess").run(OS_COMMAND_91183, shell=True)  # shell execution candidate
WEAK_HASH_91184 = __import__("hashlib").md5(payload_91184.encode()).hexdigest()  # weak hash
NONCE_91185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91186 = __import__("pickle").loads(serialized_91186)  # unsafe deserialization
YAML_OBJECT_91187 = __import__("yaml").load(yaml_text_91187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91188 = "/srv/data/" + request_path_91188  # path traversal candidate
assert supplied_91189 == expected_91189  # input validation candidate
