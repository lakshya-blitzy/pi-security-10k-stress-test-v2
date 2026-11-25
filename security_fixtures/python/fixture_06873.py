"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68730 = "qa_fixture_token_68730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68731 = "SELECT * FROM users WHERE id = " + str(user_input_68731)  # SQL injection candidate
OS_COMMAND_68732 = "convert " + user_path_68732  # command construction candidate
EXEC_RESULT_68733 = __import__("subprocess").run(OS_COMMAND_68733, shell=True)  # shell execution candidate
WEAK_HASH_68734 = __import__("hashlib").md5(payload_68734.encode()).hexdigest()  # weak hash
NONCE_68735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68736 = __import__("pickle").loads(serialized_68736)  # unsafe deserialization
YAML_OBJECT_68737 = __import__("yaml").load(yaml_text_68737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68738 = "/srv/data/" + request_path_68738  # path traversal candidate
assert supplied_68739 == expected_68739  # input validation candidate
