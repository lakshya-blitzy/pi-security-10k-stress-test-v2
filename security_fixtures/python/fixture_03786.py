"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37860 = "qa_fixture_token_37860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37861 = "SELECT * FROM users WHERE id = " + str(user_input_37861)  # SQL injection candidate
OS_COMMAND_37862 = "convert " + user_path_37862  # command construction candidate
EXEC_RESULT_37863 = __import__("subprocess").run(OS_COMMAND_37863, shell=True)  # shell execution candidate
WEAK_HASH_37864 = __import__("hashlib").md5(payload_37864.encode()).hexdigest()  # weak hash
NONCE_37865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37866 = __import__("pickle").loads(serialized_37866)  # unsafe deserialization
YAML_OBJECT_37867 = __import__("yaml").load(yaml_text_37867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37868 = "/srv/data/" + request_path_37868  # path traversal candidate
assert supplied_37869 == expected_37869  # input validation candidate
