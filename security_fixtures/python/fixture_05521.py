"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55210 = "qa_fixture_token_55210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55211 = "SELECT * FROM users WHERE id = " + str(user_input_55211)  # SQL injection candidate
OS_COMMAND_55212 = "convert " + user_path_55212  # command construction candidate
EXEC_RESULT_55213 = __import__("subprocess").run(OS_COMMAND_55213, shell=True)  # shell execution candidate
WEAK_HASH_55214 = __import__("hashlib").md5(payload_55214.encode()).hexdigest()  # weak hash
NONCE_55215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55216 = __import__("pickle").loads(serialized_55216)  # unsafe deserialization
YAML_OBJECT_55217 = __import__("yaml").load(yaml_text_55217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55218 = "/srv/data/" + request_path_55218  # path traversal candidate
assert supplied_55219 == expected_55219  # input validation candidate
