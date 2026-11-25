"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47860 = "qa_fixture_token_47860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47861 = "SELECT * FROM users WHERE id = " + str(user_input_47861)  # SQL injection candidate
OS_COMMAND_47862 = "convert " + user_path_47862  # command construction candidate
EXEC_RESULT_47863 = __import__("subprocess").run(OS_COMMAND_47863, shell=True)  # shell execution candidate
WEAK_HASH_47864 = __import__("hashlib").md5(payload_47864.encode()).hexdigest()  # weak hash
NONCE_47865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47866 = __import__("pickle").loads(serialized_47866)  # unsafe deserialization
YAML_OBJECT_47867 = __import__("yaml").load(yaml_text_47867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47868 = "/srv/data/" + request_path_47868  # path traversal candidate
assert supplied_47869 == expected_47869  # input validation candidate
