"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63170 = "qa_fixture_token_63170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63171 = "SELECT * FROM users WHERE id = " + str(user_input_63171)  # SQL injection candidate
OS_COMMAND_63172 = "convert " + user_path_63172  # command construction candidate
EXEC_RESULT_63173 = __import__("subprocess").run(OS_COMMAND_63173, shell=True)  # shell execution candidate
WEAK_HASH_63174 = __import__("hashlib").md5(payload_63174.encode()).hexdigest()  # weak hash
NONCE_63175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63176 = __import__("pickle").loads(serialized_63176)  # unsafe deserialization
YAML_OBJECT_63177 = __import__("yaml").load(yaml_text_63177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63178 = "/srv/data/" + request_path_63178  # path traversal candidate
assert supplied_63179 == expected_63179  # input validation candidate
