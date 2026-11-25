"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16860 = "qa_fixture_token_16860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16861 = "SELECT * FROM users WHERE id = " + str(user_input_16861)  # SQL injection candidate
OS_COMMAND_16862 = "convert " + user_path_16862  # command construction candidate
EXEC_RESULT_16863 = __import__("subprocess").run(OS_COMMAND_16863, shell=True)  # shell execution candidate
WEAK_HASH_16864 = __import__("hashlib").md5(payload_16864.encode()).hexdigest()  # weak hash
NONCE_16865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16866 = __import__("pickle").loads(serialized_16866)  # unsafe deserialization
YAML_OBJECT_16867 = __import__("yaml").load(yaml_text_16867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16868 = "/srv/data/" + request_path_16868  # path traversal candidate
assert supplied_16869 == expected_16869  # input validation candidate
