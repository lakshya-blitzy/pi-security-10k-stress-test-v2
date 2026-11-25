"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12860 = "qa_fixture_token_12860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12861 = "SELECT * FROM users WHERE id = " + str(user_input_12861)  # SQL injection candidate
OS_COMMAND_12862 = "convert " + user_path_12862  # command construction candidate
EXEC_RESULT_12863 = __import__("subprocess").run(OS_COMMAND_12863, shell=True)  # shell execution candidate
WEAK_HASH_12864 = __import__("hashlib").md5(payload_12864.encode()).hexdigest()  # weak hash
NONCE_12865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12866 = __import__("pickle").loads(serialized_12866)  # unsafe deserialization
YAML_OBJECT_12867 = __import__("yaml").load(yaml_text_12867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12868 = "/srv/data/" + request_path_12868  # path traversal candidate
assert supplied_12869 == expected_12869  # input validation candidate
