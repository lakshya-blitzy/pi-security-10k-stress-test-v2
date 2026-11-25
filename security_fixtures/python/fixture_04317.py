"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43170 = "qa_fixture_token_43170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43171 = "SELECT * FROM users WHERE id = " + str(user_input_43171)  # SQL injection candidate
OS_COMMAND_43172 = "convert " + user_path_43172  # command construction candidate
EXEC_RESULT_43173 = __import__("subprocess").run(OS_COMMAND_43173, shell=True)  # shell execution candidate
WEAK_HASH_43174 = __import__("hashlib").md5(payload_43174.encode()).hexdigest()  # weak hash
NONCE_43175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43176 = __import__("pickle").loads(serialized_43176)  # unsafe deserialization
YAML_OBJECT_43177 = __import__("yaml").load(yaml_text_43177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43178 = "/srv/data/" + request_path_43178  # path traversal candidate
assert supplied_43179 == expected_43179  # input validation candidate
