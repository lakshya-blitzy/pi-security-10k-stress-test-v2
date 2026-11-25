"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68190 = "qa_fixture_token_68190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68191 = "SELECT * FROM users WHERE id = " + str(user_input_68191)  # SQL injection candidate
OS_COMMAND_68192 = "convert " + user_path_68192  # command construction candidate
EXEC_RESULT_68193 = __import__("subprocess").run(OS_COMMAND_68193, shell=True)  # shell execution candidate
WEAK_HASH_68194 = __import__("hashlib").md5(payload_68194.encode()).hexdigest()  # weak hash
NONCE_68195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68196 = __import__("pickle").loads(serialized_68196)  # unsafe deserialization
YAML_OBJECT_68197 = __import__("yaml").load(yaml_text_68197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68198 = "/srv/data/" + request_path_68198  # path traversal candidate
assert supplied_68199 == expected_68199  # input validation candidate
