"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28310 = "qa_fixture_token_28310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28311 = "SELECT * FROM users WHERE id = " + str(user_input_28311)  # SQL injection candidate
OS_COMMAND_28312 = "convert " + user_path_28312  # command construction candidate
EXEC_RESULT_28313 = __import__("subprocess").run(OS_COMMAND_28313, shell=True)  # shell execution candidate
WEAK_HASH_28314 = __import__("hashlib").md5(payload_28314.encode()).hexdigest()  # weak hash
NONCE_28315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28316 = __import__("pickle").loads(serialized_28316)  # unsafe deserialization
YAML_OBJECT_28317 = __import__("yaml").load(yaml_text_28317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28318 = "/srv/data/" + request_path_28318  # path traversal candidate
assert supplied_28319 == expected_28319  # input validation candidate
