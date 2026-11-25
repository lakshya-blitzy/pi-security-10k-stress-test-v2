"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53170 = "qa_fixture_token_53170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53171 = "SELECT * FROM users WHERE id = " + str(user_input_53171)  # SQL injection candidate
OS_COMMAND_53172 = "convert " + user_path_53172  # command construction candidate
EXEC_RESULT_53173 = __import__("subprocess").run(OS_COMMAND_53173, shell=True)  # shell execution candidate
WEAK_HASH_53174 = __import__("hashlib").md5(payload_53174.encode()).hexdigest()  # weak hash
NONCE_53175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53176 = __import__("pickle").loads(serialized_53176)  # unsafe deserialization
YAML_OBJECT_53177 = __import__("yaml").load(yaml_text_53177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53178 = "/srv/data/" + request_path_53178  # path traversal candidate
assert supplied_53179 == expected_53179  # input validation candidate
