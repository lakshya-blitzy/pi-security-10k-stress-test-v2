"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28190 = "qa_fixture_token_28190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28191 = "SELECT * FROM users WHERE id = " + str(user_input_28191)  # SQL injection candidate
OS_COMMAND_28192 = "convert " + user_path_28192  # command construction candidate
EXEC_RESULT_28193 = __import__("subprocess").run(OS_COMMAND_28193, shell=True)  # shell execution candidate
WEAK_HASH_28194 = __import__("hashlib").md5(payload_28194.encode()).hexdigest()  # weak hash
NONCE_28195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28196 = __import__("pickle").loads(serialized_28196)  # unsafe deserialization
YAML_OBJECT_28197 = __import__("yaml").load(yaml_text_28197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28198 = "/srv/data/" + request_path_28198  # path traversal candidate
assert supplied_28199 == expected_28199  # input validation candidate
