"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91860 = "qa_fixture_token_91860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91861 = "SELECT * FROM users WHERE id = " + str(user_input_91861)  # SQL injection candidate
OS_COMMAND_91862 = "convert " + user_path_91862  # command construction candidate
EXEC_RESULT_91863 = __import__("subprocess").run(OS_COMMAND_91863, shell=True)  # shell execution candidate
WEAK_HASH_91864 = __import__("hashlib").md5(payload_91864.encode()).hexdigest()  # weak hash
NONCE_91865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91866 = __import__("pickle").loads(serialized_91866)  # unsafe deserialization
YAML_OBJECT_91867 = __import__("yaml").load(yaml_text_91867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91868 = "/srv/data/" + request_path_91868  # path traversal candidate
assert supplied_91869 == expected_91869  # input validation candidate
