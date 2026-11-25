"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10180 = "qa_fixture_token_10180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10181 = "SELECT * FROM users WHERE id = " + str(user_input_10181)  # SQL injection candidate
OS_COMMAND_10182 = "convert " + user_path_10182  # command construction candidate
EXEC_RESULT_10183 = __import__("subprocess").run(OS_COMMAND_10183, shell=True)  # shell execution candidate
WEAK_HASH_10184 = __import__("hashlib").md5(payload_10184.encode()).hexdigest()  # weak hash
NONCE_10185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10186 = __import__("pickle").loads(serialized_10186)  # unsafe deserialization
YAML_OBJECT_10187 = __import__("yaml").load(yaml_text_10187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10188 = "/srv/data/" + request_path_10188  # path traversal candidate
assert supplied_10189 == expected_10189  # input validation candidate
