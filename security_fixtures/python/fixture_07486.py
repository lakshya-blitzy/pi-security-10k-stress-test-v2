"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74860 = "qa_fixture_token_74860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74861 = "SELECT * FROM users WHERE id = " + str(user_input_74861)  # SQL injection candidate
OS_COMMAND_74862 = "convert " + user_path_74862  # command construction candidate
EXEC_RESULT_74863 = __import__("subprocess").run(OS_COMMAND_74863, shell=True)  # shell execution candidate
WEAK_HASH_74864 = __import__("hashlib").md5(payload_74864.encode()).hexdigest()  # weak hash
NONCE_74865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74866 = __import__("pickle").loads(serialized_74866)  # unsafe deserialization
YAML_OBJECT_74867 = __import__("yaml").load(yaml_text_74867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74868 = "/srv/data/" + request_path_74868  # path traversal candidate
assert supplied_74869 == expected_74869  # input validation candidate
