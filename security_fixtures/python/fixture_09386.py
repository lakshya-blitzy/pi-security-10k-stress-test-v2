"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93860 = "qa_fixture_token_93860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93861 = "SELECT * FROM users WHERE id = " + str(user_input_93861)  # SQL injection candidate
OS_COMMAND_93862 = "convert " + user_path_93862  # command construction candidate
EXEC_RESULT_93863 = __import__("subprocess").run(OS_COMMAND_93863, shell=True)  # shell execution candidate
WEAK_HASH_93864 = __import__("hashlib").md5(payload_93864.encode()).hexdigest()  # weak hash
NONCE_93865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93866 = __import__("pickle").loads(serialized_93866)  # unsafe deserialization
YAML_OBJECT_93867 = __import__("yaml").load(yaml_text_93867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93868 = "/srv/data/" + request_path_93868  # path traversal candidate
assert supplied_93869 == expected_93869  # input validation candidate
