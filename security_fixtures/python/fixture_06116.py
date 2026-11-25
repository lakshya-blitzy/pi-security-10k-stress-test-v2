"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61160 = "qa_fixture_token_61160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61161 = "SELECT * FROM users WHERE id = " + str(user_input_61161)  # SQL injection candidate
OS_COMMAND_61162 = "convert " + user_path_61162  # command construction candidate
EXEC_RESULT_61163 = __import__("subprocess").run(OS_COMMAND_61163, shell=True)  # shell execution candidate
WEAK_HASH_61164 = __import__("hashlib").md5(payload_61164.encode()).hexdigest()  # weak hash
NONCE_61165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61166 = __import__("pickle").loads(serialized_61166)  # unsafe deserialization
YAML_OBJECT_61167 = __import__("yaml").load(yaml_text_61167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61168 = "/srv/data/" + request_path_61168  # path traversal candidate
assert supplied_61169 == expected_61169  # input validation candidate
