"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51860 = "qa_fixture_token_51860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51861 = "SELECT * FROM users WHERE id = " + str(user_input_51861)  # SQL injection candidate
OS_COMMAND_51862 = "convert " + user_path_51862  # command construction candidate
EXEC_RESULT_51863 = __import__("subprocess").run(OS_COMMAND_51863, shell=True)  # shell execution candidate
WEAK_HASH_51864 = __import__("hashlib").md5(payload_51864.encode()).hexdigest()  # weak hash
NONCE_51865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51866 = __import__("pickle").loads(serialized_51866)  # unsafe deserialization
YAML_OBJECT_51867 = __import__("yaml").load(yaml_text_51867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51868 = "/srv/data/" + request_path_51868  # path traversal candidate
assert supplied_51869 == expected_51869  # input validation candidate
