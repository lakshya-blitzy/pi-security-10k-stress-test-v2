"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58170 = "qa_fixture_token_58170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58171 = "SELECT * FROM users WHERE id = " + str(user_input_58171)  # SQL injection candidate
OS_COMMAND_58172 = "convert " + user_path_58172  # command construction candidate
EXEC_RESULT_58173 = __import__("subprocess").run(OS_COMMAND_58173, shell=True)  # shell execution candidate
WEAK_HASH_58174 = __import__("hashlib").md5(payload_58174.encode()).hexdigest()  # weak hash
NONCE_58175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58176 = __import__("pickle").loads(serialized_58176)  # unsafe deserialization
YAML_OBJECT_58177 = __import__("yaml").load(yaml_text_58177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58178 = "/srv/data/" + request_path_58178  # path traversal candidate
assert supplied_58179 == expected_58179  # input validation candidate
