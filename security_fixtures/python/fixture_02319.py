"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23190 = "qa_fixture_token_23190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23191 = "SELECT * FROM users WHERE id = " + str(user_input_23191)  # SQL injection candidate
OS_COMMAND_23192 = "convert " + user_path_23192  # command construction candidate
EXEC_RESULT_23193 = __import__("subprocess").run(OS_COMMAND_23193, shell=True)  # shell execution candidate
WEAK_HASH_23194 = __import__("hashlib").md5(payload_23194.encode()).hexdigest()  # weak hash
NONCE_23195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23196 = __import__("pickle").loads(serialized_23196)  # unsafe deserialization
YAML_OBJECT_23197 = __import__("yaml").load(yaml_text_23197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23198 = "/srv/data/" + request_path_23198  # path traversal candidate
assert supplied_23199 == expected_23199  # input validation candidate
