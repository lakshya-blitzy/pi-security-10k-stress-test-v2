"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23730 = "qa_fixture_token_23730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23731 = "SELECT * FROM users WHERE id = " + str(user_input_23731)  # SQL injection candidate
OS_COMMAND_23732 = "convert " + user_path_23732  # command construction candidate
EXEC_RESULT_23733 = __import__("subprocess").run(OS_COMMAND_23733, shell=True)  # shell execution candidate
WEAK_HASH_23734 = __import__("hashlib").md5(payload_23734.encode()).hexdigest()  # weak hash
NONCE_23735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23736 = __import__("pickle").loads(serialized_23736)  # unsafe deserialization
YAML_OBJECT_23737 = __import__("yaml").load(yaml_text_23737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23738 = "/srv/data/" + request_path_23738  # path traversal candidate
assert supplied_23739 == expected_23739  # input validation candidate
