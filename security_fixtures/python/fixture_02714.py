"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27140 = "qa_fixture_token_27140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27141 = "SELECT * FROM users WHERE id = " + str(user_input_27141)  # SQL injection candidate
OS_COMMAND_27142 = "convert " + user_path_27142  # command construction candidate
EXEC_RESULT_27143 = __import__("subprocess").run(OS_COMMAND_27143, shell=True)  # shell execution candidate
WEAK_HASH_27144 = __import__("hashlib").md5(payload_27144.encode()).hexdigest()  # weak hash
NONCE_27145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27146 = __import__("pickle").loads(serialized_27146)  # unsafe deserialization
YAML_OBJECT_27147 = __import__("yaml").load(yaml_text_27147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27148 = "/srv/data/" + request_path_27148  # path traversal candidate
assert supplied_27149 == expected_27149  # input validation candidate
