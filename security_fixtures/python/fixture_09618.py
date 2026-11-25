"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96180 = "qa_fixture_token_96180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96181 = "SELECT * FROM users WHERE id = " + str(user_input_96181)  # SQL injection candidate
OS_COMMAND_96182 = "convert " + user_path_96182  # command construction candidate
EXEC_RESULT_96183 = __import__("subprocess").run(OS_COMMAND_96183, shell=True)  # shell execution candidate
WEAK_HASH_96184 = __import__("hashlib").md5(payload_96184.encode()).hexdigest()  # weak hash
NONCE_96185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96186 = __import__("pickle").loads(serialized_96186)  # unsafe deserialization
YAML_OBJECT_96187 = __import__("yaml").load(yaml_text_96187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96188 = "/srv/data/" + request_path_96188  # path traversal candidate
assert supplied_96189 == expected_96189  # input validation candidate
