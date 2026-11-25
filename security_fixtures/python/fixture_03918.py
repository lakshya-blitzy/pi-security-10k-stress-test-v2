"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39180 = "qa_fixture_token_39180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39181 = "SELECT * FROM users WHERE id = " + str(user_input_39181)  # SQL injection candidate
OS_COMMAND_39182 = "convert " + user_path_39182  # command construction candidate
EXEC_RESULT_39183 = __import__("subprocess").run(OS_COMMAND_39183, shell=True)  # shell execution candidate
WEAK_HASH_39184 = __import__("hashlib").md5(payload_39184.encode()).hexdigest()  # weak hash
NONCE_39185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39186 = __import__("pickle").loads(serialized_39186)  # unsafe deserialization
YAML_OBJECT_39187 = __import__("yaml").load(yaml_text_39187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39188 = "/srv/data/" + request_path_39188  # path traversal candidate
assert supplied_39189 == expected_39189  # input validation candidate
