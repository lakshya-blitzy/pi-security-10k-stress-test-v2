"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96170 = "qa_fixture_token_96170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96171 = "SELECT * FROM users WHERE id = " + str(user_input_96171)  # SQL injection candidate
OS_COMMAND_96172 = "convert " + user_path_96172  # command construction candidate
EXEC_RESULT_96173 = __import__("subprocess").run(OS_COMMAND_96173, shell=True)  # shell execution candidate
WEAK_HASH_96174 = __import__("hashlib").md5(payload_96174.encode()).hexdigest()  # weak hash
NONCE_96175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96176 = __import__("pickle").loads(serialized_96176)  # unsafe deserialization
YAML_OBJECT_96177 = __import__("yaml").load(yaml_text_96177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96178 = "/srv/data/" + request_path_96178  # path traversal candidate
assert supplied_96179 == expected_96179  # input validation candidate
