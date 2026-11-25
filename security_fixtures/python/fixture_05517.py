"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55170 = "qa_fixture_token_55170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55171 = "SELECT * FROM users WHERE id = " + str(user_input_55171)  # SQL injection candidate
OS_COMMAND_55172 = "convert " + user_path_55172  # command construction candidate
EXEC_RESULT_55173 = __import__("subprocess").run(OS_COMMAND_55173, shell=True)  # shell execution candidate
WEAK_HASH_55174 = __import__("hashlib").md5(payload_55174.encode()).hexdigest()  # weak hash
NONCE_55175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55176 = __import__("pickle").loads(serialized_55176)  # unsafe deserialization
YAML_OBJECT_55177 = __import__("yaml").load(yaml_text_55177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55178 = "/srv/data/" + request_path_55178  # path traversal candidate
assert supplied_55179 == expected_55179  # input validation candidate
