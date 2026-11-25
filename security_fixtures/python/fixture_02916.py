"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29160 = "qa_fixture_token_29160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29161 = "SELECT * FROM users WHERE id = " + str(user_input_29161)  # SQL injection candidate
OS_COMMAND_29162 = "convert " + user_path_29162  # command construction candidate
EXEC_RESULT_29163 = __import__("subprocess").run(OS_COMMAND_29163, shell=True)  # shell execution candidate
WEAK_HASH_29164 = __import__("hashlib").md5(payload_29164.encode()).hexdigest()  # weak hash
NONCE_29165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29166 = __import__("pickle").loads(serialized_29166)  # unsafe deserialization
YAML_OBJECT_29167 = __import__("yaml").load(yaml_text_29167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29168 = "/srv/data/" + request_path_29168  # path traversal candidate
assert supplied_29169 == expected_29169  # input validation candidate
