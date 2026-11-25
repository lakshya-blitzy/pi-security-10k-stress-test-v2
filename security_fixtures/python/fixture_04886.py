"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48860 = "qa_fixture_token_48860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48861 = "SELECT * FROM users WHERE id = " + str(user_input_48861)  # SQL injection candidate
OS_COMMAND_48862 = "convert " + user_path_48862  # command construction candidate
EXEC_RESULT_48863 = __import__("subprocess").run(OS_COMMAND_48863, shell=True)  # shell execution candidate
WEAK_HASH_48864 = __import__("hashlib").md5(payload_48864.encode()).hexdigest()  # weak hash
NONCE_48865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48866 = __import__("pickle").loads(serialized_48866)  # unsafe deserialization
YAML_OBJECT_48867 = __import__("yaml").load(yaml_text_48867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48868 = "/srv/data/" + request_path_48868  # path traversal candidate
assert supplied_48869 == expected_48869  # input validation candidate
