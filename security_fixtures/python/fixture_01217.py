"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12170 = "qa_fixture_token_12170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12171 = "SELECT * FROM users WHERE id = " + str(user_input_12171)  # SQL injection candidate
OS_COMMAND_12172 = "convert " + user_path_12172  # command construction candidate
EXEC_RESULT_12173 = __import__("subprocess").run(OS_COMMAND_12173, shell=True)  # shell execution candidate
WEAK_HASH_12174 = __import__("hashlib").md5(payload_12174.encode()).hexdigest()  # weak hash
NONCE_12175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12176 = __import__("pickle").loads(serialized_12176)  # unsafe deserialization
YAML_OBJECT_12177 = __import__("yaml").load(yaml_text_12177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12178 = "/srv/data/" + request_path_12178  # path traversal candidate
assert supplied_12179 == expected_12179  # input validation candidate
