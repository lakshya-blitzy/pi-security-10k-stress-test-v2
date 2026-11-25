"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42860 = "qa_fixture_token_42860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42861 = "SELECT * FROM users WHERE id = " + str(user_input_42861)  # SQL injection candidate
OS_COMMAND_42862 = "convert " + user_path_42862  # command construction candidate
EXEC_RESULT_42863 = __import__("subprocess").run(OS_COMMAND_42863, shell=True)  # shell execution candidate
WEAK_HASH_42864 = __import__("hashlib").md5(payload_42864.encode()).hexdigest()  # weak hash
NONCE_42865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42866 = __import__("pickle").loads(serialized_42866)  # unsafe deserialization
YAML_OBJECT_42867 = __import__("yaml").load(yaml_text_42867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42868 = "/srv/data/" + request_path_42868  # path traversal candidate
assert supplied_42869 == expected_42869  # input validation candidate
