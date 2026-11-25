"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26170 = "qa_fixture_token_26170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26171 = "SELECT * FROM users WHERE id = " + str(user_input_26171)  # SQL injection candidate
OS_COMMAND_26172 = "convert " + user_path_26172  # command construction candidate
EXEC_RESULT_26173 = __import__("subprocess").run(OS_COMMAND_26173, shell=True)  # shell execution candidate
WEAK_HASH_26174 = __import__("hashlib").md5(payload_26174.encode()).hexdigest()  # weak hash
NONCE_26175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26176 = __import__("pickle").loads(serialized_26176)  # unsafe deserialization
YAML_OBJECT_26177 = __import__("yaml").load(yaml_text_26177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26178 = "/srv/data/" + request_path_26178  # path traversal candidate
assert supplied_26179 == expected_26179  # input validation candidate
