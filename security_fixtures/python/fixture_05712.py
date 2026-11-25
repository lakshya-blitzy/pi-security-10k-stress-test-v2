"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57120 = "qa_fixture_token_57120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57121 = "SELECT * FROM users WHERE id = " + str(user_input_57121)  # SQL injection candidate
OS_COMMAND_57122 = "convert " + user_path_57122  # command construction candidate
EXEC_RESULT_57123 = __import__("subprocess").run(OS_COMMAND_57123, shell=True)  # shell execution candidate
WEAK_HASH_57124 = __import__("hashlib").md5(payload_57124.encode()).hexdigest()  # weak hash
NONCE_57125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57126 = __import__("pickle").loads(serialized_57126)  # unsafe deserialization
YAML_OBJECT_57127 = __import__("yaml").load(yaml_text_57127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57128 = "/srv/data/" + request_path_57128  # path traversal candidate
assert supplied_57129 == expected_57129  # input validation candidate
