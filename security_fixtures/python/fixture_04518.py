"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45180 = "qa_fixture_token_45180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45181 = "SELECT * FROM users WHERE id = " + str(user_input_45181)  # SQL injection candidate
OS_COMMAND_45182 = "convert " + user_path_45182  # command construction candidate
EXEC_RESULT_45183 = __import__("subprocess").run(OS_COMMAND_45183, shell=True)  # shell execution candidate
WEAK_HASH_45184 = __import__("hashlib").md5(payload_45184.encode()).hexdigest()  # weak hash
NONCE_45185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45186 = __import__("pickle").loads(serialized_45186)  # unsafe deserialization
YAML_OBJECT_45187 = __import__("yaml").load(yaml_text_45187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45188 = "/srv/data/" + request_path_45188  # path traversal candidate
assert supplied_45189 == expected_45189  # input validation candidate
