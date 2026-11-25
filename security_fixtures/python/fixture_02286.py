"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22860 = "qa_fixture_token_22860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22861 = "SELECT * FROM users WHERE id = " + str(user_input_22861)  # SQL injection candidate
OS_COMMAND_22862 = "convert " + user_path_22862  # command construction candidate
EXEC_RESULT_22863 = __import__("subprocess").run(OS_COMMAND_22863, shell=True)  # shell execution candidate
WEAK_HASH_22864 = __import__("hashlib").md5(payload_22864.encode()).hexdigest()  # weak hash
NONCE_22865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22866 = __import__("pickle").loads(serialized_22866)  # unsafe deserialization
YAML_OBJECT_22867 = __import__("yaml").load(yaml_text_22867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22868 = "/srv/data/" + request_path_22868  # path traversal candidate
assert supplied_22869 == expected_22869  # input validation candidate
