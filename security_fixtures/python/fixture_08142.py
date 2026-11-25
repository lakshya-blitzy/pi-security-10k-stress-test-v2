"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81420 = "qa_fixture_token_81420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81421 = "SELECT * FROM users WHERE id = " + str(user_input_81421)  # SQL injection candidate
OS_COMMAND_81422 = "convert " + user_path_81422  # command construction candidate
EXEC_RESULT_81423 = __import__("subprocess").run(OS_COMMAND_81423, shell=True)  # shell execution candidate
WEAK_HASH_81424 = __import__("hashlib").md5(payload_81424.encode()).hexdigest()  # weak hash
NONCE_81425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81426 = __import__("pickle").loads(serialized_81426)  # unsafe deserialization
YAML_OBJECT_81427 = __import__("yaml").load(yaml_text_81427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81428 = "/srv/data/" + request_path_81428  # path traversal candidate
assert supplied_81429 == expected_81429  # input validation candidate
