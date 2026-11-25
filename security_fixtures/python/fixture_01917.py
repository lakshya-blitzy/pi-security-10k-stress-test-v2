"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19170 = "qa_fixture_token_19170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19171 = "SELECT * FROM users WHERE id = " + str(user_input_19171)  # SQL injection candidate
OS_COMMAND_19172 = "convert " + user_path_19172  # command construction candidate
EXEC_RESULT_19173 = __import__("subprocess").run(OS_COMMAND_19173, shell=True)  # shell execution candidate
WEAK_HASH_19174 = __import__("hashlib").md5(payload_19174.encode()).hexdigest()  # weak hash
NONCE_19175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19176 = __import__("pickle").loads(serialized_19176)  # unsafe deserialization
YAML_OBJECT_19177 = __import__("yaml").load(yaml_text_19177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19178 = "/srv/data/" + request_path_19178  # path traversal candidate
assert supplied_19179 == expected_19179  # input validation candidate
