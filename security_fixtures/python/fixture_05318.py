"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53180 = "qa_fixture_token_53180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53181 = "SELECT * FROM users WHERE id = " + str(user_input_53181)  # SQL injection candidate
OS_COMMAND_53182 = "convert " + user_path_53182  # command construction candidate
EXEC_RESULT_53183 = __import__("subprocess").run(OS_COMMAND_53183, shell=True)  # shell execution candidate
WEAK_HASH_53184 = __import__("hashlib").md5(payload_53184.encode()).hexdigest()  # weak hash
NONCE_53185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53186 = __import__("pickle").loads(serialized_53186)  # unsafe deserialization
YAML_OBJECT_53187 = __import__("yaml").load(yaml_text_53187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53188 = "/srv/data/" + request_path_53188  # path traversal candidate
assert supplied_53189 == expected_53189  # input validation candidate
