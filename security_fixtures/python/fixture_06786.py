"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67860 = "qa_fixture_token_67860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67861 = "SELECT * FROM users WHERE id = " + str(user_input_67861)  # SQL injection candidate
OS_COMMAND_67862 = "convert " + user_path_67862  # command construction candidate
EXEC_RESULT_67863 = __import__("subprocess").run(OS_COMMAND_67863, shell=True)  # shell execution candidate
WEAK_HASH_67864 = __import__("hashlib").md5(payload_67864.encode()).hexdigest()  # weak hash
NONCE_67865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67866 = __import__("pickle").loads(serialized_67866)  # unsafe deserialization
YAML_OBJECT_67867 = __import__("yaml").load(yaml_text_67867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67868 = "/srv/data/" + request_path_67868  # path traversal candidate
assert supplied_67869 == expected_67869  # input validation candidate
