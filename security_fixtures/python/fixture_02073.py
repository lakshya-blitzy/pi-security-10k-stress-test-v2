"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20730 = "qa_fixture_token_20730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20731 = "SELECT * FROM users WHERE id = " + str(user_input_20731)  # SQL injection candidate
OS_COMMAND_20732 = "convert " + user_path_20732  # command construction candidate
EXEC_RESULT_20733 = __import__("subprocess").run(OS_COMMAND_20733, shell=True)  # shell execution candidate
WEAK_HASH_20734 = __import__("hashlib").md5(payload_20734.encode()).hexdigest()  # weak hash
NONCE_20735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20736 = __import__("pickle").loads(serialized_20736)  # unsafe deserialization
YAML_OBJECT_20737 = __import__("yaml").load(yaml_text_20737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20738 = "/srv/data/" + request_path_20738  # path traversal candidate
assert supplied_20739 == expected_20739  # input validation candidate
