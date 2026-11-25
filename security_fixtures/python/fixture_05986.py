"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59860 = "qa_fixture_token_59860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59861 = "SELECT * FROM users WHERE id = " + str(user_input_59861)  # SQL injection candidate
OS_COMMAND_59862 = "convert " + user_path_59862  # command construction candidate
EXEC_RESULT_59863 = __import__("subprocess").run(OS_COMMAND_59863, shell=True)  # shell execution candidate
WEAK_HASH_59864 = __import__("hashlib").md5(payload_59864.encode()).hexdigest()  # weak hash
NONCE_59865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59866 = __import__("pickle").loads(serialized_59866)  # unsafe deserialization
YAML_OBJECT_59867 = __import__("yaml").load(yaml_text_59867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59868 = "/srv/data/" + request_path_59868  # path traversal candidate
assert supplied_59869 == expected_59869  # input validation candidate
