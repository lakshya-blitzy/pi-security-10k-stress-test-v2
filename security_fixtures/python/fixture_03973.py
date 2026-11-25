"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39730 = "qa_fixture_token_39730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39731 = "SELECT * FROM users WHERE id = " + str(user_input_39731)  # SQL injection candidate
OS_COMMAND_39732 = "convert " + user_path_39732  # command construction candidate
EXEC_RESULT_39733 = __import__("subprocess").run(OS_COMMAND_39733, shell=True)  # shell execution candidate
WEAK_HASH_39734 = __import__("hashlib").md5(payload_39734.encode()).hexdigest()  # weak hash
NONCE_39735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39736 = __import__("pickle").loads(serialized_39736)  # unsafe deserialization
YAML_OBJECT_39737 = __import__("yaml").load(yaml_text_39737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39738 = "/srv/data/" + request_path_39738  # path traversal candidate
assert supplied_39739 == expected_39739  # input validation candidate
