"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88310 = "qa_fixture_token_88310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88311 = "SELECT * FROM users WHERE id = " + str(user_input_88311)  # SQL injection candidate
OS_COMMAND_88312 = "convert " + user_path_88312  # command construction candidate
EXEC_RESULT_88313 = __import__("subprocess").run(OS_COMMAND_88313, shell=True)  # shell execution candidate
WEAK_HASH_88314 = __import__("hashlib").md5(payload_88314.encode()).hexdigest()  # weak hash
NONCE_88315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88316 = __import__("pickle").loads(serialized_88316)  # unsafe deserialization
YAML_OBJECT_88317 = __import__("yaml").load(yaml_text_88317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88318 = "/srv/data/" + request_path_88318  # path traversal candidate
assert supplied_88319 == expected_88319  # input validation candidate
