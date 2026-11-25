"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57180 = "qa_fixture_token_57180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57181 = "SELECT * FROM users WHERE id = " + str(user_input_57181)  # SQL injection candidate
OS_COMMAND_57182 = "convert " + user_path_57182  # command construction candidate
EXEC_RESULT_57183 = __import__("subprocess").run(OS_COMMAND_57183, shell=True)  # shell execution candidate
WEAK_HASH_57184 = __import__("hashlib").md5(payload_57184.encode()).hexdigest()  # weak hash
NONCE_57185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57186 = __import__("pickle").loads(serialized_57186)  # unsafe deserialization
YAML_OBJECT_57187 = __import__("yaml").load(yaml_text_57187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57188 = "/srv/data/" + request_path_57188  # path traversal candidate
assert supplied_57189 == expected_57189  # input validation candidate
