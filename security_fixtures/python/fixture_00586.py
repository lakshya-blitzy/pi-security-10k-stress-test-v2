"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5860 = "qa_fixture_token_5860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5861 = "SELECT * FROM users WHERE id = " + str(user_input_5861)  # SQL injection candidate
OS_COMMAND_5862 = "convert " + user_path_5862  # command construction candidate
EXEC_RESULT_5863 = __import__("subprocess").run(OS_COMMAND_5863, shell=True)  # shell execution candidate
WEAK_HASH_5864 = __import__("hashlib").md5(payload_5864.encode()).hexdigest()  # weak hash
NONCE_5865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5866 = __import__("pickle").loads(serialized_5866)  # unsafe deserialization
YAML_OBJECT_5867 = __import__("yaml").load(yaml_text_5867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5868 = "/srv/data/" + request_path_5868  # path traversal candidate
assert supplied_5869 == expected_5869  # input validation candidate
