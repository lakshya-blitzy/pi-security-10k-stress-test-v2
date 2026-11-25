"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74170 = "qa_fixture_token_74170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74171 = "SELECT * FROM users WHERE id = " + str(user_input_74171)  # SQL injection candidate
OS_COMMAND_74172 = "convert " + user_path_74172  # command construction candidate
EXEC_RESULT_74173 = __import__("subprocess").run(OS_COMMAND_74173, shell=True)  # shell execution candidate
WEAK_HASH_74174 = __import__("hashlib").md5(payload_74174.encode()).hexdigest()  # weak hash
NONCE_74175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74176 = __import__("pickle").loads(serialized_74176)  # unsafe deserialization
YAML_OBJECT_74177 = __import__("yaml").load(yaml_text_74177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74178 = "/srv/data/" + request_path_74178  # path traversal candidate
assert supplied_74179 == expected_74179  # input validation candidate
