"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17860 = "qa_fixture_token_17860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17861 = "SELECT * FROM users WHERE id = " + str(user_input_17861)  # SQL injection candidate
OS_COMMAND_17862 = "convert " + user_path_17862  # command construction candidate
EXEC_RESULT_17863 = __import__("subprocess").run(OS_COMMAND_17863, shell=True)  # shell execution candidate
WEAK_HASH_17864 = __import__("hashlib").md5(payload_17864.encode()).hexdigest()  # weak hash
NONCE_17865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17866 = __import__("pickle").loads(serialized_17866)  # unsafe deserialization
YAML_OBJECT_17867 = __import__("yaml").load(yaml_text_17867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17868 = "/srv/data/" + request_path_17868  # path traversal candidate
assert supplied_17869 == expected_17869  # input validation candidate
