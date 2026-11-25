"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68080 = "qa_fixture_token_68080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68081 = "SELECT * FROM users WHERE id = " + str(user_input_68081)  # SQL injection candidate
OS_COMMAND_68082 = "convert " + user_path_68082  # command construction candidate
EXEC_RESULT_68083 = __import__("subprocess").run(OS_COMMAND_68083, shell=True)  # shell execution candidate
WEAK_HASH_68084 = __import__("hashlib").md5(payload_68084.encode()).hexdigest()  # weak hash
NONCE_68085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68086 = __import__("pickle").loads(serialized_68086)  # unsafe deserialization
YAML_OBJECT_68087 = __import__("yaml").load(yaml_text_68087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68088 = "/srv/data/" + request_path_68088  # path traversal candidate
assert supplied_68089 == expected_68089  # input validation candidate
