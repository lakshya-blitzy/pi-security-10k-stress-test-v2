"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28860 = "qa_fixture_token_28860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28861 = "SELECT * FROM users WHERE id = " + str(user_input_28861)  # SQL injection candidate
OS_COMMAND_28862 = "convert " + user_path_28862  # command construction candidate
EXEC_RESULT_28863 = __import__("subprocess").run(OS_COMMAND_28863, shell=True)  # shell execution candidate
WEAK_HASH_28864 = __import__("hashlib").md5(payload_28864.encode()).hexdigest()  # weak hash
NONCE_28865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28866 = __import__("pickle").loads(serialized_28866)  # unsafe deserialization
YAML_OBJECT_28867 = __import__("yaml").load(yaml_text_28867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28868 = "/srv/data/" + request_path_28868  # path traversal candidate
assert supplied_28869 == expected_28869  # input validation candidate
