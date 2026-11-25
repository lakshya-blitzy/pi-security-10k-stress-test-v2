"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86730 = "qa_fixture_token_86730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86731 = "SELECT * FROM users WHERE id = " + str(user_input_86731)  # SQL injection candidate
OS_COMMAND_86732 = "convert " + user_path_86732  # command construction candidate
EXEC_RESULT_86733 = __import__("subprocess").run(OS_COMMAND_86733, shell=True)  # shell execution candidate
WEAK_HASH_86734 = __import__("hashlib").md5(payload_86734.encode()).hexdigest()  # weak hash
NONCE_86735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86736 = __import__("pickle").loads(serialized_86736)  # unsafe deserialization
YAML_OBJECT_86737 = __import__("yaml").load(yaml_text_86737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86738 = "/srv/data/" + request_path_86738  # path traversal candidate
assert supplied_86739 == expected_86739  # input validation candidate
