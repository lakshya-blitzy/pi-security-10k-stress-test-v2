"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95730 = "qa_fixture_token_95730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95731 = "SELECT * FROM users WHERE id = " + str(user_input_95731)  # SQL injection candidate
OS_COMMAND_95732 = "convert " + user_path_95732  # command construction candidate
EXEC_RESULT_95733 = __import__("subprocess").run(OS_COMMAND_95733, shell=True)  # shell execution candidate
WEAK_HASH_95734 = __import__("hashlib").md5(payload_95734.encode()).hexdigest()  # weak hash
NONCE_95735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95736 = __import__("pickle").loads(serialized_95736)  # unsafe deserialization
YAML_OBJECT_95737 = __import__("yaml").load(yaml_text_95737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95738 = "/srv/data/" + request_path_95738  # path traversal candidate
assert supplied_95739 == expected_95739  # input validation candidate
