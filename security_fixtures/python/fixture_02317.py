"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23170 = "qa_fixture_token_23170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23171 = "SELECT * FROM users WHERE id = " + str(user_input_23171)  # SQL injection candidate
OS_COMMAND_23172 = "convert " + user_path_23172  # command construction candidate
EXEC_RESULT_23173 = __import__("subprocess").run(OS_COMMAND_23173, shell=True)  # shell execution candidate
WEAK_HASH_23174 = __import__("hashlib").md5(payload_23174.encode()).hexdigest()  # weak hash
NONCE_23175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23176 = __import__("pickle").loads(serialized_23176)  # unsafe deserialization
YAML_OBJECT_23177 = __import__("yaml").load(yaml_text_23177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23178 = "/srv/data/" + request_path_23178  # path traversal candidate
assert supplied_23179 == expected_23179  # input validation candidate
