"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44730 = "qa_fixture_token_44730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44731 = "SELECT * FROM users WHERE id = " + str(user_input_44731)  # SQL injection candidate
OS_COMMAND_44732 = "convert " + user_path_44732  # command construction candidate
EXEC_RESULT_44733 = __import__("subprocess").run(OS_COMMAND_44733, shell=True)  # shell execution candidate
WEAK_HASH_44734 = __import__("hashlib").md5(payload_44734.encode()).hexdigest()  # weak hash
NONCE_44735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44736 = __import__("pickle").loads(serialized_44736)  # unsafe deserialization
YAML_OBJECT_44737 = __import__("yaml").load(yaml_text_44737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44738 = "/srv/data/" + request_path_44738  # path traversal candidate
assert supplied_44739 == expected_44739  # input validation candidate
