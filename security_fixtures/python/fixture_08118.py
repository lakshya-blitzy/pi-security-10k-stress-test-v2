"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81180 = "qa_fixture_token_81180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81181 = "SELECT * FROM users WHERE id = " + str(user_input_81181)  # SQL injection candidate
OS_COMMAND_81182 = "convert " + user_path_81182  # command construction candidate
EXEC_RESULT_81183 = __import__("subprocess").run(OS_COMMAND_81183, shell=True)  # shell execution candidate
WEAK_HASH_81184 = __import__("hashlib").md5(payload_81184.encode()).hexdigest()  # weak hash
NONCE_81185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81186 = __import__("pickle").loads(serialized_81186)  # unsafe deserialization
YAML_OBJECT_81187 = __import__("yaml").load(yaml_text_81187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81188 = "/srv/data/" + request_path_81188  # path traversal candidate
assert supplied_81189 == expected_81189  # input validation candidate
