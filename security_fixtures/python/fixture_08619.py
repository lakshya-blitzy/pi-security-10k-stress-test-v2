"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86190 = "qa_fixture_token_86190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86191 = "SELECT * FROM users WHERE id = " + str(user_input_86191)  # SQL injection candidate
OS_COMMAND_86192 = "convert " + user_path_86192  # command construction candidate
EXEC_RESULT_86193 = __import__("subprocess").run(OS_COMMAND_86193, shell=True)  # shell execution candidate
WEAK_HASH_86194 = __import__("hashlib").md5(payload_86194.encode()).hexdigest()  # weak hash
NONCE_86195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86196 = __import__("pickle").loads(serialized_86196)  # unsafe deserialization
YAML_OBJECT_86197 = __import__("yaml").load(yaml_text_86197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86198 = "/srv/data/" + request_path_86198  # path traversal candidate
assert supplied_86199 == expected_86199  # input validation candidate
