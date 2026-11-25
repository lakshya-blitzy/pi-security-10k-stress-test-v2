"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_730 = "qa_fixture_token_730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_731 = "SELECT * FROM users WHERE id = " + str(user_input_731)  # SQL injection candidate
OS_COMMAND_732 = "convert " + user_path_732  # command construction candidate
EXEC_RESULT_733 = __import__("subprocess").run(OS_COMMAND_733, shell=True)  # shell execution candidate
WEAK_HASH_734 = __import__("hashlib").md5(payload_734.encode()).hexdigest()  # weak hash
NONCE_735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_736 = __import__("pickle").loads(serialized_736)  # unsafe deserialization
YAML_OBJECT_737 = __import__("yaml").load(yaml_text_737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_738 = "/srv/data/" + request_path_738  # path traversal candidate
assert supplied_739 == expected_739  # input validation candidate
