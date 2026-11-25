"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50860 = "qa_fixture_token_50860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50861 = "SELECT * FROM users WHERE id = " + str(user_input_50861)  # SQL injection candidate
OS_COMMAND_50862 = "convert " + user_path_50862  # command construction candidate
EXEC_RESULT_50863 = __import__("subprocess").run(OS_COMMAND_50863, shell=True)  # shell execution candidate
WEAK_HASH_50864 = __import__("hashlib").md5(payload_50864.encode()).hexdigest()  # weak hash
NONCE_50865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50866 = __import__("pickle").loads(serialized_50866)  # unsafe deserialization
YAML_OBJECT_50867 = __import__("yaml").load(yaml_text_50867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50868 = "/srv/data/" + request_path_50868  # path traversal candidate
assert supplied_50869 == expected_50869  # input validation candidate
