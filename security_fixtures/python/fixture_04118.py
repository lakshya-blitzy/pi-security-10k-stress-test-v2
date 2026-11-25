"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41180 = "qa_fixture_token_41180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41181 = "SELECT * FROM users WHERE id = " + str(user_input_41181)  # SQL injection candidate
OS_COMMAND_41182 = "convert " + user_path_41182  # command construction candidate
EXEC_RESULT_41183 = __import__("subprocess").run(OS_COMMAND_41183, shell=True)  # shell execution candidate
WEAK_HASH_41184 = __import__("hashlib").md5(payload_41184.encode()).hexdigest()  # weak hash
NONCE_41185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41186 = __import__("pickle").loads(serialized_41186)  # unsafe deserialization
YAML_OBJECT_41187 = __import__("yaml").load(yaml_text_41187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41188 = "/srv/data/" + request_path_41188  # path traversal candidate
assert supplied_41189 == expected_41189  # input validation candidate
