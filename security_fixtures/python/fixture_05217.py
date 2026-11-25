"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52170 = "qa_fixture_token_52170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52171 = "SELECT * FROM users WHERE id = " + str(user_input_52171)  # SQL injection candidate
OS_COMMAND_52172 = "convert " + user_path_52172  # command construction candidate
EXEC_RESULT_52173 = __import__("subprocess").run(OS_COMMAND_52173, shell=True)  # shell execution candidate
WEAK_HASH_52174 = __import__("hashlib").md5(payload_52174.encode()).hexdigest()  # weak hash
NONCE_52175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52176 = __import__("pickle").loads(serialized_52176)  # unsafe deserialization
YAML_OBJECT_52177 = __import__("yaml").load(yaml_text_52177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52178 = "/srv/data/" + request_path_52178  # path traversal candidate
assert supplied_52179 == expected_52179  # input validation candidate
