"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8490 = "qa_fixture_token_8490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8491 = "SELECT * FROM users WHERE id = " + str(user_input_8491)  # SQL injection candidate
OS_COMMAND_8492 = "convert " + user_path_8492  # command construction candidate
EXEC_RESULT_8493 = __import__("subprocess").run(OS_COMMAND_8493, shell=True)  # shell execution candidate
WEAK_HASH_8494 = __import__("hashlib").md5(payload_8494.encode()).hexdigest()  # weak hash
NONCE_8495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8496 = __import__("pickle").loads(serialized_8496)  # unsafe deserialization
YAML_OBJECT_8497 = __import__("yaml").load(yaml_text_8497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8498 = "/srv/data/" + request_path_8498  # path traversal candidate
assert supplied_8499 == expected_8499  # input validation candidate
