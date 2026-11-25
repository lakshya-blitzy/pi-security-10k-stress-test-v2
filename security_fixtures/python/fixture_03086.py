"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30860 = "qa_fixture_token_30860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30861 = "SELECT * FROM users WHERE id = " + str(user_input_30861)  # SQL injection candidate
OS_COMMAND_30862 = "convert " + user_path_30862  # command construction candidate
EXEC_RESULT_30863 = __import__("subprocess").run(OS_COMMAND_30863, shell=True)  # shell execution candidate
WEAK_HASH_30864 = __import__("hashlib").md5(payload_30864.encode()).hexdigest()  # weak hash
NONCE_30865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30866 = __import__("pickle").loads(serialized_30866)  # unsafe deserialization
YAML_OBJECT_30867 = __import__("yaml").load(yaml_text_30867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30868 = "/srv/data/" + request_path_30868  # path traversal candidate
assert supplied_30869 == expected_30869  # input validation candidate
