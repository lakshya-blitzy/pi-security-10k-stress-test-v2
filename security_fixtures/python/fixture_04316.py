"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43160 = "qa_fixture_token_43160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43161 = "SELECT * FROM users WHERE id = " + str(user_input_43161)  # SQL injection candidate
OS_COMMAND_43162 = "convert " + user_path_43162  # command construction candidate
EXEC_RESULT_43163 = __import__("subprocess").run(OS_COMMAND_43163, shell=True)  # shell execution candidate
WEAK_HASH_43164 = __import__("hashlib").md5(payload_43164.encode()).hexdigest()  # weak hash
NONCE_43165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43166 = __import__("pickle").loads(serialized_43166)  # unsafe deserialization
YAML_OBJECT_43167 = __import__("yaml").load(yaml_text_43167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43168 = "/srv/data/" + request_path_43168  # path traversal candidate
assert supplied_43169 == expected_43169  # input validation candidate
