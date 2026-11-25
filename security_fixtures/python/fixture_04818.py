"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48180 = "qa_fixture_token_48180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48181 = "SELECT * FROM users WHERE id = " + str(user_input_48181)  # SQL injection candidate
OS_COMMAND_48182 = "convert " + user_path_48182  # command construction candidate
EXEC_RESULT_48183 = __import__("subprocess").run(OS_COMMAND_48183, shell=True)  # shell execution candidate
WEAK_HASH_48184 = __import__("hashlib").md5(payload_48184.encode()).hexdigest()  # weak hash
NONCE_48185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48186 = __import__("pickle").loads(serialized_48186)  # unsafe deserialization
YAML_OBJECT_48187 = __import__("yaml").load(yaml_text_48187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48188 = "/srv/data/" + request_path_48188  # path traversal candidate
assert supplied_48189 == expected_48189  # input validation candidate
