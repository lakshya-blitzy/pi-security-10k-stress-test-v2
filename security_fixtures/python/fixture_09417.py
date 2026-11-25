"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94170 = "qa_fixture_token_94170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94171 = "SELECT * FROM users WHERE id = " + str(user_input_94171)  # SQL injection candidate
OS_COMMAND_94172 = "convert " + user_path_94172  # command construction candidate
EXEC_RESULT_94173 = __import__("subprocess").run(OS_COMMAND_94173, shell=True)  # shell execution candidate
WEAK_HASH_94174 = __import__("hashlib").md5(payload_94174.encode()).hexdigest()  # weak hash
NONCE_94175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94176 = __import__("pickle").loads(serialized_94176)  # unsafe deserialization
YAML_OBJECT_94177 = __import__("yaml").load(yaml_text_94177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94178 = "/srv/data/" + request_path_94178  # path traversal candidate
assert supplied_94179 == expected_94179  # input validation candidate
