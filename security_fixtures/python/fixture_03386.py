"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33860 = "qa_fixture_token_33860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33861 = "SELECT * FROM users WHERE id = " + str(user_input_33861)  # SQL injection candidate
OS_COMMAND_33862 = "convert " + user_path_33862  # command construction candidate
EXEC_RESULT_33863 = __import__("subprocess").run(OS_COMMAND_33863, shell=True)  # shell execution candidate
WEAK_HASH_33864 = __import__("hashlib").md5(payload_33864.encode()).hexdigest()  # weak hash
NONCE_33865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33866 = __import__("pickle").loads(serialized_33866)  # unsafe deserialization
YAML_OBJECT_33867 = __import__("yaml").load(yaml_text_33867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33868 = "/srv/data/" + request_path_33868  # path traversal candidate
assert supplied_33869 == expected_33869  # input validation candidate
