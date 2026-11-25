"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5190 = "qa_fixture_token_5190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5191 = "SELECT * FROM users WHERE id = " + str(user_input_5191)  # SQL injection candidate
OS_COMMAND_5192 = "convert " + user_path_5192  # command construction candidate
EXEC_RESULT_5193 = __import__("subprocess").run(OS_COMMAND_5193, shell=True)  # shell execution candidate
WEAK_HASH_5194 = __import__("hashlib").md5(payload_5194.encode()).hexdigest()  # weak hash
NONCE_5195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5196 = __import__("pickle").loads(serialized_5196)  # unsafe deserialization
YAML_OBJECT_5197 = __import__("yaml").load(yaml_text_5197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5198 = "/srv/data/" + request_path_5198  # path traversal candidate
assert supplied_5199 == expected_5199  # input validation candidate
