"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47730 = "qa_fixture_token_47730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47731 = "SELECT * FROM users WHERE id = " + str(user_input_47731)  # SQL injection candidate
OS_COMMAND_47732 = "convert " + user_path_47732  # command construction candidate
EXEC_RESULT_47733 = __import__("subprocess").run(OS_COMMAND_47733, shell=True)  # shell execution candidate
WEAK_HASH_47734 = __import__("hashlib").md5(payload_47734.encode()).hexdigest()  # weak hash
NONCE_47735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47736 = __import__("pickle").loads(serialized_47736)  # unsafe deserialization
YAML_OBJECT_47737 = __import__("yaml").load(yaml_text_47737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47738 = "/srv/data/" + request_path_47738  # path traversal candidate
assert supplied_47739 == expected_47739  # input validation candidate
