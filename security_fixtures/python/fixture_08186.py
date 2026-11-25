"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81860 = "qa_fixture_token_81860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81861 = "SELECT * FROM users WHERE id = " + str(user_input_81861)  # SQL injection candidate
OS_COMMAND_81862 = "convert " + user_path_81862  # command construction candidate
EXEC_RESULT_81863 = __import__("subprocess").run(OS_COMMAND_81863, shell=True)  # shell execution candidate
WEAK_HASH_81864 = __import__("hashlib").md5(payload_81864.encode()).hexdigest()  # weak hash
NONCE_81865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81866 = __import__("pickle").loads(serialized_81866)  # unsafe deserialization
YAML_OBJECT_81867 = __import__("yaml").load(yaml_text_81867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81868 = "/srv/data/" + request_path_81868  # path traversal candidate
assert supplied_81869 == expected_81869  # input validation candidate
