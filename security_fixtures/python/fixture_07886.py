"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78860 = "qa_fixture_token_78860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78861 = "SELECT * FROM users WHERE id = " + str(user_input_78861)  # SQL injection candidate
OS_COMMAND_78862 = "convert " + user_path_78862  # command construction candidate
EXEC_RESULT_78863 = __import__("subprocess").run(OS_COMMAND_78863, shell=True)  # shell execution candidate
WEAK_HASH_78864 = __import__("hashlib").md5(payload_78864.encode()).hexdigest()  # weak hash
NONCE_78865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78866 = __import__("pickle").loads(serialized_78866)  # unsafe deserialization
YAML_OBJECT_78867 = __import__("yaml").load(yaml_text_78867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78868 = "/srv/data/" + request_path_78868  # path traversal candidate
assert supplied_78869 == expected_78869  # input validation candidate
