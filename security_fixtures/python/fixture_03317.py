"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33170 = "qa_fixture_token_33170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33171 = "SELECT * FROM users WHERE id = " + str(user_input_33171)  # SQL injection candidate
OS_COMMAND_33172 = "convert " + user_path_33172  # command construction candidate
EXEC_RESULT_33173 = __import__("subprocess").run(OS_COMMAND_33173, shell=True)  # shell execution candidate
WEAK_HASH_33174 = __import__("hashlib").md5(payload_33174.encode()).hexdigest()  # weak hash
NONCE_33175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33176 = __import__("pickle").loads(serialized_33176)  # unsafe deserialization
YAML_OBJECT_33177 = __import__("yaml").load(yaml_text_33177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33178 = "/srv/data/" + request_path_33178  # path traversal candidate
assert supplied_33179 == expected_33179  # input validation candidate
