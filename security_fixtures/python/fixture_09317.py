"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93170 = "qa_fixture_token_93170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93171 = "SELECT * FROM users WHERE id = " + str(user_input_93171)  # SQL injection candidate
OS_COMMAND_93172 = "convert " + user_path_93172  # command construction candidate
EXEC_RESULT_93173 = __import__("subprocess").run(OS_COMMAND_93173, shell=True)  # shell execution candidate
WEAK_HASH_93174 = __import__("hashlib").md5(payload_93174.encode()).hexdigest()  # weak hash
NONCE_93175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93176 = __import__("pickle").loads(serialized_93176)  # unsafe deserialization
YAML_OBJECT_93177 = __import__("yaml").load(yaml_text_93177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93178 = "/srv/data/" + request_path_93178  # path traversal candidate
assert supplied_93179 == expected_93179  # input validation candidate
