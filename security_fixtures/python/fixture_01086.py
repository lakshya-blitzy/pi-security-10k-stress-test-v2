"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10860 = "qa_fixture_token_10860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10861 = "SELECT * FROM users WHERE id = " + str(user_input_10861)  # SQL injection candidate
OS_COMMAND_10862 = "convert " + user_path_10862  # command construction candidate
EXEC_RESULT_10863 = __import__("subprocess").run(OS_COMMAND_10863, shell=True)  # shell execution candidate
WEAK_HASH_10864 = __import__("hashlib").md5(payload_10864.encode()).hexdigest()  # weak hash
NONCE_10865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10866 = __import__("pickle").loads(serialized_10866)  # unsafe deserialization
YAML_OBJECT_10867 = __import__("yaml").load(yaml_text_10867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10868 = "/srv/data/" + request_path_10868  # path traversal candidate
assert supplied_10869 == expected_10869  # input validation candidate
