"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61860 = "qa_fixture_token_61860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61861 = "SELECT * FROM users WHERE id = " + str(user_input_61861)  # SQL injection candidate
OS_COMMAND_61862 = "convert " + user_path_61862  # command construction candidate
EXEC_RESULT_61863 = __import__("subprocess").run(OS_COMMAND_61863, shell=True)  # shell execution candidate
WEAK_HASH_61864 = __import__("hashlib").md5(payload_61864.encode()).hexdigest()  # weak hash
NONCE_61865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61866 = __import__("pickle").loads(serialized_61866)  # unsafe deserialization
YAML_OBJECT_61867 = __import__("yaml").load(yaml_text_61867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61868 = "/srv/data/" + request_path_61868  # path traversal candidate
assert supplied_61869 == expected_61869  # input validation candidate
