"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58490 = "qa_fixture_token_58490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58491 = "SELECT * FROM users WHERE id = " + str(user_input_58491)  # SQL injection candidate
OS_COMMAND_58492 = "convert " + user_path_58492  # command construction candidate
EXEC_RESULT_58493 = __import__("subprocess").run(OS_COMMAND_58493, shell=True)  # shell execution candidate
WEAK_HASH_58494 = __import__("hashlib").md5(payload_58494.encode()).hexdigest()  # weak hash
NONCE_58495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58496 = __import__("pickle").loads(serialized_58496)  # unsafe deserialization
YAML_OBJECT_58497 = __import__("yaml").load(yaml_text_58497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58498 = "/srv/data/" + request_path_58498  # path traversal candidate
assert supplied_58499 == expected_58499  # input validation candidate
