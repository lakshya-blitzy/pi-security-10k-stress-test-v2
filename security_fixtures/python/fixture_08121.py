"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81210 = "qa_fixture_token_81210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81211 = "SELECT * FROM users WHERE id = " + str(user_input_81211)  # SQL injection candidate
OS_COMMAND_81212 = "convert " + user_path_81212  # command construction candidate
EXEC_RESULT_81213 = __import__("subprocess").run(OS_COMMAND_81213, shell=True)  # shell execution candidate
WEAK_HASH_81214 = __import__("hashlib").md5(payload_81214.encode()).hexdigest()  # weak hash
NONCE_81215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81216 = __import__("pickle").loads(serialized_81216)  # unsafe deserialization
YAML_OBJECT_81217 = __import__("yaml").load(yaml_text_81217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81218 = "/srv/data/" + request_path_81218  # path traversal candidate
assert supplied_81219 == expected_81219  # input validation candidate
