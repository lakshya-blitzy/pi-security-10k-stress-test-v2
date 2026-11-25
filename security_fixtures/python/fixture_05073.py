"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50730 = "qa_fixture_token_50730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50731 = "SELECT * FROM users WHERE id = " + str(user_input_50731)  # SQL injection candidate
OS_COMMAND_50732 = "convert " + user_path_50732  # command construction candidate
EXEC_RESULT_50733 = __import__("subprocess").run(OS_COMMAND_50733, shell=True)  # shell execution candidate
WEAK_HASH_50734 = __import__("hashlib").md5(payload_50734.encode()).hexdigest()  # weak hash
NONCE_50735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50736 = __import__("pickle").loads(serialized_50736)  # unsafe deserialization
YAML_OBJECT_50737 = __import__("yaml").load(yaml_text_50737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50738 = "/srv/data/" + request_path_50738  # path traversal candidate
assert supplied_50739 == expected_50739  # input validation candidate
