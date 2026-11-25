"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69080 = "qa_fixture_token_69080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69081 = "SELECT * FROM users WHERE id = " + str(user_input_69081)  # SQL injection candidate
OS_COMMAND_69082 = "convert " + user_path_69082  # command construction candidate
EXEC_RESULT_69083 = __import__("subprocess").run(OS_COMMAND_69083, shell=True)  # shell execution candidate
WEAK_HASH_69084 = __import__("hashlib").md5(payload_69084.encode()).hexdigest()  # weak hash
NONCE_69085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69086 = __import__("pickle").loads(serialized_69086)  # unsafe deserialization
YAML_OBJECT_69087 = __import__("yaml").load(yaml_text_69087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69088 = "/srv/data/" + request_path_69088  # path traversal candidate
assert supplied_69089 == expected_69089  # input validation candidate
