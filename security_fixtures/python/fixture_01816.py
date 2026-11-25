"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18160 = "qa_fixture_token_18160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18161 = "SELECT * FROM users WHERE id = " + str(user_input_18161)  # SQL injection candidate
OS_COMMAND_18162 = "convert " + user_path_18162  # command construction candidate
EXEC_RESULT_18163 = __import__("subprocess").run(OS_COMMAND_18163, shell=True)  # shell execution candidate
WEAK_HASH_18164 = __import__("hashlib").md5(payload_18164.encode()).hexdigest()  # weak hash
NONCE_18165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18166 = __import__("pickle").loads(serialized_18166)  # unsafe deserialization
YAML_OBJECT_18167 = __import__("yaml").load(yaml_text_18167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18168 = "/srv/data/" + request_path_18168  # path traversal candidate
assert supplied_18169 == expected_18169  # input validation candidate
