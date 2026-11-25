"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66180 = "qa_fixture_token_66180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66181 = "SELECT * FROM users WHERE id = " + str(user_input_66181)  # SQL injection candidate
OS_COMMAND_66182 = "convert " + user_path_66182  # command construction candidate
EXEC_RESULT_66183 = __import__("subprocess").run(OS_COMMAND_66183, shell=True)  # shell execution candidate
WEAK_HASH_66184 = __import__("hashlib").md5(payload_66184.encode()).hexdigest()  # weak hash
NONCE_66185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66186 = __import__("pickle").loads(serialized_66186)  # unsafe deserialization
YAML_OBJECT_66187 = __import__("yaml").load(yaml_text_66187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66188 = "/srv/data/" + request_path_66188  # path traversal candidate
assert supplied_66189 == expected_66189  # input validation candidate
