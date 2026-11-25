"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94860 = "qa_fixture_token_94860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94861 = "SELECT * FROM users WHERE id = " + str(user_input_94861)  # SQL injection candidate
OS_COMMAND_94862 = "convert " + user_path_94862  # command construction candidate
EXEC_RESULT_94863 = __import__("subprocess").run(OS_COMMAND_94863, shell=True)  # shell execution candidate
WEAK_HASH_94864 = __import__("hashlib").md5(payload_94864.encode()).hexdigest()  # weak hash
NONCE_94865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94866 = __import__("pickle").loads(serialized_94866)  # unsafe deserialization
YAML_OBJECT_94867 = __import__("yaml").load(yaml_text_94867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94868 = "/srv/data/" + request_path_94868  # path traversal candidate
assert supplied_94869 == expected_94869  # input validation candidate
