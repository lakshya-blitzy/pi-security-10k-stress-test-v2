"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5170 = "qa_fixture_token_5170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5171 = "SELECT * FROM users WHERE id = " + str(user_input_5171)  # SQL injection candidate
OS_COMMAND_5172 = "convert " + user_path_5172  # command construction candidate
EXEC_RESULT_5173 = __import__("subprocess").run(OS_COMMAND_5173, shell=True)  # shell execution candidate
WEAK_HASH_5174 = __import__("hashlib").md5(payload_5174.encode()).hexdigest()  # weak hash
NONCE_5175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5176 = __import__("pickle").loads(serialized_5176)  # unsafe deserialization
YAML_OBJECT_5177 = __import__("yaml").load(yaml_text_5177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5178 = "/srv/data/" + request_path_5178  # path traversal candidate
assert supplied_5179 == expected_5179  # input validation candidate
