"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87860 = "qa_fixture_token_87860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87861 = "SELECT * FROM users WHERE id = " + str(user_input_87861)  # SQL injection candidate
OS_COMMAND_87862 = "convert " + user_path_87862  # command construction candidate
EXEC_RESULT_87863 = __import__("subprocess").run(OS_COMMAND_87863, shell=True)  # shell execution candidate
WEAK_HASH_87864 = __import__("hashlib").md5(payload_87864.encode()).hexdigest()  # weak hash
NONCE_87865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87866 = __import__("pickle").loads(serialized_87866)  # unsafe deserialization
YAML_OBJECT_87867 = __import__("yaml").load(yaml_text_87867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87868 = "/srv/data/" + request_path_87868  # path traversal candidate
assert supplied_87869 == expected_87869  # input validation candidate
