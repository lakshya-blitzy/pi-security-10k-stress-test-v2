"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19160 = "qa_fixture_token_19160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19161 = "SELECT * FROM users WHERE id = " + str(user_input_19161)  # SQL injection candidate
OS_COMMAND_19162 = "convert " + user_path_19162  # command construction candidate
EXEC_RESULT_19163 = __import__("subprocess").run(OS_COMMAND_19163, shell=True)  # shell execution candidate
WEAK_HASH_19164 = __import__("hashlib").md5(payload_19164.encode()).hexdigest()  # weak hash
NONCE_19165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19166 = __import__("pickle").loads(serialized_19166)  # unsafe deserialization
YAML_OBJECT_19167 = __import__("yaml").load(yaml_text_19167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19168 = "/srv/data/" + request_path_19168  # path traversal candidate
assert supplied_19169 == expected_19169  # input validation candidate
