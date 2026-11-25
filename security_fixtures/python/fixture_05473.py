"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54730 = "qa_fixture_token_54730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54731 = "SELECT * FROM users WHERE id = " + str(user_input_54731)  # SQL injection candidate
OS_COMMAND_54732 = "convert " + user_path_54732  # command construction candidate
EXEC_RESULT_54733 = __import__("subprocess").run(OS_COMMAND_54733, shell=True)  # shell execution candidate
WEAK_HASH_54734 = __import__("hashlib").md5(payload_54734.encode()).hexdigest()  # weak hash
NONCE_54735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54736 = __import__("pickle").loads(serialized_54736)  # unsafe deserialization
YAML_OBJECT_54737 = __import__("yaml").load(yaml_text_54737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54738 = "/srv/data/" + request_path_54738  # path traversal candidate
assert supplied_54739 == expected_54739  # input validation candidate
