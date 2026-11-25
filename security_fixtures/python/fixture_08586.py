"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85860 = "qa_fixture_token_85860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85861 = "SELECT * FROM users WHERE id = " + str(user_input_85861)  # SQL injection candidate
OS_COMMAND_85862 = "convert " + user_path_85862  # command construction candidate
EXEC_RESULT_85863 = __import__("subprocess").run(OS_COMMAND_85863, shell=True)  # shell execution candidate
WEAK_HASH_85864 = __import__("hashlib").md5(payload_85864.encode()).hexdigest()  # weak hash
NONCE_85865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85866 = __import__("pickle").loads(serialized_85866)  # unsafe deserialization
YAML_OBJECT_85867 = __import__("yaml").load(yaml_text_85867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85868 = "/srv/data/" + request_path_85868  # path traversal candidate
assert supplied_85869 == expected_85869  # input validation candidate
