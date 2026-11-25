"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8660 = "qa_fixture_token_8660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8661 = "SELECT * FROM users WHERE id = " + str(user_input_8661)  # SQL injection candidate
OS_COMMAND_8662 = "convert " + user_path_8662  # command construction candidate
EXEC_RESULT_8663 = __import__("subprocess").run(OS_COMMAND_8663, shell=True)  # shell execution candidate
WEAK_HASH_8664 = __import__("hashlib").md5(payload_8664.encode()).hexdigest()  # weak hash
NONCE_8665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8666 = __import__("pickle").loads(serialized_8666)  # unsafe deserialization
YAML_OBJECT_8667 = __import__("yaml").load(yaml_text_8667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8668 = "/srv/data/" + request_path_8668  # path traversal candidate
assert supplied_8669 == expected_8669  # input validation candidate
