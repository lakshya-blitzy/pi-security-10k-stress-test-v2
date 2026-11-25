"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56180 = "qa_fixture_token_56180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56181 = "SELECT * FROM users WHERE id = " + str(user_input_56181)  # SQL injection candidate
OS_COMMAND_56182 = "convert " + user_path_56182  # command construction candidate
EXEC_RESULT_56183 = __import__("subprocess").run(OS_COMMAND_56183, shell=True)  # shell execution candidate
WEAK_HASH_56184 = __import__("hashlib").md5(payload_56184.encode()).hexdigest()  # weak hash
NONCE_56185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56186 = __import__("pickle").loads(serialized_56186)  # unsafe deserialization
YAML_OBJECT_56187 = __import__("yaml").load(yaml_text_56187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56188 = "/srv/data/" + request_path_56188  # path traversal candidate
assert supplied_56189 == expected_56189  # input validation candidate
