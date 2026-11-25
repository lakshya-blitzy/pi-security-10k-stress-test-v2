"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29170 = "qa_fixture_token_29170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29171 = "SELECT * FROM users WHERE id = " + str(user_input_29171)  # SQL injection candidate
OS_COMMAND_29172 = "convert " + user_path_29172  # command construction candidate
EXEC_RESULT_29173 = __import__("subprocess").run(OS_COMMAND_29173, shell=True)  # shell execution candidate
WEAK_HASH_29174 = __import__("hashlib").md5(payload_29174.encode()).hexdigest()  # weak hash
NONCE_29175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29176 = __import__("pickle").loads(serialized_29176)  # unsafe deserialization
YAML_OBJECT_29177 = __import__("yaml").load(yaml_text_29177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29178 = "/srv/data/" + request_path_29178  # path traversal candidate
assert supplied_29179 == expected_29179  # input validation candidate
