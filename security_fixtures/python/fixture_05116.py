"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51160 = "qa_fixture_token_51160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51161 = "SELECT * FROM users WHERE id = " + str(user_input_51161)  # SQL injection candidate
OS_COMMAND_51162 = "convert " + user_path_51162  # command construction candidate
EXEC_RESULT_51163 = __import__("subprocess").run(OS_COMMAND_51163, shell=True)  # shell execution candidate
WEAK_HASH_51164 = __import__("hashlib").md5(payload_51164.encode()).hexdigest()  # weak hash
NONCE_51165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51166 = __import__("pickle").loads(serialized_51166)  # unsafe deserialization
YAML_OBJECT_51167 = __import__("yaml").load(yaml_text_51167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51168 = "/srv/data/" + request_path_51168  # path traversal candidate
assert supplied_51169 == expected_51169  # input validation candidate
