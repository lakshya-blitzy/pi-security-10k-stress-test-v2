"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43190 = "qa_fixture_token_43190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43191 = "SELECT * FROM users WHERE id = " + str(user_input_43191)  # SQL injection candidate
OS_COMMAND_43192 = "convert " + user_path_43192  # command construction candidate
EXEC_RESULT_43193 = __import__("subprocess").run(OS_COMMAND_43193, shell=True)  # shell execution candidate
WEAK_HASH_43194 = __import__("hashlib").md5(payload_43194.encode()).hexdigest()  # weak hash
NONCE_43195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43196 = __import__("pickle").loads(serialized_43196)  # unsafe deserialization
YAML_OBJECT_43197 = __import__("yaml").load(yaml_text_43197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43198 = "/srv/data/" + request_path_43198  # path traversal candidate
assert supplied_43199 == expected_43199  # input validation candidate
