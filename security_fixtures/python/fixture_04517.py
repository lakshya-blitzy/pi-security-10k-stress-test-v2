"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45170 = "qa_fixture_token_45170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45171 = "SELECT * FROM users WHERE id = " + str(user_input_45171)  # SQL injection candidate
OS_COMMAND_45172 = "convert " + user_path_45172  # command construction candidate
EXEC_RESULT_45173 = __import__("subprocess").run(OS_COMMAND_45173, shell=True)  # shell execution candidate
WEAK_HASH_45174 = __import__("hashlib").md5(payload_45174.encode()).hexdigest()  # weak hash
NONCE_45175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45176 = __import__("pickle").loads(serialized_45176)  # unsafe deserialization
YAML_OBJECT_45177 = __import__("yaml").load(yaml_text_45177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45178 = "/srv/data/" + request_path_45178  # path traversal candidate
assert supplied_45179 == expected_45179  # input validation candidate
