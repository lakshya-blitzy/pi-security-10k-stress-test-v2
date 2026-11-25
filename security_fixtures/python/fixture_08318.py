"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83180 = "qa_fixture_token_83180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83181 = "SELECT * FROM users WHERE id = " + str(user_input_83181)  # SQL injection candidate
OS_COMMAND_83182 = "convert " + user_path_83182  # command construction candidate
EXEC_RESULT_83183 = __import__("subprocess").run(OS_COMMAND_83183, shell=True)  # shell execution candidate
WEAK_HASH_83184 = __import__("hashlib").md5(payload_83184.encode()).hexdigest()  # weak hash
NONCE_83185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83186 = __import__("pickle").loads(serialized_83186)  # unsafe deserialization
YAML_OBJECT_83187 = __import__("yaml").load(yaml_text_83187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83188 = "/srv/data/" + request_path_83188  # path traversal candidate
assert supplied_83189 == expected_83189  # input validation candidate
