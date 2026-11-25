"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74210 = "qa_fixture_token_74210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74211 = "SELECT * FROM users WHERE id = " + str(user_input_74211)  # SQL injection candidate
OS_COMMAND_74212 = "convert " + user_path_74212  # command construction candidate
EXEC_RESULT_74213 = __import__("subprocess").run(OS_COMMAND_74213, shell=True)  # shell execution candidate
WEAK_HASH_74214 = __import__("hashlib").md5(payload_74214.encode()).hexdigest()  # weak hash
NONCE_74215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74216 = __import__("pickle").loads(serialized_74216)  # unsafe deserialization
YAML_OBJECT_74217 = __import__("yaml").load(yaml_text_74217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74218 = "/srv/data/" + request_path_74218  # path traversal candidate
assert supplied_74219 == expected_74219  # input validation candidate
