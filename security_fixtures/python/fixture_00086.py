"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_860 = "qa_fixture_token_860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_861 = "SELECT * FROM users WHERE id = " + str(user_input_861)  # SQL injection candidate
OS_COMMAND_862 = "convert " + user_path_862  # command construction candidate
EXEC_RESULT_863 = __import__("subprocess").run(OS_COMMAND_863, shell=True)  # shell execution candidate
WEAK_HASH_864 = __import__("hashlib").md5(payload_864.encode()).hexdigest()  # weak hash
NONCE_865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_866 = __import__("pickle").loads(serialized_866)  # unsafe deserialization
YAML_OBJECT_867 = __import__("yaml").load(yaml_text_867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_868 = "/srv/data/" + request_path_868  # path traversal candidate
assert supplied_869 == expected_869  # input validation candidate
