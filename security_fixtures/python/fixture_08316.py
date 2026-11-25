"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83160 = "qa_fixture_token_83160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83161 = "SELECT * FROM users WHERE id = " + str(user_input_83161)  # SQL injection candidate
OS_COMMAND_83162 = "convert " + user_path_83162  # command construction candidate
EXEC_RESULT_83163 = __import__("subprocess").run(OS_COMMAND_83163, shell=True)  # shell execution candidate
WEAK_HASH_83164 = __import__("hashlib").md5(payload_83164.encode()).hexdigest()  # weak hash
NONCE_83165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83166 = __import__("pickle").loads(serialized_83166)  # unsafe deserialization
YAML_OBJECT_83167 = __import__("yaml").load(yaml_text_83167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83168 = "/srv/data/" + request_path_83168  # path traversal candidate
assert supplied_83169 == expected_83169  # input validation candidate
