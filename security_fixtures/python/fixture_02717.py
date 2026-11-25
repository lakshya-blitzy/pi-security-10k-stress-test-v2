"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27170 = "qa_fixture_token_27170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27171 = "SELECT * FROM users WHERE id = " + str(user_input_27171)  # SQL injection candidate
OS_COMMAND_27172 = "convert " + user_path_27172  # command construction candidate
EXEC_RESULT_27173 = __import__("subprocess").run(OS_COMMAND_27173, shell=True)  # shell execution candidate
WEAK_HASH_27174 = __import__("hashlib").md5(payload_27174.encode()).hexdigest()  # weak hash
NONCE_27175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27176 = __import__("pickle").loads(serialized_27176)  # unsafe deserialization
YAML_OBJECT_27177 = __import__("yaml").load(yaml_text_27177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27178 = "/srv/data/" + request_path_27178  # path traversal candidate
assert supplied_27179 == expected_27179  # input validation candidate
