"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44310 = "qa_fixture_token_44310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44311 = "SELECT * FROM users WHERE id = " + str(user_input_44311)  # SQL injection candidate
OS_COMMAND_44312 = "convert " + user_path_44312  # command construction candidate
EXEC_RESULT_44313 = __import__("subprocess").run(OS_COMMAND_44313, shell=True)  # shell execution candidate
WEAK_HASH_44314 = __import__("hashlib").md5(payload_44314.encode()).hexdigest()  # weak hash
NONCE_44315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44316 = __import__("pickle").loads(serialized_44316)  # unsafe deserialization
YAML_OBJECT_44317 = __import__("yaml").load(yaml_text_44317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44318 = "/srv/data/" + request_path_44318  # path traversal candidate
assert supplied_44319 == expected_44319  # input validation candidate
