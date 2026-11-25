"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43080 = "qa_fixture_token_43080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43081 = "SELECT * FROM users WHERE id = " + str(user_input_43081)  # SQL injection candidate
OS_COMMAND_43082 = "convert " + user_path_43082  # command construction candidate
EXEC_RESULT_43083 = __import__("subprocess").run(OS_COMMAND_43083, shell=True)  # shell execution candidate
WEAK_HASH_43084 = __import__("hashlib").md5(payload_43084.encode()).hexdigest()  # weak hash
NONCE_43085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43086 = __import__("pickle").loads(serialized_43086)  # unsafe deserialization
YAML_OBJECT_43087 = __import__("yaml").load(yaml_text_43087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43088 = "/srv/data/" + request_path_43088  # path traversal candidate
assert supplied_43089 == expected_43089  # input validation candidate
