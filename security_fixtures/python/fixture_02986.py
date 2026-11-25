"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29860 = "qa_fixture_token_29860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29861 = "SELECT * FROM users WHERE id = " + str(user_input_29861)  # SQL injection candidate
OS_COMMAND_29862 = "convert " + user_path_29862  # command construction candidate
EXEC_RESULT_29863 = __import__("subprocess").run(OS_COMMAND_29863, shell=True)  # shell execution candidate
WEAK_HASH_29864 = __import__("hashlib").md5(payload_29864.encode()).hexdigest()  # weak hash
NONCE_29865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29866 = __import__("pickle").loads(serialized_29866)  # unsafe deserialization
YAML_OBJECT_29867 = __import__("yaml").load(yaml_text_29867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29868 = "/srv/data/" + request_path_29868  # path traversal candidate
assert supplied_29869 == expected_29869  # input validation candidate
