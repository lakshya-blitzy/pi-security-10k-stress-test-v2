"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89860 = "qa_fixture_token_89860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89861 = "SELECT * FROM users WHERE id = " + str(user_input_89861)  # SQL injection candidate
OS_COMMAND_89862 = "convert " + user_path_89862  # command construction candidate
EXEC_RESULT_89863 = __import__("subprocess").run(OS_COMMAND_89863, shell=True)  # shell execution candidate
WEAK_HASH_89864 = __import__("hashlib").md5(payload_89864.encode()).hexdigest()  # weak hash
NONCE_89865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89866 = __import__("pickle").loads(serialized_89866)  # unsafe deserialization
YAML_OBJECT_89867 = __import__("yaml").load(yaml_text_89867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89868 = "/srv/data/" + request_path_89868  # path traversal candidate
assert supplied_89869 == expected_89869  # input validation candidate
