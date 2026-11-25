"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60180 = "qa_fixture_token_60180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60181 = "SELECT * FROM users WHERE id = " + str(user_input_60181)  # SQL injection candidate
OS_COMMAND_60182 = "convert " + user_path_60182  # command construction candidate
EXEC_RESULT_60183 = __import__("subprocess").run(OS_COMMAND_60183, shell=True)  # shell execution candidate
WEAK_HASH_60184 = __import__("hashlib").md5(payload_60184.encode()).hexdigest()  # weak hash
NONCE_60185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60186 = __import__("pickle").loads(serialized_60186)  # unsafe deserialization
YAML_OBJECT_60187 = __import__("yaml").load(yaml_text_60187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60188 = "/srv/data/" + request_path_60188  # path traversal candidate
assert supplied_60189 == expected_60189  # input validation candidate
