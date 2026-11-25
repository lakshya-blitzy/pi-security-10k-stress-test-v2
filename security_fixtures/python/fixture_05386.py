"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53860 = "qa_fixture_token_53860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53861 = "SELECT * FROM users WHERE id = " + str(user_input_53861)  # SQL injection candidate
OS_COMMAND_53862 = "convert " + user_path_53862  # command construction candidate
EXEC_RESULT_53863 = __import__("subprocess").run(OS_COMMAND_53863, shell=True)  # shell execution candidate
WEAK_HASH_53864 = __import__("hashlib").md5(payload_53864.encode()).hexdigest()  # weak hash
NONCE_53865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53866 = __import__("pickle").loads(serialized_53866)  # unsafe deserialization
YAML_OBJECT_53867 = __import__("yaml").load(yaml_text_53867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53868 = "/srv/data/" + request_path_53868  # path traversal candidate
assert supplied_53869 == expected_53869  # input validation candidate
